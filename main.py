from fastapi import FastAPI, Request, HTTPException
import os
from dotenv import load_dotenv
from datetime import date
from llm_groq import connect_with_groq_api_mixtral, match_rm_to_lead, chat_with_lead_and_rm  # Import the function and match_rm_to_lead
from exotel_api import make_call  # Add this import at the top

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
async def analyze_lead(lead_id: str = None, email: str = None, phone: str = None):
    """Endpoint to analyze lead using Groq API."""
    if not any([lead_id, email, phone]):
        return {"error": "Either lead_id, email or phone must be provided."}
    
    response = await connect_with_groq_api_mixtral(lead_id=lead_id, email=email, phone=phone)
    return response

@app.get("/match_rm/{lead_id}")
async def match_rm(lead_id: str):
    """Endpoint to match RM profiles to a lead."""
    response = await match_rm_to_lead(lead_id)
    return response

@app.post("/chat/{lead_id}")
async def chat_with_lead(lead_id: str, user_message: str):
    """Endpoint to chat with the lead and RM profiles."""
    response = await chat_with_lead_and_rm(lead_id, user_message)
    return response

# New endpoint to make a call directly
@app.get("/make-call/{lead_phone}/{rm_phone}")
async def make_call_endpoint(lead_phone: str, rm_phone: str):
    """Endpoint to make a call between a lead and an RM."""
    if not lead_phone or not rm_phone:
        raise HTTPException(status_code=400, detail="lead_phone and rm_phone are required.")
    
    response = make_call(lead_phone, rm_phone)  # No await since make_call is now synchronous
    return response
