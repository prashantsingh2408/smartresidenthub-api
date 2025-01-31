CREATE TABLE lead ( -- use lead insed of leads as showing issue on superbase
    id UUID PRIMARY KEY,
    assigned_rm_id UUID NULL,
    budget NUMERIC NULL, -- range 
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
 


-- Insertiong
