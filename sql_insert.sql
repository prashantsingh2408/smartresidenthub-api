INSERT INTO lead (
    id, assigned_rm_id, budget, conversion_probability, created_at, email, 
    interaction_history, last_contact_date, name, phone, preferences, sentiment, 
    source, status, updated_at
) VALUES 
(
    'b42878d2-dba4-4c3c-93f7-0756be06f24d', '7d47c093-b00a-4f0c-bbf9-4023e678ff89', 
    50000, 0.85, '2025-01-31T00:00:00+00:00', 'john.doe@example.com',
    '[{"action": "Initial Contact", "date": "2025-01-29"}]'::jsonb,
    '2025-01-30T14:00:00+00:00', 'John Doe', '+1234567890', 
    '{"industry": "Finance", "location": "New York"}'::jsonb, 
    'Positive', 'Website', 'New', '2025-01-31T00:00:00+00:00'
),
(
    '46c9d755-e079-4a0a-81fa-6ffbd8fa4c5b', 'f917f9c9-53a6-41d4-9379-abb1e6354b39', 
    35000, 0.75, '2025-01-30T15:00:00+00:00', 'jane.smith@example.com',
    '[{"action": "Follow-up Call", "date": "2025-01-30"}]'::jsonb,
    '2025-01-30T12:00:00+00:00', 'Jane Smith', '+1234567891', 
    '{"industry": "Retail", "location": "Los Angeles"}'::jsonb, 
    'Neutral', 'Referral', 'Contacted', '2025-01-30T15:00:00+00:00'
),

(
    '1a2b3c4d-1234-5678-9101-112131415161', '7d47c093-b00a-4f0c-bbf9-4023e678ff89', 
    75000, 0.92, '2025-01-29T10:00:00+00:00', 'alice.brown@example.com',
    '[{"action": "Inquiry", "date": "2025-01-28"}]'::jsonb,
    '2025-01-28T16:30:00+00:00', 'Alice Brown', '+1987654321', 
    '{"industry": "Tech", "location": "San Francisco"}'::jsonb, 
    'Highly Interested', 'Social Media', 'Qualified', '2025-01-29T10:00:00+00:00'
),
(
    '2b3c4d5e-2234-5678-9101-112131415162', 'f917f9c9-53a6-41d4-9379-abb1e6354b39', 
    60000, 0.81, '2025-01-28T12:00:00+00:00', 'charlie.white@example.com',
    '[{"action": "Site Visit", "date": "2025-01-27"}]'::jsonb,
    '2025-01-27T18:00:00+00:00', 'Charlie White', '+1555444333', 
    '{"industry": "Healthcare", "location": "Chicago"}'::jsonb, 
    'Interested', 'Advertisement', 'Negotiation', '2025-01-28T12:00:00+00:00'
),
(
    '3c4d5e6f-3234-5678-9101-112131415163', '7d47c093-b00a-4f0c-bbf9-4023e678ff89', 
    45000, 0.68, '2025-01-26T09:00:00+00:00', 'daniel.green@example.com',
    '[{"action": "Email Inquiry", "date": "2025-01-25"}]'::jsonb,
    '2025-01-25T11:00:00+00:00', 'Daniel Green', '+1666777888', 
    '{"industry": "Education", "location": "Austin"}'::jsonb, 
    'Moderate', 'Website', 'Evaluating', '2025-01-26T09:00:00+00:00'
),
(
    '4d5e6f7g-4234-5678-9101-112131415164', 'f917f9c9-53a6-41d4-9379-abb1e6354b39', 
    90000, 0.95, '2025-01-27T14:30:00+00:00', 'emily.jones@example.com',
    '[{"action": "Phone Inquiry", "date": "2025-01-26"}]'::jsonb,
    '2025-01-26T17:45:00+00:00', 'Emily Jones', '+1777888999', 
    '{"industry": "Real Estate", "location": "New York"}'::jsonb, 
    'Highly Interested', 'Referral', 'Finalizing', '2025-01-27T14:30:00+00:00'
),
(
    '5e6f7g8h-5234-5678-9101-112131415165', '7d47c093-b00a-4f0c-bbf9-4023e678ff89', 
    70000, 0.87, '2025-01-25T11:20:00+00:00', 'frank.thomas@example.com',
    '[{"action": "Social Media DM", "date": "2025-01-24"}]'::jsonb,
    '2025-01-24T13:30:00+00:00', 'Frank Thomas', '+1888999000', 
    '{"industry": "Entertainment", "location": "Las Vegas"}'::jsonb, 
    'Interested', 'Social Media', 'Follow-up Needed', '2025-01-25T11:20:00+00:00'
),
(
    '6f7g8h9i-6234-5678-9101-112131415166', 'f917f9c9-53a6-41d4-9379-abb1e6354b39', 
    55000, 0.73, '2025-01-24T16:10:00+00:00', 'grace.miller@example.com',
    '[{"action": "Cold Call", "date": "2025-01-23"}]'::jsonb,
    '2025-01-23T19:15:00+00:00', 'Grace Miller', '+1999000111', 
    '{"industry": "Hospitality", "location": "Miami"}'::jsonb, 
    'Neutral', 'Advertisement', 'Considering', '2025-01-24T16:10:00+00:00'
),
(
    '7g8h9i0j-7234-5678-9101-112131415167', '7d47c093-b00a-4f0c-bbf9-4023e678ff89', 
    62000, 0.78, '2025-01-23T08:45:00+00:00', 'henry.adams@example.com',
    '[{"action": "Live Chat", "date": "2025-01-22"}]'::jsonb,
    '2025-01-22T10:30:00+00:00', 'Henry Adams', '+1222333444', 
    '{"industry": "Automotive", "location": "Detroit"}'::jsonb, 
    'Moderate', 'Live Chat', 'Waiting for Response', '2025-01-23T08:45:00+00:00'
),
(
    '8h9i0j1k-8234-5678-9101-112131415168', 'f917f9c9-53a6-41d4-9379-abb1e6354b39', 
    30000, 0.60, '2025-01-22T12:30:00+00:00', 'isabella.wilson@example.com',
    '[{"action": "Site Visit Scheduled", "date": "2025-01-21"}]'::jsonb,
    '2025-01-21T15:00:00+00:00', 'Isabella Wilson', '+1444555666', 
    '{"industry": "Fashion", "location": "New York"}'::jsonb, 
    'Neutral', 'Website', 'Scheduling Visit', '2025-01-22T12:30:00+00:00'
);


