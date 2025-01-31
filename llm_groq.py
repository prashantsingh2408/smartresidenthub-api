from groq import Groq
import os
from db.get_lead_detail_by_id import get_lead_detail_by_id
from db.get_lead_detail_by_email import get_lead_detail
import asyncio  # Import asyncio

os.environ['GROQ_API_KEY'] = "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"

# Update version to production
VERSION = "1.0.0"  # Change this to your production version

async def connect_with_groq_api_mixtral(lead_id=None, email=None):
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
        content = get_lead_detail(email=email)
    else:
        raise ValueError("Either lead_id or email must be provided.")

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
            result = result[start_idx:end_idx]
    except Exception as e:
        print(f"An error occurred while extracting JSON: {e}")
        
    return result  # Return the complete response

# Example usage
if __name__ == "__main__":
    lead_id_to_fetch = "1e88b663-d6a1-32c9-bd02-665fb39b80b1"
    email_to_fetch = None  # Replace with the desired email

    # Use asyncio to run the async function
    response = asyncio.run(connect_with_groq_api_mixtral(lead_id=lead_id_to_fetch, email=email_to_fetch))
    print("Groq API Response:", response)


