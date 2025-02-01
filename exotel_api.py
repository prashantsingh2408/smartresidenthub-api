import requests  # Use requests for synchronous requests
import os
from dotenv import load_dotenv
from fastapi import HTTPException  # Ensure this import is present

# Load environment variables
load_dotenv()

# Exotel Credentials
EXOTEL_SID = os.getenv("EXOTEL_SID")
EXOTEL_API_KEY = os.getenv("EXOTEL_API_KEY")
EXOTEL_API_TOKEN = os.getenv("EXOTEL_API_TOKEN")
EXOTEL_VIRTUAL_NUMBER = os.getenv("EXOTEL_VIRTUAL_NUMBER")
EXOTEL_BASE_URL = f"https://api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect"

def make_call(customer_number: str, agent_number: str):
    """
    API to make a call between a customer and an agent using Exotel.
    :param customer_number: The customer's phone number.
    :param agent_number: The agent's phone number.
    :return: Response from Exotel API.
    """
    if not all([EXOTEL_SID, EXOTEL_API_KEY, EXOTEL_API_TOKEN, EXOTEL_VIRTUAL_NUMBER]):
        raise HTTPException(status_code=500, detail="Exotel credentials are not set properly.")

    payload = {
        "From": customer_number,  # Customer's phone number
        "To": agent_number,  # Agent's phone number
        "CallerId": EXOTEL_VIRTUAL_NUMBER,  # Exotel Virtual Number (masking)
        "CallType": "trans"  # Transactional call
    }

    response = requests.post(
        EXOTEL_BASE_URL,
        data=payload,
        auth=(EXOTEL_API_KEY, EXOTEL_API_TOKEN),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=10  # Timeout in seconds
    )

    # Debugging: Print the response status and text
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    print(f"Response Headers: {response.headers}")
    if response.status_code == 200:
        # Check if response is XML (Exotel returns XML response)
        if 'xml' in response.headers.get('Content-Type', '').lower():
            return {
                "status": "success",
                "response": {
                    "call_sid": response.text.split("<Sid>")[1].split("</Sid>")[0],
                    "status": response.text.split("<Status>")[1].split("</Status>")[0],
                    "raw_response": response.text
                }
            }
        try:
            return {"status": "success", "response": response.json()}
        except ValueError:
            return {"status": "error", "message": "Invalid response format from Exotel"}
    else:
        return {"status": "error", "message": f"Error: {response.status_code} - {response.text}"}

   


make_call("8417891491", "9786095546")  # Corrected the function call