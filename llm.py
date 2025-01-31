import logging
import json
import boto3
from botocore.exceptions import ClientError
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_temporary_aws_credentials():
    """Retrieve temporary AWS credentials using STS."""
    session = boto3.Session()
    client = session.client("sts")
    response = client.get_session_token()

    credentials = response["Credentials"]
    aws_access_key = credentials["AccessKeyId"]
    aws_secret_key = credentials["SecretAccessKey"]
    aws_session_token = credentials["SessionToken"]

    print("Access Key:", aws_access_key)
    print("Secret Key:", aws_secret_key)
    print("Session Token:", aws_session_token)

    # Set the environment variables for the credentials
    os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key
    os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_key
    os.environ['AWS_SESSION_TOKEN'] = aws_session_token

# Call the function to get temporary AWS credentials
get_temporary_aws_credentials()
# os.environ['AWS_ACCESS_KEY_ID'] = "AKIAVUXUHEW2LB4MNP5H"
# os.environ['AWS_SECRET_ACCESS_KEY'] = "AKIAVUXUHEW2LB4MNP5H"
# os.environ['AWS_SESSION_TOKEN'] = "dshk107N6/IkMdH1wWBIei3S9BQkvUkVk4Rsa6uI"

boto3.setup_default_session(region_name='us-east-1')

brt = boto3.client(service_name='bedrock-runtime')

def invoke_claude(bedrock_runtime_client, messages):
    try:
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 200,
            "top_k": 250,
            "stopSequences": [],
            "temperature": 1,
            "top_p": 0.999,
            "messages": messages  # Use the messages passed to the function
        }

        model_id = 'anthropic.claude-3-5-haiku-20241022-v1:0'
        response = bedrock_runtime_client.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json", 
            body=json.dumps(body)
        )

        response_body = json.loads(response["body"].read())
        completion = response_body["content"][0]["text"]

        return completion

    except ClientError:
        print("Couldn't invoke Claude")
        raise

def check_aws_credentials():
    """Check if AWS credentials are set and valid."""
    try:
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

# Call the function to check credentials
if check_aws_credentials():
    print('AWS credentials are valid.')
    
    # Define a message to send to the Claude model
    message = [
        {
            "type": "text",
            "text": "Explain Pythagorean Theorem"
        }
    ]
    
    result = invoke_claude(brt, message)
    print(result)

