import streamlit as st
import processor
from styles import get_custom_styles

# Page configuration
st.set_page_config(
    page_title="Hunar - Talent Mapper",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS
st.markdown(get_custom_styles(), unsafe_allow_html=True)

# Translation Dictionary
TEXTS = {
    "English": {
        "title": "Hunar",
        "subtitle": "Mapping informal skills to formal opportunities.",
        "input_label": "Describe your work in your own words:",
        "placeholder": "e.g., 'Main mobile repair karta hoon aur thora coding seekha hai'",
        "button": "Generate Digital Talent Card",
        "processing": "Analyzing your expertise...",
        "verified": "Verified Potential",
        "primary": "Primary Expertise",
        "secondary": "Additional Strengths",
        "jobs": "Suggested Pathways",
        "bridge": "Bridge Skills to Double Earnings",
        "badge_text": "Skill Match: High"
    },
    "Urdu": {
        "title": "ہنر",
        "subtitle": "غیر رسمی مہارتوں کو باقاعدہ ملازمتوں سے جوڑنا۔",
        "input_label": "اپنا کام اپنے الفاظ میں بیان کریں:",
        "placeholder": "مثال کے طور پر: 'میں موبائل ریپیئر کرتا ہوں اور کچھ ویب ڈیزائننگ بھی آتی ہے'",
        "button": "ڈیجیٹل ٹیلنٹ کارڈ بنائیں",
        "processing": "تجزیہ کیا جا رہا ہے...",
        "verified": "تصدیق شدہ صلاحیت",
        "primary": "بنیادی مہارت",
        "secondary": "اضافی طاقتیں",
        "jobs": "مجوزہ راستے",
        "bridge": "آمدنی دگنی کرنے کے لیے ضروری ہنر",
        "badge_text": "ہنر کی میچ: اعلیٰ"
    }
}

# Language Selector
lang = st.sidebar.selectbox("Language / زبان", ["English", "Urdu"])
t = TEXTS[lang]
is_rtl = "rtl" if lang == "Urdu" else ""

# Header
st.markdown(f'<h1 class="main-title {is_rtl}">{t["title"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-title {is_rtl}">{t["subtitle"]}</p>', unsafe_allow_html=True)

# Input Section
with st.container():
    user_input = st.text_area(
        label=t["input_label"],
        placeholder=t["placeholder"],
        height=150,
        key="desc_input"
    )
    
    if st.button(t["button"]):
        if user_input.strip() == "":
            st.warning("Please enter a description / براہ کرم تفصیل درج کریں")
        else:
            with st.spinner(t["processing"]):
                data = processor.extract_talent_data(user_input)
                
                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    # Talent Card
                    st.markdown('<div class="talent-card">', unsafe_allow_html=True)
                    
                    # Badge logic
                    if data.get("Confidence_Score", 0) > 0.8:
                        st.markdown(f'<span class="badge">✦ {t["verified"]}</span>', unsafe_allow_html=True)
                    
                    st.markdown(f'<h2 class="{is_rtl}">{t["primary"]}</h2>', unsafe_allow_html=True)
                    for skill in data.get("Primary_Skills", []):
                        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
                    
                    st.markdown(f'<h3 style="margin-top:20px;" class="{is_rtl}">{t["secondary"]}</h3>', unsafe_allow_html=True)
                    for skill in data.get("Secondary_Skills", []):
                        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
                    
                    st.markdown(f'<hr>', unsafe_allow_html=True)
                    st.markdown(f'<h3 class="{is_rtl}">{t["jobs"]}</h3>', unsafe_allow_html=True)
                    st.write(", ".join(data.get("Suggested_Job_Titles", [])))
                    
                    # Bridge Skills Section
                    st.markdown(f'''
                    <div class="bridge-section">
                        <h4 class="{is_rtl}" style="margin-top:0; color:#00796B;">🚀 {t["bridge"]}</h4>
                        <ul class="{is_rtl}">
                            {" ".join([f"<li>{s}</li>" for s in data.get("Bridge_Skills", [])])}
                        </ul>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)

# Footer Info
st.markdown("---")
st.caption("Powered by Hunar AI - Mardan Region Talent Hub")
