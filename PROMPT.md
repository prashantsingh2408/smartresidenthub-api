# API (Prompt)

Provide analysis in this format extactly

# Sentiment Analysis Respones format
{
  "tabs": {
    "sentiment": {
      "title": "Site Visit Sentiment Analysis",
      "overall_sentiment": {
        "label": "Overall Sentiment",
        "description": "Based on site visit feedback and interactions",
        "value": "{lead.sentiment}"
      },
      "key_insights": [
        "Shows strong interest in property amenities",
        "Price sensitivity detected in conversations",
        "Multiple site visits indicate serious intent"
      ]
    },
    "prediction": {
      "title": "Conversion Prediction",
      "conversion_probability": {
        "label": "Conversion Probability",
        "description": "Based on historical data and current engagement",
        "value": "{lead.conversion_probability}%"
      },
      "contributing_factors": [
        "Site visit engagement level",
        "Budget alignment with property options",
        "Response rate to communications"
      ]
    },
    "suggestions": {
      "title": "Recommended Actions",
      "recommended_actions": [
        {
          "action": "Schedule Follow-up Call",
          "description": "Based on the sentiment analysis, a personal follow-up within 48 hours could increase conversion chances."
        },
        {
          "action": "Share Similar Properties",
          "description": "Send curated list of properties matching preferences to maintain engagement."
        },
        {
          "action": "Offer Virtual Tour",
          "description": "Provide a virtual tour option for better visualization of the property."
        }
      ]
    }
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


