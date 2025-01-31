import boto3
import json
import os

aws_access_key_id = 'AKIAVUXUHEW2C7DSA3FR'
aws_secret_access_key = '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'

      
# aws_access_key_id = 'AKIAVUXUHEW2LB4MNP5H'
# aws_secret_access_key = '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'

os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key


# Create AWS Bedrock runtime client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Correctly formatted Claude prompt
prompt = """\n\nHuman: Explain quantum computing in simple terms.\n\nAssistant:"""

# Define the request payload
payload = {
    "prompt": prompt,
    "max_tokens_to_sample": 200
}

# Invoke the model using the inference profile
response = client.invoke_model(
    modelId="anthropic.claude-v2",
    body=json.dumps(payload),
    accept="application/json",
    contentType="application/json"
)

# Parse and print the response
response_body = json.loads(response["body"].read())
print("Response:", response_body)