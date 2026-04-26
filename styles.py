# Custom CSS for Hunar App

def get_custom_styles():
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Noto+Sans+Arabic:wght@400;700&display=swap');

    /* Global Overrides */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #0F172A 0%, #1E3A5F 100%);
        color: #F8FAFC;
    }
    
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    /* Hide Streamlit Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom Container */
    .stMainBlockContainer {
        padding-top: 2rem;
        max-width: 900px;
    }

    /* Hero Styling */
    .hero-section {
        text-align: center;
        padding: 4rem 1rem;
        margin-bottom: 2rem;
    }

    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 4rem;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    
    .sub-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #94A3B8;
        margin-bottom: 1rem;
    }
    
    .hero-desc {
        font-size: 1.1rem;
        color: #CBD5E1;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
        text-align: center;
    }

    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 2rem;
        font-size: 0.9rem;
        font-weight: 600;
        color: #38BDF8;
        margin-top: 2rem;
    }

    /* Talent Card Styling */
    .talent-card {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        color: #0F172A;
        margin-top: 2rem;
        animation: fadeIn 0.8s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Section Headers with Accent */
    .section-header {
        color: #0F172A;
        font-weight: 700;
        border-left: 4px solid #0891B2;
        padding-left: 12px;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    /* Skill Tags (Pills) */
    .skill-tag-primary {
        background: #DBEAFE;
        color: #1E40AF;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;
    }

    .skill-tag-additional {
        background: #EDE9FE;
        color: #6D28D9;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;
    }

    .skill-tag-soft {
        background: #D1FAE5;
        color: #065F46;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;
    }

    /* Language Badges */
    .lang-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .lang-urdu { background: #D1FAE5; color: #065F46; }
    .lang-english { background: #DBEAFE; color: #1E40AF; }
    .lang-roman { background: #FFEDD5; color: #9A3412; }
    .lang-mixed { background: #F3E8FF; color: #7E22CE; }

    /* Opportunity Cards */
    .opp-card {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.2s;
    }
    .opp-card:hover {
        border-color: #0891B2;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    .match-badge {
        font-size: 0.75rem;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 4px;
        float: right;
    }
    .match-high { background: #D1FAE5; color: #065F46; }
    .match-med { background: #FFEDD5; color: #9A3412; }
    .match-low { background: #F1F5F9; color: #475569; }

    /* CTA Button */
    .stButton>button {
        background-color: #0891B2 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        background-color: #0E7490 !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }

    /* Personal Story Section */
    .story-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 3rem;
        font-style: italic;
    }

    /* RTL Support for Urdu */
    .rtl {
        direction: rtl;
        text-align: right;
        font-family: 'Noto Sans Arabic', sans-serif;
    }

    .footer {
        text-align: center;
        padding: 2rem;
        color: #94A3B8;
        font-size: 0.875rem;
    }
    </style>
    """
