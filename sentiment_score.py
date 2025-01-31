import pandas as pd
from textblob import TextBlob
import random

# Sample dataset with more detailed feedback
feedback_data = [
    {
        "lead_name": "John Doe",
        "feedback": "The property was amazing! I loved the spacious rooms, the natural lighting, and the amenities provided. "
                    "The location is perfect for my commute, and I can definitely see myself living here. "
                    "However, I wish the price was a bit more flexible. Overall, a fantastic place!"
    },
    {
        "lead_name": "Jane Smith",
        "feedback": "It was okay, but I expected better. The pictures online were slightly misleading, and the space felt smaller than anticipated. "
                    "The surroundings are decent, but I’m not sure if it’s the right fit for my family. "
                    "Still, I appreciate the effort from the sales team in showing me around."
    },
    {
        "lead_name": "Alice Brown",
        "feedback": "Not interested at all. The location is bad, and the neighborhood does not feel safe. "
                    "Additionally, the property lacks essential amenities like parking space and a gym, which are very important to me. "
                    "I found better options elsewhere that are more affordable and in a much better area."
    },
    {
        "lead_name": "Bob Johnson",
        "feedback": "Great amenities, but a bit expensive. The clubhouse, swimming pool, and security services are top-notch. "
                    "I really liked the modern design and the overall atmosphere. "
                    "If the price was more competitive, I would have seriously considered this as my next home."
    },
    {
        "lead_name": "Emma Wilson",
        "feedback": "I absolutely loved this property! The view from the balcony is breathtaking, and the interior design is modern and stylish. "
                    "The customer service was excellent, and they answered all my queries. "
                    "Although the pricing is on the higher side, I feel it’s worth it for the quality offered. "
                    "If everything goes smoothly, I will definitely finalize this soon."
    },
    {
        "lead_name": "David Lee",
        "feedback": "I had a mixed experience. While the property itself is well-maintained and the features are appealing, "
                    "the location is not ideal for my daily commute. The pricing also seems slightly overvalued compared to similar properties in the area. "
                    "I’m still considering my options before making a final decision."
    },
    {
        "lead_name": "Sophia Martinez",
        "feedback": "Very disappointing. The property was not well-maintained, and the photos online did not match reality. "
                    "The walls had cracks, and some of the facilities were in poor condition. "
                    "I expected much better given the price range. I will not be considering this any further."
    },
]

# Convert to DataFrame
df = pd.DataFrame(feedback_data)

def get_sentiment_score(feedback):
    """Analyze sentiment score using TextBlob."""
    return TextBlob(feedback).sentiment.polarity

def categorize_sentiment(score):
    """Categorize lead into buckets based on sentiment score."""
    if score > 0.5:
        return "Highly Interested"
    elif 0 < score <= 0.5:
        return "Interested"
    elif -0.5 <= score <= 0:
        return "Moderate"
    else:
        return "Not Interested"

def predict_conversion_chance(category):
    """Generate a random predictive conversion chance based on category."""
    chances = {
        "Highly Interested": random.randint(80, 100),
        "Interested": random.randint(50, 80),
        "Moderate": random.randint(20, 50),
        "Not Interested": random.randint(0, 20),
    }
    return chances[category]

# Apply sentiment analysis
df["sentiment_score"] = df["feedback"].apply(get_sentiment_score)
df["category"] = df["sentiment_score"].apply(categorize_sentiment)
df["conversion_chance"] = df["category"].apply(predict_conversion_chance)

# Display results
print(df)
