from db.supabase_config import get_supabase_client, fetch_data

# Initialize the Supabase client
supabase = get_supabase_client()

def get_lead_detail_by_id(lead_id):
    """Fetch lead details by ID from the Supabase database."""
    filters = {'id': lead_id}
    lead_data = fetch_data('lead', filters)
    return lead_data

# Example usage
if __name__ == "__main__":
    lead_id_to_fetch = "46c9d755-e079-4a0a-81fa-6ffbd8fa4c5c"  # Replace with the desired lead ID
    lead_details = get_lead_detail_by_id(lead_id_to_fetch)
    print("Lead Details:", lead_details)
