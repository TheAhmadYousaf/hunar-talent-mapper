import json
import os
from google import genai
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables
load_dotenv()

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        return genai.Client(api_key=api_key)
    except Exception:
        return None


def extract_talent_data(user_description: str) -> Dict[str, Any]:
    """
    Parses informal text (English, Urdu, or Roman Urdu) to extract structured talent data using Gemini 2.0.
    """
    client = get_client()
    if not client:
        return {
            "error": "Gemini API Key not found or initialization failed. Please set the GEMINI_API_KEY in .env file.",
            "Primary_Skills": [],
            "Secondary_Skills": [],
            "Confidence_Score": 0.0,
            "Suggested_Job_Titles": [],
            "Bridge_Skills": []
        }

    prompt = f"""
    You are an expert Talent Acquisition Specialist specializing in informal labor markets in Pakistan.
    Analyze the following description of a worker's skills, which might be in English, Urdu, or Roman Urdu.
    
    User Description: "{user_description}"
    
    Extract the following information into a valid JSON object:
    1. "Primary_Skills": List of 2-3 most strong skills.
    2. "Secondary_Skills": List of additional skills or tools mentioned.
    3. "Confidence_Score": A float between 0 and 1 representing how clearly the skills are defined.
    4. "Suggested_Job_Titles": List of 3 formal job titles this person could apply for.
    5. "Bridge_Skills": A list of 1 or 2 specific skills or certifications they should learn to double their earning potential.

    Requirements:
    - Respond ONLY with the JSON object.
    - If the input is in Roman Urdu or Urdu, translate the extracted labels into English but keep the context.
    - Be specific (e.g., instead of "Mobile repair", use "Hardware Diagnostics" or "Circuit Repair").
    
    Example Input: "Main mobile repair karta hoon aur thora coding seekha hai"
    Example Output:
    {{
        "Primary_Skills": ["Mobile Hardware Diagnostics", "Basic Software Troubleshooting"],
        "Secondary_Skills": ["Introductory Programming (Python)", "Customer Service"],
        "Confidence_Score": 0.85,
        "Suggested_Job_Titles": ["Junior Smartphone Technician", "Technical Support Representative", "Electronics Repair Apprentice"],
        "Bridge_Skills": ["Advanced Chip-Level Repairing", "Full-stack Web Development basics"]
    }}
    """

    try:
        # Using gemini-flash-latest based on the list of available models
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
            }
        )
        
        extracted_data = json.loads(response.text)
        return extracted_data
    except Exception as e:
        return {
            "error": str(e),
            "Primary_Skills": [],
            "Secondary_Skills": [],
            "Confidence_Score": 0.0,
            "Suggested_Job_Titles": ["No match found"],
            "Bridge_Skills": ["Unable to determine"]
        }

if __name__ == "__main__":
    # Test logic
    test_input = "Main mobile repair karta hoon aur thora coding seekha hai"
    result = extract_talent_data(test_input)
    print(json.dumps(result, indent=4))
