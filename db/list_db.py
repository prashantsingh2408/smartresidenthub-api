from supabase import create_client, Client
import json
from pprint import pprint

SUPABASE_URL = "https://thwdxicmulviwctkbhek.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgyNDExNjMsImV4cCI6MjA1MzgxNzE2M30.kviglZ2Awdn6aEfei93g49wIvDoyZhhvWZT5-d0do9g"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

print("\n=== RM Profiles ===")
response = supabase.table('rm_profiles').select('*').execute()
pprint(response.data)

print("\n=== Selling Factors ===")
response = supabase.table('selling_factors').select('*').execute()
pprint(response.data)

# print("\n=== Leads ===")
# response = supabase.table('leads_table').select('*').execute()
# pprint(response.data)

# site_visits
print("\n=== Site Visits ===")
response = supabase.table('site_visits').select('*').execute()
pprint(response.data)
