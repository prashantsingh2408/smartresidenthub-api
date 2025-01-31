CREATE TABLE leads_table (
    id UUID PRIMARY KEY,
    assigned_rm_id UUID NULL,
    budget NUMERIC NULL,
    conversion_probability NUMERIC NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    email VARCHAR(255) NULL,
    interaction_history JSONB[] NULL,
    last_contact_date TIMESTAMP NULL,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NULL,
    preferences JSONB NULL,
    sentiment VARCHAR(50) NULL,
    source VARCHAR(255) NULL,
    status VARCHAR(50) NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE site_visits (
    id UUID PRIMARY KEY,
    lead_id UUID NULL,
    rm_id UUID NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    feedback TEXT NULL,
    scheduled_at TIMESTAMP NOT NULL,
    status VARCHAR(50) NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_lead FOREIGN KEY (lead_id) REFERENCES leads_table(id) ON DELETE SET NULL,
    CONSTRAINT fk_rm FOREIGN KEY (rm_id) REFERENCES rm_profiles(id) ON DELETE SET NULL
);



CREATE TABLE rm_profiles (
    rm_id INT PRIMARY KEY,
    name VARCHAR(100),
    years_of_experience INT,
    client_feedback_score DECIMAL(3, 2),
    top_3_feedback_keywords TEXT,
    client_requests_for_same_rm INT,
    response_time DECIMAL(3, 2),
    skills TEXT,
    avg_sale_ticket_size DECIMAL(10, 2),
    language VARCHAR(255),
    locality VARCHAR(100),
    properties_managed INT,
    availability VARCHAR(20)
);
CREATE TABLE selling_factors (
    selling_factor_id INT PRIMARY KEY,
    price_band VARCHAR(20),
    location VARCHAR(50),
    possession_timeline VARCHAR(50),
    property_type VARCHAR(50),
    builder_credibility VARCHAR(50),
    loan_payment_plan_options VARCHAR(50)
);
 


--
INSERT INTO leads_table (
    id, 
    assigned_rm_id, 
    budget, 
    conversion_probability, 
    created_at, 
    email, 
    interaction_history, 
    last_contact_date, 
    name, 
    phone, 
    preferences, 
    sentiment, 
    source, 
    status, 
    updated_at
) VALUES
(
    '11111111-aaaa-1111-aaaa-111111111111', 
    '6795a94d-327b-4430-bb15-8f7192366be5', 
    5000000, 
    0.8, 
    '2025-01-30T20:30:00+00:00', 
    'lead1@example.com', 
    '[{"interaction":"call","outcome":"interested"},{"interaction":"email","outcome":"follow-up"}]', 
    '2025-01-29T12:00:00+00:00', 
    'John Doe', 
    '+911234567890', 
    '{"location":"Mumbai","property_type":"3BHK"}', 
    'Positive', 
    'Referral', 
    'Active', 
    '2025-01-30T20:30:00+00:00'
),
(
    '22222222-bbbb-2222-bbbb-222222222222', 
    'f8cd1102-a3cb-400d-93fd-c59233f507be', 
    7500000, 
    0.9, 
    '2025-01-30T21:00:00+00:00', 
    'lead2@example.com', 
    '[{"interaction":"site visit","outcome":"highly interested"}]', 
    '2025-01-28T15:00:00+00:00', 
    'Jane Smith', 
    '+919876543210', 
    '{"location":"Pune","property_type":"2BHK"}', 
    'Neutral', 
    'Online Ad', 
    'Hot', 
    '2025-01-30T21:00:00+00:00'
),
(
    '33333333-cccc-3333-cccc-333333333333', 
    '302634ad-7aa0-4171-8c58-497f9b3910ad', 
    2500000, 
    0.6, 
    '2025-01-30T22:00:00+00:00', 
    'lead3@example.com', 
    '[{"interaction":"call","outcome":"considering"}]', 
    '2025-01-27T10:00:00+00:00', 
    'Alice Brown', 
    '+918765432109', 
    '{"location":"Mumbai Central","property_type":"1BHK"}', 
    'Negative', 
    'Walk-in', 
    'Warm', 
    '2025-01-30T22:00:00+00:00'
);
