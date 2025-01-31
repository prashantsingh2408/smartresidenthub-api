from supabase_config import get_supabase_client, fetch_data, delete_data

# Initialize the Supabase client
supabase = get_supabase_client()

# Example usage: Fetch data from the lead table
response = fetch_data('lead')

# Print the result (list of profiles)
print("Existing lead data:", response)

# Specify the row ID to delete
row_id_to_delete = "46c9d755-e079-4a0a-81fa-6ffbd8fa4c5c"

# Use the helper function to delete the record
deleted_record = delete_data('lead', {'id': row_id_to_delete})

print("Deleted record:", deleted_record)

# Fetch updated data to confirm deletion
updated_response = fetch_data('lead')

# Print the result (list of profiles)
print("Updated lead data:", updated_response)