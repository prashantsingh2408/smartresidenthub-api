from groq import Groq
import os
from db.get_lead_detail_by_id import get_lead_detail_by_id
from db.get_lead_detail_by_email import get_lead_detail_by_email
from db.get_lead_detail_by_phone import get_lead_detail_by_phone
from db.get_rm_profiles import get_rm_profiles  # Assuming you have a function to get RM profiles
import asyncio  # Import asyncio

os.environ['GROQ_API_KEY'] = "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"

# Update version to production
VERSION = "1.0.0"  # Change this to your production version

async def connect_with_groq_api_mixtral(lead_id=None, email=None, phone=None):
    """Connect to the Groq API and get chat completions for the mixtral model."""
    client = Groq()
    prompt = """
    You are a JSON generator. Only output valid JSON with no additional text or markdown formatting.

    Provide analysis in this format exactly:

    # Sentiment Analysis Responses format
      {
  "site_visit_sentiment_analysis": {
    "title": "Site Visit Sentiment Analysis",
    "overall_sentiment": {
      "score": 85,
      "confidence": 92,
      "color": "green"
    },
    "key_insights": [
      {
        "description": "Strong interest in property amenities",
        "confidence": 90
      },
      {
        "description": "Price sensitivity detected in feedback",
        "confidence": 75
      },
      {
        "description": "Single site visit indicates interest",
        "confidence": 80
      }
    ]
  },
  "conversion_prediction": {
    "title": "Conversion Prediction",
    "conversion_probability": {
      "score": 85,
      "color": "green"
    },
    "engagement_metrics": {
      "engagement_score": 78,
      "follow_up_urgency": "medium"
    }
  },
  "recommended_actions": {
    "title": "Recommended Actions",
    "actions": [
      {
        "action": "Schedule Follow-up Call",
        "description": "Based on the sentiment analysis, a personal follow-up within 48 hours could increase conversion chances."
      },
      {
        "action": "Share Similar Properties",
        "description": "Send curated list of properties matching preferences to maintain engagement."
      },
      {
        "action": "Discuss Financial Options",
        "description": "Address budget concerns by discussing financial options or property price negotiation."
      }
    ]
  }
}


    ## Input data


    use this data 
"""
    # Fetch lead data based on ID or email
    if lead_id:
        content = get_lead_detail_by_id(lead_id)
    elif email:
        content = get_lead_detail_by_email(email=email)
    elif phone:
        content = get_lead_detail_by_phone(phone=phone)
    else:
        raise ValueError("Either lead_id, email or phone must be provided.")

    # Ensure content is a string
    if isinstance(content, list):
        # If content is a list of dictionaries, extract the relevant string data
        content = " ".join([str(item) for item in content])  # Convert each item to string
    elif not isinstance(content, str):
        content = str(content)  # Convert to string if necessary

    content = content + prompt

    role = "system"
    additional_messages = [
        {
            "role": role,
            "content": content
        }
    ]

    # Call the create method without await if it's synchronous
    additional_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=additional_messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    result = ""
    for chunk in additional_completion:
        result += chunk.choices[0].delta.content or ""
        
    # Extract just the JSON part
    try:
        start_idx = result.find('{')
        end_idx = result.rfind('}') + 1
        if start_idx >= 0 and end_idx > 0:
            result = result[start_idx:end_idx].replace("\\n", "").replace("\\\"", "\"").strip()  # Clean up the JSON format
            result = result.replace("\n", "").replace("  ", "")  # Remove newlines and extra spaces for proper JSON format
            result = result.replace("\\", "")  # Remove any remaining backslashes
            result = result.replace("\"{", "{").replace("}\"", "}")  # Clean up any leading/trailing quotes
    except Exception as e:
        print(f"An error occurred while extracting JSON: {e}")
        
    return result  # Return the complete response

async def match_rm_to_lead(lead_id):
    """Match RM profiles to a lead based on the lead ID."""
    # Fetch lead details
    lead_details = get_lead_detail_by_id(lead_id)
    
    # Fetch RM profiles
    rm_profiles = get_rm_profiles()  # Implement this function to fetch RM profiles

    # Prepare the prompt for Groq API
    prompt = f"Match the following RM profiles to the lead details: {lead_details}. Here are the RM profiles: {rm_profiles}."

    # Call the Groq API with the prepared prompt
    client = Groq()
    additional_messages = [
        {
            "role": "system",
            "content": prompt
        }
    ]

    # Call the create method without await if it's synchronous
    additional_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=additional_messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    result = ""
    for chunk in additional_completion:
        result += chunk.choices[0].delta.content or ""

    # Extract just the JSON part
    try:
        start_idx = result.find('{')
        end_idx = result.rfind('}') + 1
        if start_idx >= 0 and end_idx > 0:
            result = result[start_idx:end_idx].replace("\\n", "").replace("\\\"", "\"")  # Clean up the JSON format
    except Exception as e:
        print(f"An error occurred while extracting JSON: {e}")

    return result  # Return the complete response

async def chat_with_lead_and_rm(lead_id, user_message):
    """Chat with the lead and RM profiles based on the lead ID and user message."""
    # Fetch lead details
    lead_details = get_lead_detail_by_id(lead_id)
    
    # Fetch RM profiles
    rm_profiles = get_rm_profiles()

    # Prepare the prompt for Groq API
    prompt = f"Lead Details: {lead_details}\nRM Profiles: {rm_profiles}\nUser Message: {user_message}\nRespond appropriately."

    # Call the Groq API with the prepared prompt
    client = Groq()
    additional_messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    additional_completion = await client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=additional_messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    result = ""
    for chunk in additional_completion:
        result += chunk.choices[0].delta.content or ""

    # Extract just the JSON part
    try:
        start_idx = result.find('{')
        end_idx = result.rfind('}') + 1
        if start_idx >= 0 and end_idx > 0:
            result = result[start_idx:end_idx].replace("\\n", "").replace("\\\"", "\"")  # Clean up the JSON format
    except Exception as e:
        print(f"An error occurred while extracting JSON: {e}")

    return result  # Return the complete response

# Example usage
if __name__ == "__main__":
    lead_id_to_fetch = "1e88b663-d6a1-32c9-bd02-665fb39b80b1"
    email_to_fetch = None  # Replace with the desired email

    # Use asyncio to run the async function
    # response = asyncio.run(connect_with_groq_api_mixtral(lead_id=lead_id_to_fetch, email=email_to_fetch))
    # print("Groq API Response:", response)

    response = asyncio.run(match_rm_to_lead(lead_id_to_fetch))
    print("Top 3 Suitable RMs:", response)


