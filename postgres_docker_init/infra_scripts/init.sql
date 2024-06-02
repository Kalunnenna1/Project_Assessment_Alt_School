
-- Create schema
CREATE SCHEMA IF NOT EXISTS HRANLY;


-- Create a table with the CSV file structure
CREATE TABLE HRANLY 
(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(255)
);


COPY hranly (id, name, age, email)
FROM '/data/hranly.csv' DELIMITER ',' CSV HEADER;