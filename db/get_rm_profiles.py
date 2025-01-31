from db.supabase_config import get_supabase_client, fetch_data

def get_rm_profiles():
    """Fetch all RM profiles from the database."""
    return fetch_data('rm_profiles')  # Assuming fetch_data is implemented to get data from the 'rm_profiles' table 