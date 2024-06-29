BEGIN;

-- Create the enum for the gender
CREATE TYPE gender_enum AS ENUM ('male', 'female');

CREATE TABLE IF NOT EXISTS user (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    gender gender_enum NOT NULL,
    enabled BOOLEAN NOT NULL);

-- Add a unique constraint on the email column
ALTER TABLE user
ADD CONSTRAINT unique_email UNIQUE (email);

COMMIT;