from supabase import create_client, Client

# Define your Supabase URL and Key
SUPABASE_URL = "https://thwdxicmulviwctkbhek.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgyNDExNjMsImV4cCI6MjA1MzgxNzE2M30.kviglZ2Awdn6aEfei93g49wIvDoyZhhvWZT5-d0do9g"

# Initialize the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

# selling_factors
selling_factors = [
    {
        "selling_factor_id": 1,
        "price_band": "₹50L - ₹1Cr",
        "location": "Mumbai", 
        "possession_timeline": "Ready-to-move",
        "property_type": "Apartment",
        "builder_credibility": "Tier 1",
        "loan_payment_plan_options": "EMI"
    },
    {
        "selling_factor_id": 2, 
        "price_band": "₹1Cr - ₹2Cr",
        "location": "Bangalore",
        "possession_timeline": "6 months", 
        "property_type": "Villa",
        "builder_credibility": "Tier 2",
        "loan_payment_plan_options": "Full Payment"
    },
    {
        "selling_factor_id": 3,
        "price_band": "₹2Cr+",
        "location": "Pune",
        "possession_timeline": "1 year",
        "property_type": "Studio", 
        "builder_credibility": "Tier 3",
        "loan_payment_plan_options": "Rental Yields"
    }
]


delete_factors_response = supabase.table('selling_factors').delete().execute()
print("Deleted old selling_factors data:", delete_factors_response.data)

insert_factors = supabase.table('selling_factors').insert(selling_factors).execute()
print(insert_factors.data)