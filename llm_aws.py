import json
import boto3
from botocore.exceptions import ClientError
import os

def check_aws_credentials():
    """Check if AWS credentials are set and valid."""
    try:
        aws_access_key_id = 'AKIAVUXUHEW2C7DSA3FR'
        aws_secret_access_key = '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'

      
        # aws_access_key_id = 'AKIAVUXUHEW2LB4MNP5H'
        # aws_secret_access_key = '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'

        os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
        os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

        # Attempt to create a session with the provided credentials
        session = boto3.Session()
        credentials = session.get_credentials()
 
        if credentials is None or not credentials.get_frozen_credentials():
            print("AWS credentials are not set or invalid.")
            return False
 
        # Check if the credentials are valid by making a simple AWS call
        sts_client = boto3.client('sts')
        sts_client.get_caller_identity()  # This will raise an error if credentials are invalid
        print("AWS credentials are valid.")
        return True
    except Exception as e:
        print(f"Error checking AWS credentials: {e}")
        return False


def invoke_claude():
    # Create AWS Bedrock runtime client
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    # Define the request payload
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "top_k": 250,
        "stop_sequences": [],
        "temperature": 1,
        "top_p": 0.999,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "hello world"
                    }
                ]
            }
        ]
    }

    # Invoke the model using the inference profile
    response = client.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20241022-v2:0",
        body=json.dumps(payload),
        accept="application/json",
        contentType="application/json"
    )

    # Parse and print the response
    response_body = json.loads(response["body"].read())
    print("Response:", response_body)

check_aws_credentials()

# Invoke the function
invoke_claude()

