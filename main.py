from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from datetime import date
from llm_groq import connect_with_groq_api_mixtral, match_rm_to_lead  # Import the function and match_rm_to_lead

# Load environment variables
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Set a timeout for the FastAPI application
@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Timeout"] = "180"  # Set timeout in seconds
    return response

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

@app.get("/analyze/")
async def analyze_lead(lead_id: str = None, email: str = None):
    """Endpoint to analyze lead using Groq API."""
    if not lead_id and not email:
        return {"error": "Either lead_id or email must be provided."}
    
    response = await connect_with_groq_api_mixtral(lead_id=lead_id, email=email)  # Pass both parameters
    return response  # Return the response from the Groq API

@app.get("/match_rm/{lead_id}")
async def match_rm(lead_id: str):
    """Endpoint to match RM profiles to a lead."""
    response = await match_rm_to_lead(lead_id)
    return response