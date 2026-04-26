import json
import os
from groq import Groq
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables
load_dotenv()

def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    try:
        return Groq(api_key=api_key)
    except Exception:
        return None


def extract_talent_data(user_description: str) -> Dict[str, Any]:
    """
    Parses informal text (English, Urdu, or Roman Urdu) to extract structured talent data using Groq (Llama 3).
    """
    client = get_client()
    if not client:
        return {
            "error": "Groq API Key not found. Please set the GROQ_API_KEY in Streamlit secrets or .env file.",
            "Primary_Skills": [],
            "Secondary_Skills": [],
            "Soft_Skills": [],
            "Confidence_Score": 0.0,
            "Suggested_Job_Titles": [],
            "Bridge_Skills": []
        }

    prompt = f"""
    You are an expert Talent Acquisition Specialist specializing in informal labor markets in Pakistan.
    Analyze the following description of a worker's skills, which might be in English, Urdu, or Roman Urdu.
    
    User Description: "{user_description}"
    
    Extract the following information into a valid JSON object:
    1. "Primary_Skills": List of 2-3 most strong technical/hard skills.
    2. "Secondary_Skills": List of additional technical skills or tools mentioned.
    3. "Soft_Skills": List of 2-3 behavioral or interpersonal skills (e.g. Communication, Problem Solving, Urdu/English proficiency).
    4. "Confidence_Score": A float between 0 and 1 representing how clearly the skills are defined.
    5. "Suggested_Job_Titles": List of 3 formal job titles this person could apply for.
    6. "Bridge_Skills": A list of 1 or 2 specific skills or certifications they should learn to double their earning potential.

    Requirements:
    - Respond ONLY with the JSON object.
    - If the input is in Roman Urdu or Urdu, translate the extracted labels into English but keep the context.
    - Be specific (e.g., instead of "Mobile repair", use "Hardware Diagnostics" or "Circuit Repair").
    
    Example Input: "Main mobile repair karta hoon aur thora coding seekha hai"
    Example Output:
    {{
        "Primary_Skills": ["Mobile Hardware Diagnostics", "Basic Software Troubleshooting"],
        "Secondary_Skills": ["Introductory Programming (Python)", "Soldering"],
        "Soft_Skills": ["Customer Service", "Technical Communication", "Analytical Thinking"],
        "Confidence_Score": 0.85,
        "Suggested_Job_Titles": ["Junior Smartphone Technician", "Technical Support Representative", "Electronics Repair Apprentice"],
        "Bridge_Skills": ["Advanced Chip-Level Repairing", "Full-stack Web Development basics"]
    }}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a professional talent mapper. Return results in JSON format only."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        extracted_data = json.loads(response.choices[0].message.content)
        return extracted_data
    except Exception as e:
        return {
            "error": str(e),
            "Primary_Skills": [],
            "Secondary_Skills": [],
            "Soft_Skills": [],
            "Confidence_Score": 0.0,
            "Suggested_Job_Titles": ["No match found"],
            "Bridge_Skills": ["Unable to determine"]
        }

if __name__ == "__main__":
    # Test logic
    test_input = "Main mobile repair karta hoon aur thora coding seekha hai"
    result = extract_talent_data(test_input)
    print(json.dumps(result, indent=4))
