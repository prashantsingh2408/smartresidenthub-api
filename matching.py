from openai import OpenAI

def match_rm_with_property(rm_profiles, property_data):
    prompt = f"""
    Match the relationship managers with the most suitable properties based on the following criteria:
    - Location proximity
    - Skills match
    - Years of experience
    - Language compatibility
    - Client feedback score

    RM Profiles:
    {rm_profiles}

    Property Data:
    {property_data}

    Provide a ranked list of RM matches for the property.
    """

    response = openai.Completion.create(
        engine="davinci",  # You can change this to another LLM model you are using
        prompt=prompt,
        max_tokens=150
    )

    return response['choices'][0]['text']

# Example usage:
rm_profiles = [
    {'id': '6795a94d-327b-4430-bb15-8f7192366be5', 'years_of_experience': 5, 'skills': ['Sales pitch', 'Marketing', 'Customer Service'], 'locality': 'Mumbai', 'client_feedback_score': 4.7, 'language': ['Hindi', 'English']},
    {'id': 'f8cd1102-a3cb-400d-93fd-c59233f507be', 'years_of_experience': 8, 'skills': ['Negotiation', 'Market Analysis', 'Follow-ups'], 'locality': 'Pune', 'client_feedback_score': 4.5, 'language': ['English', 'Marathi']},
    # Add more RM profiles here
]

property_data = {'price_band': '₹50L - ₹1Cr', 'location': 'Mumbai', 'possession_timeline': 'Ready-to-move', 'property_type': 'Apartment', 'builder_credibility': 'Tier 1'}

# Call the function to match RM with property
matched_rms = match_rm_with_property(rm_profiles, property_data)
print(matched_rms)
