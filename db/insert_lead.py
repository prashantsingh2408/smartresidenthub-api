from supabase import create_client, Client

# Define your Supabase URL and Key
SUPABASE_URL = "https://thwdxicmulviwctkbhek.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzgyNDExNjMsImV4cCI6MjA1MzgxNzE2M30.kviglZ2Awdn6aEfei93g49wIvDoyZhhvWZT5-d0do9g"
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRod2R4aWNtdWx2aXdjdGtiaGVrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczODI0MTE2MywiZXhwIjoyMDUzODE3MTYzfQ.owlJOmGx29AvqpRiMyHoxmVwdd91Du0G0iHxOR-pQD0"
# Initialize the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

profiles = [
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "prashant.singh1@anarock.com",
        "id": "1e88b663-d6a1-32c9-bd02-665fb39b80b1",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed strong interest in the property.",
                "agent": "Agent A",
                "status_update": "Lead is very interested.",
                "sentiment": "Positive"
            },
            {
                "interaction_id": "I001",
                "date": "2025-01-31",
                "type": "Initial Inquiry",
                "notes": "Lead inquired about 2-bedroom apartments.",
                "agent": "Agent A",
                "status_update": "Lead acknowledged and added to the system.",
                "sentiment": "Positive"
            },
            {
                "interaction_id": "I002",
                "date": "2025-02-01",
                "type": "Email Follow-up",
                "notes": "Sent additional property options via email.",
                "agent": "Agent A",
                "status_update": "Awaiting response from the lead.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Prashant Singh",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "surendra.lamrod@anarock.com",
        "id": "2e88b663-d6a1-32c9-bd02-665fb39b80b2",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead showed moderate interest.",
                "agent": "Agent B",
                "status_update": "Lead is considering options.",
                "sentiment": "Neutral"
            },
            {
                "interaction_id": "I003",
                "date": "2025-01-31",
                "type": "Follow-up Call",
                "notes": "Discussed property options.",
                "agent": "Agent B",
                "status_update": "Lead is still evaluating.",
                "sentiment": "Neutral"
            },
            {
                "interaction_id": "I004",
                "date": "2025-02-02",
                "type": "Text Message",
                "notes": "Sent a text reminder about the property visit.",
                "agent": "Agent B",
                "status_update": "Awaiting confirmation for the visit.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Surendra Lamrod",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "chandra.mohan@anarock.com",
        "id": "3e88b663-d6a1-32c9-bd02-665fb39b80b3",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed dissatisfaction with the options.",
                "agent": "Agent C",
                "status_update": "Lead is not interested.",
                "sentiment": "Negative"
            },
            {
                "interaction_id": "I005",
                "date": "2025-01-31",
                "type": "Follow-up Call",
                "notes": "Discussed concerns about pricing.",
                "agent": "Agent C",
                "status_update": "Lead is unhappy with the pricing.",
                "sentiment": "Negative"
            },
            {
                "interaction_id": "I006",
                "date": "2025-02-01",
                "type": "Email Follow-up",
                "notes": "Sent an email with alternative options.",
                "agent": "Agent C",
                "status_update": "Awaiting response from the lead.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Chandra Mohan",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "chirag.mewara@anarock.com",
        "id": "4e88b663-d6a1-32c9-bd02-665fb39b80b4",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed interest in the property.",
                "agent": "Agent D",
                "status_update": "Lead is considering options.",
                "sentiment": "Neutral"
            },
            {
                "interaction_id": "I007",
                "date": "2025-01-31",
                "type": "Follow-up Call",
                "notes": "Discussed property options.",
                "agent": "Agent D",
                "status_update": "Lead is still evaluating.",
                "sentiment": "Neutral"
            },
            {
                "interaction_id": "I008",
                "date": "2025-02-01",
                "type": "Text Message",
                "notes": "Sent a text reminder about the property visit.",
                "agent": "Agent D",
                "status_update": "Awaiting confirmation for the visit.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Chirag Mewara",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "vinayak.kumar@anarock.com",
        "id": "5e88b663-d6a1-32c9-bd02-665fb39b80b5",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed dissatisfaction with the options.",
                "agent": "Agent E",
                "status_update": "Lead is not interested.",
                "sentiment": "Negative"
            },
            {
                "interaction_id": "I009",
                "date": "2025-01-31",
                "type": "Follow-up Call",
                "notes": "Discussed concerns about pricing.",
                "agent": "Agent E",
                "status_update": "Lead is unhappy with the pricing.",
                "sentiment": "Negative"
            },
            {
                "interaction_id": "I010",
                "date": "2025-02-01",
                "type": "Text Message",
                "notes": "Sent a text reminder about the property visit.",
                "agent": "Agent E",
                "status_update": "Awaiting confirmation for the visit.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Vinayak Kumar",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "saurabh.maun@anarock.com",
        "id": "6e88b663-d6a1-32c9-bd02-665fb39b80b6",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed strong interest in the property.",
                "agent": "Agent F",
                "status_update": "Lead is very interested.",
                "sentiment": "Positive"
            },
            {
                "interaction_id": "I011",
                "date": "2025-01-31",
                "type": "Initial Inquiry",
                "notes": "Lead inquired about 2-bedroom apartments.",
                "agent": "Agent F",
                "status_update": "Lead acknowledged and added to the system.",
                "sentiment": "Positive"
            },
            {
                "interaction_id": "I012",
                "date": "2025-02-01",
                "type": "Text Message",
                "notes": "Sent a text reminder about the property visit.",
                "agent": "Agent F",
                "status_update": "Awaiting confirmation for the visit.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Saurabh Maun",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "raman.manogaran@anarock.com",
        "id": "7e88b663-d6a1-32c9-bd02-665fb39b80b7",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed dissatisfaction with the options.",
                "agent": "Agent G",
                "status_update": "Lead is not interested.",
                "sentiment": "Negative"
            },
            {
                "interaction_id": "I013",
                "date": "2025-01-31",
                "type": "Follow-up Call",
                "notes": "Discussed concerns about pricing.",
                "agent": "Agent G",
                "status_update": "Lead is unhappy with the pricing.",
                "sentiment": "Negative"
            },
            {
                "interaction_id": "I014",
                "date": "2025-02-01",
                "type": "Email Follow-up",
                "notes": "Sent an email with alternative options.",
                "agent": "Agent G",
                "status_update": "Awaiting response from the lead.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Raman Manogaran",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    },
    {
        "additional_preferences": "Prefers properties with gym and parking",
        "amenities": ["Gym", "Parking", "Pool"], 
        "assigned_rm_id": None,  
        "conversion_probability": 0.75,
        "created_at": "2025-01-30T15:00:00+00:00",
        "email": "dharmalingam.p@anarock.com",
        "id": "8e88b663-d6a1-32c9-bd02-665fb39b80b8",
        "industry": "Retail",
        "interaction_history": [
            {
                "action": "Follow-up Call",
                "date": "2025-01-30",
                "notes": "Lead expressed strong interest in the property.",
                "agent": "Agent H",
                "status_update": "Lead is very interested.",
                "sentiment": "Positive"
            },
            {
                "interaction_id": "I015",
                "date": "2025-01-31",
                "type": "Initial Inquiry",
                "notes": "Lead inquired about 2-bedroom apartments.",
                "agent": "Agent H",
                "status_update": "Lead acknowledged and added to the system.",
                "sentiment": "Positive"
            },
            {
                "interaction_id": "I016",
                "date": "2025-02-01",
                "type": "Text Message",
                "notes": "Sent a text reminder about the property visit.",
                "agent": "Agent H",
                "status_update": "Awaiting confirmation for the visit.",
                "sentiment": "Neutral"
            }
        ],
        "last_contact_date": "2025-01-30T12:00:00+00:00",
        "last_visit_date": "2025-02-07T10:00:00+00:00",
        "location": "Los Angeles",
        "max_budget": 5000,
        "min_budget": 3000,
        "name": "Dharmalingam P",
        "phone": "+1234567891",
        "preferences": {
            "industry": "Retail",
            "location": "Los Angeles",
            "property_type": "Apartment",
            "amenities": ["Gym", "Parking"]
        },
        "property_type": "Apartment",
        "rm_assigned_at": "2025-01-30T15:30:00+00:00",
        "sentiment": "moderate",
        "source": "Referral",
        "status": "Contacted",
        "updated_at": "2025-01-31T12:34:36.18852+00:00",
        "visit_scheduled": True
    }
]

insert_response = supabase.table('lead').insert(profiles).execute()
# Print the inserted record's response
print(insert_response)

