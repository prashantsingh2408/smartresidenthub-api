from fastapi import FastAPI
import os
from dotenv import load_dotenv
from datetime import date
from llm_groq import connect_with_groq_api_mixtral  # Import the function

# Load environment variables
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Database connection settings
DATABASE_URL = os.getenv('DATABASE_URL')

# Add this after loading environment variables
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Root endpoint to return a greeting message
@app.get("/")
async def root():
    return {"status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/analyze")
async def analyze_lead():
    """Endpoint to analyze lead using Groq API."""
    response = connect_with_groq_api_mixtral()
    return response  # Return the response from the Groq API