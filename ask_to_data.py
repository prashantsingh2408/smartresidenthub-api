from db.get_lead_detail_by_id import get_lead_detail_by_id
from db.get_rm_profiles import get_rm_profiles
import asyncio
from groq import Groq

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
            result = result[start_idx:end_idx]
    except Exception as e:
        print(f"An error occurred while extracting JSON: {e}")

    return result  # Return the complete response

async def aks_to_data(user_message):
    """Chat with RM profiles based on the user message."""
    # Fetch RM profiles
    rm_profiles = get_rm_profiles()

    # Prepare the prompt for Groq API
    prompt = f"RM Profiles: {rm_profiles}\nUser Message: {user_message}\nRespond appropriately."

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
            result = result[start_idx:end_idx]
    except Exception as e:
        print(f"An error occurred while extracting JSON: {e}")

    return result  # Return the complete response
