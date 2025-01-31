from groq import Groq
import os

os.environ['GROQ_API_KEY'] = "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"

# Update version to production
VERSION = "1.0.0"  # Change this to your production version

def connect_with_groq_api_mixtral(role=None, content=None):
    """Connect to the Groq API and get chat completions for the mixtral model."""
    client = Groq()
    role = "system"
    content = """
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

    [{'assigned_rm_id': '7d47c093-b00a-4f0c-bbf9-4023e678ff89',
      'budget': 50000,
      'conversion_probability': 0.85,
      'created_at': '2025-01-31T00:00:00+00:00',
      'email': 'john.doe@example.com',
      'id': 'b42878d2-dba4-4c3c-93f7-0756be06f24d',
      'interaction_history': [{'action': 'Initial Contact', 'date': '2025-01-29'}],
      'last_contact_date': '2025-01-30T14:00:00+00:00',
      'name': 'John Doe',
      'phone': '+1234567890',
      'preferences': {'industry': 'Finance', 'location': 'New York'},
      'sentiment': 'Positive',
      'source': 'Website',
      'status': 'New',
      'updated_at': '2025-01-31T00:00:00+00:00'},
    {'assigned_rm_id': 'f917f9c9-53a6-41d4-9379-abb1e6354b39',
      'budget': 35000,
      'conversion_probability': 0.75,
      'created_at': '2025-01-30T15:00:00+00:00',
      'email': 'jane.smith@example.com',
      'id': '46c9d755-e079-4a0a-81fa-6ffbd8fa4c5b',
      'interaction_history': [{'action': 'Follow-up Call', 'date': '2025-01-30'}],
      'last_contact_date': '2025-01-30T12:00:00+00:00',
      'name': 'Jane Smith',
      'phone': '+1234567891',
      'preferences': {'industry': 'Retail', 'location': 'Los Angeles'},
      'sentiment': 'Neutral',
      'source': 'Referral',
      'status': 'Contacted',
      'updated_at': '2025-01-30T15:00:00+00:00'}]

    {
            "lead_name": "John Doe",
            "feedback": "The property was amazing! I loved the spacious rooms, the natural  lighting, and the amenities provided. "
                        "The location is perfect for my commute, and I can definitely see myself living here. "
                        "However, I wish the price was a bit more flexible. Overall, a fantastic place!"
    },
    """

    
    # Define a message to send to the Groq model
    additional_messages = [
        {
            "role": role,
            "content": content
        }
    ]

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
    except:
        pass
        
    return result

# Call the functions to connect with Groq API
# connect_with_groq_api_deepseek()

connect_with_groq_api_mixtral()
print(connect_with_groq_api_mixtral())


