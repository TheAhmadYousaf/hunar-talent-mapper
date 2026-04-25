# Custom CSS for Hunar App

def get_custom_styles():
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Noto+Sans+Arabic:wght@400;700&display=swap');

    /* Global Overrides */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F7FAFC;
        color: #2D3748;
    }

    /* Hide Streamlit Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom Container */
    .stMainBlockContainer {
        padding-top: 2rem;
        max-width: 800px;
    }

    /* Header Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3rem;
        color: #00796B; /* Teal */
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        font-size: 1.1rem;
        color: #718096;
        text-align: center;
        margin-bottom: 3rem;
    }

    /* Talent Card Styling */
    .talent-card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0, 168, 107, 0.05);
        border: 1px solid #E2E8F0;
        margin-top: 2rem;
        animation: fadeIn 0.8s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .badge {
        background: #E6FFFA;
        color: #00796B;
        padding: 4px 12px;
        border-radius: 99px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 1rem;
    }

    .skill-tag {
        background: #F1F5F9;
        color: #475569;
        padding: 6px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;
        border: 1px solid #E2E8F0;
    }

    .bridge-section {
        background: #F0FDFA;
        border-left: 4px solid #00A86B;
        padding: 1.5rem;
        border-radius: 0 12px 12px 0;
        margin-top: 2rem;
    }

    /* Buttons */
    .stButton>button {
        background-color: #00796B !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #00695C !important;
        box-shadow: 0 4px 12px rgba(0, 121, 107, 0.2);
        transform: translateY(-1px);
    }

    /* Input Area */
    .stTextArea textarea {
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* RTL Support for Urdu */
    .rtl {
        direction: rtl;
        text-align: right;
        font-family: 'Noto Sans Arabic', sans-serif;
    }
    </style>
    """
