from db.supabase_config import get_supabase_client, fetch_data

# Initialize the Supabase client
supabase = get_supabase_client()

def get_lead_detail_by_phone(phone=None):
    """Fetch lead details by phone from the Supabase database."""
    if not phone:
        raise ValueError("Phone number must be provided.")
    
    filters = {'phone': phone}
    lead_data = fetch_data('lead', filters)
    return lead_data

# Example usage
if __name__ == "__main__":
    phone_to_fetch = "1234567890"  # Replace with the desired phone number
    lead_details = get_lead_detail_by_phone(phone=phone_to_fetch)
    print("Lead Details:", lead_details) 