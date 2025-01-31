from fastapi import FastAPI
import os
from dotenv import load_dotenv
from datetime import date

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