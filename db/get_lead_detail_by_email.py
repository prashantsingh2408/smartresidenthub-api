from db.supabase_config import get_supabase_client, fetch_data

# Initialize the Supabase client
supabase = get_supabase_client()

def get_lead_detail(lead_id=None, email=None):
    """Fetch lead details by ID or email from the Supabase database."""
    filters = {}
    
    if lead_id:
        filters['id'] = lead_id
    elif email:
        filters['email'] = email
    else:
        raise ValueError("Either lead_id or email must be provided.")

    lead_data = fetch_data('lead', filters)
    return lead_data

# Example usage
if __name__ == "__main__":
    lead_id_to_fetch = None  # Replace with the desired lead ID or set to None
    email_to_fetch = "prashant.singh1@anarock.com"  # Replace with the desired email

    lead_details = get_lead_detail(lead_id=lead_id_to_fetch, email=email_to_fetch)
    print("Lead Details:", lead_details)
