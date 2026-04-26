import streamlit as st
import processor
from styles import get_custom_styles
import uuid
from langdetect import detect, DetectorFactory
import urllib.parse

# Ensure consistent results for language detection
DetectorFactory.seed = 0

# Page configuration
st.set_page_config(
    page_title="Hunar - Talent Mapper",
    page_icon="🇵🇰",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS
st.markdown(get_custom_styles(), unsafe_allow_html=True)

# Initialize session state for profiles if not exists
if 'profiles' not in st.session_state:
    st.session_state.profiles = {}

# Translation Dictionary
TEXTS = {
    "English": {
        "hero_title": "🇵🇰 Hunar",
        "hero_tagline": "You built it. You know it. Now the world can see it.",
        "hero_desc": "Describe your skills in any language — English, Urdu, or Roman Urdu. Get a shareable talent profile in seconds. No CV needed. No degree required.",
        "stats": ["✨ Works in 3 Languages", "⚡ Results in Seconds", "🔗 Shareable Profile"],
        "input_label": "Describe your work in your own words:",
        "placeholder": "e.g., 'Main mobile repair karta hoon aur thora coding seekha hai or I can make websites'",
        "button": "Generate Digital Talent Card",
        "processing": "Analyzing your expertise...",
        "verified": "Verified Potential",
        "primary": "Primary Expertise",
        "secondary": "Additional Strengths",
        "soft_skills": "Professional Qualities",
        "jobs": "Suggested Pathways",
        "bridge": "Bridge Skills to Double Earnings",
        "share_title": "Share Your Profile",
        "copy_link": "📋 Copy Link",
        "whatsapp": "Share on WhatsApp",
        "story_title": "Why Hunar?",
        "story_text": "A 22-year-old in Mardan builds an AI system in his spare time. He has no LinkedIn. No degree yet. No formal work history. By every traditional measure — invisible. By every real measure — talented, driven, and ready. Hunar changes that.",
        "opps_title": "Real Opportunities for You",
        "match_score": "Match Score"
    },
    "Urdu": {
        "hero_title": "🇵🇰 ہنر",
        "hero_tagline": "آپ نے بنایا، آپ جانتے ہیں۔ اب دنیا دیکھے گی۔",
        "hero_desc": "اپنی مہارت کسی بھی زبان میں بیان کریں - انگریزی، اردو، یا رومن اردو۔ سیکنڈوں میں اپنا ٹیلنٹ پروفائل حاصل کریں۔ کسی سی وی یا ڈگری کی ضرورت نہیں۔",
        "stats": ["✨ 3 زبانوں میں دستیاب", "⚡ فوری نتائج", "🔗 شیئر ایبل پروفائل"],
        "input_label": "اپنا کام اپنے الفاظ میں بیان کریں:",
        "placeholder": "مثال کے طور پر: 'میں موبائل ریپیئر کرتا ہوں اور کچھ ویب ڈیزائننگ بھی آتی ہے'",
        "button": "ڈیجیٹل ٹیلنٹ کارڈ بنائیں",
        "processing": "تجزیہ کیا جا رہا ہے...",
        "verified": "تصدیق شدہ صلاحیت",
        "primary": "بنیادی مہارت",
        "secondary": "اضافی طاقتیں",
        "soft_skills": "پیشہ ورانہ خصوصیات",
        "jobs": "مجوزہ راستے",
        "bridge": "آمدنی دگنی کرنے کے لیے ضروری ہنر",
        "share_title": "اپنا پروفائل شیئر کریں",
        "copy_link": "📋 لنک کاپی کریں",
        "whatsapp": "واٹس ایپ پر شیئر کریں",
        "story_title": "ہنر کیوں؟",
        "story_text": "مردان میں ایک 22 سالہ نوجوان فارغ وقت میں AI سسٹم بناتا ہے۔ اس کے پاس کوئی لنکڈ ان نہیں ہے۔ ابھی تک کوئی ڈگری نہیں۔ کوئی رسمی کام کی تاریخ نہیں۔ روایتی معیار کے مطابق — پوشیدہ۔ حقیقی معیار کے مطابق — باصلاحیت، پرجوش، اور تیار۔ ہنر اسے بدل دیتا ہے۔",
        "opps_title": "آپ کے لیے حقیقی مواقع",
        "match_score": "میچ اسکور"
    }
}

OPPORTUNITIES = [
    # Web Dev
    {"name": "Upwork", "emoji": "🔵", "title": "Web Development Gigs", "url": "https://www.upwork.com/freelance-jobs/web-development/", "skills": ["web development", "javascript", "html", "css", "react", "node.js"]},
    {"name": "Fiverr", "emoji": "🟢", "title": "Web Programming Orders", "url": "https://www.fiverr.com/categories/programming-tech/web-programming", "skills": ["web programming", "wordpress", "php", "javascript"]},
    {"name": "RemoteOK", "emoji": "💼", "title": "Remote Web Developer Jobs", "url": "https://remoteok.com/remote-web-developer-jobs", "skills": ["remote web", "fullstack", "frontend", "backend"]},
    {"name": "Rozee.pk", "emoji": "🇵🇰", "title": "Web Developer Jobs (Pakistan)", "url": "https://www.rozee.pk/job/search/q/web-developer", "skills": ["web developer", "laravel", "asp.net", "python"]},
    # Mobile App
    {"name": "Upwork", "emoji": "🔵", "title": "Mobile Development Projects", "url": "https://www.upwork.com/freelance-jobs/mobile-development/", "skills": ["mobile development", "android", "ios", "react native", "swift"]},
    {"name": "Fiverr", "emoji": "📱", "title": "Mobile App Services", "url": "https://www.fiverr.com/categories/programming-tech/mobile-apps", "skills": ["mobile app", "flutter", "dart", "kotlin"]},
    {"name": "Flutter Jobs", "emoji": "💼", "title": "Flutter Developer Roles", "url": "https://flutter.dev/jobs", "skills": ["flutter", "dart", "mobile app developer"]},
    # AI/ML
    {"name": "Kaggle", "emoji": "🤖", "title": "AI & Data Science Jobs", "url": "https://www.kaggle.com/jobs", "skills": ["machine learning", "data science", "ai", "python", "pytorch", "tensorflow"]},
    {"name": "Upwork ML", "emoji": "🔵", "title": "Machine Learning Gigs", "url": "https://www.upwork.com/freelance-jobs/machine-learning/", "skills": ["machine learning", "computer vision", "nlp", "data analysis"]},
    {"name": "Google Summer of Code", "emoji": "🎓", "title": "Open Source Internships", "url": "https://summerofcode.withgoogle.com/", "skills": ["open source", "coding", "software engineering", "programming"]},
    # Technical Pakistan
    {"name": "KPITB Programs", "emoji": "🇵🇰", "title": "KP IT Board Initiatives", "url": "https://kpitb.gov.pk/", "skills": ["it training", "freelancing", "digital skills", "government program"]},
    {"name": "Ignite Pakistan", "emoji": "🇵🇰", "title": "Innovation Fund Projects", "url": "https://ignite.org.pk/", "skills": ["startup", "innovation", "technology", "research"]},
    {"name": "P@SHA", "emoji": "🇵🇰", "title": "IT Industry Roles", "url": "https://pasha.org.pk/", "skills": ["software industry", "it sector", "pakistan jobs"]},
    # Scholarships
    {"name": "Stipendium Hungaricum", "emoji": "🎓", "title": "Hungary Fully Funded", "url": "https://stipendiumhungaricum.hu/apply/", "skills": ["higher education", "scholarship", "international study", "bachelors", "masters"]},
    {"name": "DAAD Germany", "emoji": "🎓", "title": "Germany Study Grants", "url": "https://www.daad.de/en/", "skills": ["research scholarship", "germany", "study abroad"]},
    {"name": "Erasmus Mundus", "emoji": "🎓", "title": "European Joint Degrees", "url": "https://erasmus-plus.ec.europa.eu/", "skills": ["masters degree", "europe", "fully funded scholarship"]}
]

def detect_language_badge(text):
    if not text.strip():
        return None
    try:
        # Simple heuristic for Roman Urdu vs English
        # Roman Urdu often uses 'hai', 'karta', 'hoon', 'hai', 'ka', 'ke'
        roman_urdu_keywords = ['hai', 'hain', 'hoon', 'karta', 'karte', 'karti', 'ka', 'ke', 'ki', 'ko', 'mein', 'par', 'tha', 'thi', 'the', 'raha', 'rahe', 'rahi']
        text_lower = text.lower()
        words = text_lower.split()
        
        has_urdu_chars = any('\u0600' <= c <= '\u06FF' for c in text)
        
        if has_urdu_chars:
            # Check if it also has many English chars (mixed)
            eng_chars = sum(1 for c in text if 'a' <= c.lower() <= 'z')
            if eng_chars > len(text) * 0.3: # More than 30% English chars in Urdu text
                return "🔀 Mixed Language", "lang-mixed"
            return "🇵🇰 Urdu", "lang-urdu"
        
        # Roman Urdu Detection
        roman_score = sum(1 for word in words if word in roman_urdu_keywords)
        if roman_score >= 1:
            return "💬 Roman Urdu", "lang-roman"
            
        lang_code = detect(text)
        if lang_code == 'en':
            return "🌐 English", "lang-english"
        elif lang_code in ['ur', 'fa', 'ar']:
            return "🇵🇰 Urdu", "lang-urdu"
        else:
            return "🌐 English", "lang-english" # Default to English
    except:
        return "🌐 English", "lang-english"

def calculate_match_score(user_skills, opp_skills):
    if not user_skills or not opp_skills:
        return 0
    matched = 0
    user_skills_lower = [s.lower() for s in user_skills]
    for os in opp_skills:
        for us in user_skills_lower:
            if os in us or us in os:
                matched += 1
                break
    score = (matched / len(opp_skills)) * 100
    return min(100, int(score * 2.5)) # Boosting score for better UX, usually opp_skills lists many

def get_match_class(score):
    if score > 80: return "match-high"
    if score > 50: return "match-med"
    return "match-low"

# Language Selector
lang = st.sidebar.selectbox("Language / زبان", ["English", "Urdu"])
t = TEXTS[lang]
is_rtl = "rtl" if lang == "Urdu" else ""

# Handle Shared Profile
query_params = st.query_params
profile_id = query_params.get("profile")

if profile_id:
    # In a real app, this would come from a database. 
    # For this demo, we check session state, or show a mock if it's a specific test ID.
    if profile_id in st.session_state.profiles:
        profile_data = st.session_state.profiles[profile_id]
        
        # Header
        st.markdown(f'''
        <div class="hero-section">
            <h1 class="main-title">{t["hero_title"]}</h1>
            <p class="sub-title">{t["hero_tagline"]}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('<div class="talent-card">', unsafe_allow_html=True)
        st.markdown(f'<h2 class="section-header {is_rtl}">{t["primary"]}</h2>', unsafe_allow_html=True)
        for skill in profile_data.get("Primary_Skills", []):
            st.markdown(f'<span class="skill-tag-primary">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown(f'<h2 class="section-header {is_rtl}">{t["secondary"]}</h2>', unsafe_allow_html=True)
        for skill in profile_data.get("Secondary_Skills", []):
            st.markdown(f'<span class="skill-tag-additional">{skill}</span>', unsafe_allow_html=True)
            
        st.markdown(f'<h2 class="section-header {is_rtl}">{t["soft_skills"]}</h2>', unsafe_allow_html=True)
        for skill in profile_data.get("Soft_Skills", []):
            st.markdown(f'<span class="skill-tag-soft">{skill}</span>', unsafe_allow_html=True)
            
        st.markdown(f'<hr>', unsafe_allow_html=True)
        st.markdown(f'<h2 class="section-header {is_rtl}">{t["jobs"]}</h2>', unsafe_allow_html=True)
        st.write(", ".join(profile_data.get("Suggested_Job_Titles", [])))
        
        st.markdown(f'''
        <div style="background: #F0FDFA; border-left: 4px solid #0891B2; padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">
            <h4 class="{is_rtl}" style="margin-top:0; color:#0891B2;">🚀 {t["bridge"]}</h4>
            <ul class="{is_rtl}">
                {" ".join([f"<li>{s}</li>" for s in profile_data.get("Bridge_Skills", [])])}
            </ul>
        </div>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("Create My Own Profile"):
            st.query_params.clear()
            st.rerun()
            
        st.markdown(f'<div class="footer">Powered by Hunar AI - Mardan Region Talent Hub</div>', unsafe_allow_html=True)
        st.stop()

# Main Interface
# Hero Section
st.markdown(f'''
<div class="hero-section">
    <h1 class="main-title">{t["hero_title"]}</h1>
    <p class="sub-title">{t["hero_tagline"]}</p>
    <p class="hero-desc">{t["hero_desc"]}</p>
    <div class="hero-stats">
        <span>{t["stats"][0]}</span>
        <span>|</span>
        <span>{t["stats"][1]}</span>
        <span>|</span>
        <span>{t["stats"][2]}</span>
    </div>
</div>
''', unsafe_allow_html=True)

# Input Section
with st.container():
    user_input = st.text_area(
        label=t["input_label"],
        placeholder=t["placeholder"],
        height=150,
        key="desc_input"
    )
    
    # Language Detection Badge
    if user_input:
        lang_name, lang_class = detect_language_badge(user_input)
        st.markdown(f'<span class="lang-badge {lang_class}">{lang_name} Detected</span>', unsafe_allow_html=True)
    
    if st.button(t["button"]):
        if user_input.strip() == "":
            st.warning("Please enter a description / براہ کرم تفصیل درج کریں")
        else:
            with st.spinner(t["processing"]):
                data = processor.extract_talent_data(user_input)
                
                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    # Store in session state for shareability
                    uid = str(uuid.uuid4())
                    st.session_state.profiles[uid] = data
                    
                    # Talent Card
                    st.markdown('<div class="talent-card">', unsafe_allow_html=True)
                    
                    if data.get("Confidence_Score", 0) > 0.8:
                        st.markdown(f'<span class="lang-badge lang-urdu" style="background:#0891B2; color:white;">✦ {t["verified"]}</span>', unsafe_allow_html=True)
                    
                    st.markdown(f'<h2 class="section-header {is_rtl}">{t["primary"]}</h2>', unsafe_allow_html=True)
                    for skill in data.get("Primary_Skills", []):
                        st.markdown(f'<span class="skill-tag-primary">{skill}</span>', unsafe_allow_html=True)
                    
                    st.markdown(f'<h2 class="section-header {is_rtl}">{t["secondary"]}</h2>', unsafe_allow_html=True)
                    for skill in data.get("Secondary_Skills", []):
                        st.markdown(f'<span class="skill-tag-additional">{skill}</span>', unsafe_allow_html=True)
                        
                    st.markdown(f'<h2 class="section-header {is_rtl}">{t["soft_skills"]}</h2>', unsafe_allow_html=True)
                    for skill in data.get("Soft_Skills", []):
                        st.markdown(f'<span class="skill-tag-soft">{skill}</span>', unsafe_allow_html=True)
                    
                    st.markdown(f'<hr>', unsafe_allow_html=True)
                    st.markdown(f'<h2 class="section-header {is_rtl}">{t["jobs"]}</h2>', unsafe_allow_html=True)
                    st.write(", ".join(data.get("Suggested_Job_Titles", [])))
                    
                    # Bridge Skills Section
                    st.markdown(f'''
                    <div style="background: #F0FDFA; border-left: 4px solid #0891B2; padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">
                        <h4 class="{is_rtl}" style="margin-top:0; color:#0891B2;">🚀 {t["bridge"]}</h4>
                        <ul class="{is_rtl}">
                            {" ".join([f"<li>{s}</li>" for s in data.get("Bridge_Skills", [])])}
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Share Section
                    st.markdown(f'<h3 class="section-header" style="color:white; border-color:white;">🔗 {t["share_title"]}</h3>', unsafe_allow_html=True)
                    base_url = "https://hunar-talent-mapper-p3jrurcstdm2az2gff5m4v.streamlit.app/"
                    share_url = f"{base_url}?profile={uid}"
                    st.code(share_url)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        # WhatsApp Share
                        whatsapp_msg = urllib.parse.quote(f"Check out my Hunar skill profile: {share_url}")
                        wa_link = f"https://wa.me/?text={whatsapp_msg}"
                        st.markdown(f'''
                        <a href="{wa_link}" target="_blank" style="text-decoration:none;">
                            <div style="background:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; font-weight:700;">
                                💬 {t["whatsapp"]}
                            </div>
                        </a>
                        ''', unsafe_allow_html=True)
                    
                    # Opportunity Cards (Task 4)
                    st.markdown(f'<h2 class="section-header" style="color:white; border-color:white;">🎯 {t["opps_title"]}</h2>', unsafe_allow_html=True)
                    
                    user_all_skills = data.get("Primary_Skills", []) + data.get("Secondary_Skills", []) + data.get("Soft_Skills", [])
                    
                    scored_opps = []
                    for opp in OPPORTUNITIES:
                        score = calculate_match_score(user_all_skills, opp["skills"])
                        scored_opps.append({**opp, "score": score})
                    
                    # Sort and take top 6
                    scored_opps = sorted(scored_opps, key=lambda x: x["score"], reverse=True)[:6]
                    
                    for opp in scored_opps:
                        m_class = get_match_class(opp["score"])
                        st.markdown(f'''
                        <div class="opp-card">
                            <span class="match-badge {m_class}">{t["match_score"]}: {opp["score"]}%</span>
                            <h4 style="margin:0; color:#0F172A;">{opp["emoji"]} {opp["name"]}</h4>
                            <p style="margin:5px 0; color:#475569; font-weight:600;">{opp["title"]}</p>
                            <div style="margin-top:10px;">
                                {" ".join([f'<span style="font-size:0.7rem; background:#E2E8F0; padding:2px 6px; border-radius:4px; margin-right:4px;">{s}</span>' for s in opp["skills"][:3]])}
                            </div>
                            <div style="margin-top:15px; text-align:right;">
                                <a href="{opp["url"]}" target="_blank" style="color:#0891B2; text-decoration:none; font-weight:700;">Explore →</a>
                            </div>
                        </div>
                        ''', unsafe_allow_html=True)

# Personal Story Section (Task 6)
st.markdown(f'''
<div class="story-section">
    <h3 style="margin-top:0; color:#38BDF8;">{t["story_title"]}</h3>
    <p>{t["story_text"]}</p>
</div>
''', unsafe_allow_html=True)

# Footer Info
st.markdown(f'<div class="footer">Powered by Hunar AI - Mardan Region Talent Hub</div>', unsafe_allow_html=True)
