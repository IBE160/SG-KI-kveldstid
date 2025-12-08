from typing import Dict, Any
import openai
import json
import os # Added for environment variable check
from .config import settings

# Initialize the OpenAI client
# It will automatically pick up the OPENAI_API_KEY from the environment/settings
client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

def extract_structured_data(raw_text: str) -> Dict[str, Any]:
    """
    Extracts structured data from the raw text of a CV using the OpenAI API.

    Args:
        raw_text: The raw text content of the CV.

    Returns:
        A dictionary containing the structured data, or an empty dictionary on failure.
    """
    # If in a testing environment, return mock data to avoid actual API calls
    if os.environ.get("TESTING_ENV") == "true":
        return {
            "contact_info": {
                "name": "Mock Test User",
                "email": "mock.test@example.com",
                "phone": "000-000-0000"
            },
            "summary": "Mock summary for testing purposes.",
            "experience": [
                {
                    "title": "Mock Software Engineer",
                    "company": "Mock Corp",
                    "dates": "2020 - Present",
                    "description": "Mock description of duties."
                }
            ],
            "education": [
                {
                    "degree": "Mock Bachelor of Science",
                    "university": "Mock University",
                    "year": 2022
                }
            ],
            "skills": ["Mock Python", "Mock FastAPI", "Mock React"]
        }
    system_prompt = """
    You are an expert CV parser. Your task is to extract structured information from the provided CV text and return it as a valid JSON object.
    
    The JSON object must have the following structure. Do not add any extra fields or deviate from this structure.
    If a section or field is not found in the CV, omit it from the JSON object.

    {
      "contact_info": {
        "name": "string (full name)",
        "email": "string (email address)",
        "phone": "string (phone number)"
      },
      "summary": "string (a brief professional summary)",
      "experience": [
        {
          "title": "string (job title)",
          "company": "string (company name)",
          "dates": "string (e.g., 'Jan 2022 - Present' or '2020-2022')",
          "description": "string (a description of responsibilities and achievements)"
        }
      ],
      "education": [
        {
          "degree": "string (degree name)",
          "university": "string (university name)",
          "year": "integer or string (graduation year)"
        }
      ],
      "skills": ["string (a list of skills)"]
    }
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo", # As specified in architecture.md
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": raw_text}
            ]
        )
        
        # The response from the API is a JSON string, so we need to parse it.
        if response.choices[0].message.content:
            return json.loads(response.choices[0].message.content)
        else:
            return {"error": "Failed to extract data: No content from AI model."}

    except openai.APIError as e:
        # Handle API error here, e.g. logging
        print(f"OpenAI API returned an API Error: {e}")
        return {"error": f"OpenAI API Error: {e}"}
    except json.JSONDecodeError as e:
        # Handle JSON parsing error
        print(f"Failed to decode JSON from AI response: {e}")
        return {"error": "Failed to decode JSON from AI response."}
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
        return {"error": f"An unexpected error occurred: {e}"}
