from supabase import create_client, Client

SUPABASE_URL = "https://thwdxicmulviwctkbhek.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgyNDExNjMsImV4cCI6MjA1MzgxNzE2M30.kviglZ2Awdn6aEfei93g49wIvDoyZhhvWZT5-d0do9g"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

response = supabase.table('rm_profiles').select('*').execute()
print(response)

# response = supabase.table('selling_factors').select('*').execute()
# print(response)


# response = supabase.table('leads').select('*').execute()
# print(response)


# show all tables
# response = supabase.table('information_schema.tables').select('table_name').eq('table_schema', 'public').execute()
# print(response)


