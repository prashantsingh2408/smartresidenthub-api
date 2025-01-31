from supabase import create_client, Client
import os

SUPABASE_URL = "https://thwdxicmulviwctkbhek.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgyNDExNjMsImV4cCI6MjA1MzgxNzE2M30.kviglZ2Awdn6aEfei93g49wIvDoyZhhvWZT5-d0do9g"
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczODI0MTE2MywiZXhwIjoyMDUzODE3MTYzfQ.owlJOmGx29AvqpRiMyHoxmVwdd91Du0G0iHxOR-pQD0"
#
# Initialize the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def get_supabase_client() -> Client:
    """Return the Supabase client."""
    return supabase

def insert_data(table_name, data):
    """Insert data into a specified table."""
    response = supabase.table(table_name).insert(data).execute()
    return response.data

def fetch_data(table_name, filters=None):
    """Fetch data from a specified table with optional filters."""
    query = supabase.table(table_name).select('*')
    if filters:
        for key, value in filters.items():
            query = query.eq(key, value)
    response = query.execute()
    return response.data

def delete_data(table_name, filters):
    """Delete data from a specified table based on filters."""
    response = supabase.table(table_name).delete()
    for key, value in filters.items():
        response = response.eq(key, value)
    return response.execute() 