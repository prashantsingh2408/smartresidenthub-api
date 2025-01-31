from supabase import create_client, Client

# Define your Supabase URL and Key
SUPABASE_URL = "https://thwdxicmulviwctkbhek.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgyNDExNjMsImV4cCI6MjA1MzgxNzE2M30.kviglZ2Awdn6aEfei93g49wIvDoyZhhvWZT5-d0do9g"

# Initialize the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

# Example usage: Fetch data from the lead table
response = supabase.table('lead').select('*').execute()

# Print the result (list of profiles)
print(response.data)

# Delete all existing data in the 'lead' table
delete_profiles_response = supabase.table('lead').delete().execute()
print("Deleted old lead data:", delete_profiles_response.data)

profiles = [
    {
        "rm_id": 1,
        "name": "Amit Sharma",
        "years_of_experience": 5,
        "client_feedback_score": 4.7,
        "top_3_feedback_keywords": "excellent service, quick response, professional",
        "client_requests_for_same_rm": 12,
        "response_time": 2,
        "skills": "Sales pitch, Marketing, Customer Service",
        "avg_sale_ticket_size": 50,
        "language": "Hindi, English",
        "locality": "Mumbai",
        "properties_managed": 20,
        "availability": "Full-time"
    },
    {
        "rm_id": 2,
        "name": "Rohit Mehta",
        "years_of_experience": 8,
        "client_feedback_score": 4.5,
        "top_3_feedback_keywords": "great negotiator, responsive, problem solver",
        "client_requests_for_same_rm": 20,
        "response_time": 1.5,
        "skills": "Negotiation, Market Analysis, Follow-ups",
        "avg_sale_ticket_size": 75,
        "language": "English, Marathi",
        "locality": "Pune",
        "properties_managed": 25,
        "availability": "Full-time"
    },
    {
        "rm_id": 3,
        "name": "Priya Gupta",
        "years_of_experience": 3,
        "client_feedback_score": 4.3,
        "top_3_feedback_keywords": "friendly, knowledgeable, approachable",
        "client_requests_for_same_rm": 8,
        "response_time": 3,
        "skills": "Lead nurturing, Closing deals, CRM",
        "avg_sale_ticket_size": 40,
        "language": "Hindi, Tamil", 
        "locality": "Bangalore",
        "properties_managed": 15,
        "availability": "Part-time"
    },
    {
        "rm_id": 4,
        "name": "Neha Verma",
        "years_of_experience": 6,
        "client_feedback_score": 4.8,
        "top_3_feedback_keywords": "trustworthy, proactive, great communication",
        "client_requests_for_same_rm": 15,
        "response_time": 1,
        "skills": "Customer engagement, Follow-ups, Relationship Building",
        "avg_sale_ticket_size": 60,
        "language": "English, Hindi",
        "locality": "Delhi", 
        "properties_managed": 22,
        "availability": "Full-time"
    },
    {
        "rm_id": 5,
        "name": "Suresh Reddy",
        "years_of_experience": 7,
        "client_feedback_score": 4.6,
        "top_3_feedback_keywords": "experienced, reliable, efficient",
        "client_requests_for_same_rm": 18,
        "response_time": 2.5,
        "skills": "Real estate advisory, Business Development, Communication",
        "avg_sale_ticket_size": 80,
        "language": "Telugu, English",
        "locality": "Hyderabad",
        "properties_managed": 18,
        "availability": "Full-time"
    }
]

insert_response = supabase.table('lead').insert(profiles).execute()
# Print the inserted record's response

