from supabase_config import get_supabase_client, fetch_data
from pprint import pprint

# Initialize the Supabase client
supabase = get_supabase_client()

print("\n=== Lead ===")
response = fetch_data('lead')
pprint(response)

# Uncomment to fetch other tables
# print("\n=== RM Profiles ===")
# response = fetch_data('rm_profiles')
# pprint(response)

# print("\n=== Selling Factors ===")
# response = fetch_data('selling_factors')
# pprint(response)

# print("\n=== Site Visits ===")
# response = fetch_data('site_visits')
# pprint(response)
