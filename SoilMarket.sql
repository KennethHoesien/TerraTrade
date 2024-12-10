use soilmarket;

-- Tables below are the required tables for our website, created as per the data model. 
CREATE TABLE Soil_Types (
    soil_id INT PRIMARY KEY,
    owner_id INT,
    pH_level INT,
    type VARCHAR(255),
    NPK_level DECIMAL,
    Quantity DECIMAL,
    availability VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE Owners (
    owner_id INT PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    role VARCHAR(255),
    phone_number INT
);

CREATE TABLE Listings (
    listing_id INT PRIMARY KEY,
    owner_id INT,
    soil_id INT,
    price DECIMAL,
    quantity DECIMAL,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (soil_id) REFERENCES Soil_Types(soil_id)
);

CREATE TABLE Farms (
    farm_id VARCHAR(255) PRIMARY KEY,
    soil_id INT,
    owner_id INT,
    listing_id INT,
    location VARCHAR(255),
    size DECIMAL,
    FOREIGN KEY (soil_id) REFERENCES Soil_Types(soil_id),
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id),
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id)
);


-- RUN THESE FIRST TO CHANGE THE TABLES IF YOU ALREADY HAVE THE DB SET UP, IF NOT. 
ALTER TABLE Soil_Types
DROP COLUMN provider_id;
ALTER TABLE Soil_Types ADD COLUMN owner_id INT;

ALTER TABLE Listings
DROP COLUMN user_id;
ALTER TABLE Soil_Types ADD COLUMN owner_id INT;


-- the actual data
INSERT INTO Owners (owner_id, name, phone_number, email)
VALUES
    (301, 'Alice Miller', '6041234567', 'alice.miller@farmmail.com'),
    (302, 'Bob Turner', '6042345678', 'bob.turner@farmmail.com'),
    (303, 'Charlie Wilson', '6043456789', 'charlie.wilson@farmmail.com'),
    (304, 'Diana Scott', '6044567890', 'diana.scott@farmmail.com'),
    (305, 'Evan Harris', '6045678901', 'evan.harris@farmmail.com');

-- Inserting data into Users table with user_id, name, address, role, and phone_number
INSERT INTO Users (user_id, name, address, role, phone_number)
VALUES
    (506, 'Fiona Clark', '303 Elm Ave, Victoria, BC', 'Buyer', 60467),
    (507, 'George Lewis', '404 Redwood Dr, Kelowna, BC', 'Buyer', 604789),
    (508, 'Hannah King', '505 Willow Rd, Vancouver, BC', 'Buyer', 60489),
    (509, 'Ian Walker', '606 Cherry St, Abbotsford, BC', 'Buyer', 60490),
    (510, 'Julia Wright', '707 Walnut Blvd, Prince Rupert, BC', 'Admin', 60401);

-- Inserting data into Soil_Types table with soil_id and associated attributes
-- Multiple soil types for each owner
INSERT INTO Soil_Types (soil_id, owner_id, pH_level, type, NPK_level, Quantity, availability, location)
VALUES
    (201, 301, 7, 'Loamy', 5.0, 1000.0, 'Available', 'Victoria, BC'),
    (202, 301, 6, 'Silty', 4.0, 1200.0, 'Available', 'Victoria, BC'),
    (203, 302, 6, 'Clay', 3.5, 1400.0, 'Limited', 'Kelowna, BC'),
    (204, 302, 7, 'Peaty', 6.0, 1600.0, 'Available', 'Kelowna, BC'),
    (205, 303, 5, 'Saline', 2.5, 800.0, 'Available', 'Vancouver, BC'),
    (206, 303, 6, 'Chalky', 5.5, 1100.0, 'Available', 'Vancouver, BC'),
    (207, 304, 7, 'Loamy', 4.5, 1300.0, 'Limited', 'Abbotsford, BC'),
    (208, 304, 5, 'Silty', 3.0, 1400.0, 'Available', 'Abbotsford, BC'),
    (209, 305, 6, 'Clay', 6.0, 1500.0, 'Limited', 'Prince Rupert, BC'),
    (210, 305, 6, 'Peaty', 5.0, 1700.0, 'Available', 'Prince Rupert, BC');

-- Inserting data into Listings table with listing_id, owner_id, soil_id, price, quantity, date
INSERT INTO Listings (listing_id, owner_id, soil_id, price, quantity, date)
VALUES
    (401, 301, 201, 50.0, 200.0, '2024-11-22'),
    (402, 301, 202, 45.0, 400.0, '2024-09-19'),
    (403, 302, 203, 40.0, 300.0, '2024-11-06'),
    (404, 302, 204, 60.0, 240.0, '2024-10-16'),
    (405, 303, 205, 55.0, 260.0, '2024-09-23'),
    (406, 303, 206, 70.0, 350.0, '2024-11-19'),
    (407, 304, 207, 65.0, 320.0, '2024-12-03'),
    (408, 304, 208, 80.0, 450.0, '2024-11-21'),
    (409, 305, 209, 75.0, 420.0, '2024-10-17'),
    (410, 305, 210, 85.0, 500.0, '2024-09-15');

-- Inserting data into Farms table with farm_id, soil_id, owner_id, listing_id, location, size
INSERT INTO Farms (farm_id, soil_id, owner_id, listing_id, location, size)
VALUES
    ('101', 201, 301, 401, '123 Evergreen Lane, Victoria, BC V8X 2M2, Canada', 50.0),
    ('102', 202, 302, 402, '456 Maple St, Kelowna, BC V1X 3Z3, Canada', 60.0),
    ('103', 203, 303, 403, '789 Oak Rd, Vancouver, BC V6B 4A5, Canada', 70.0),
    ('104', 204, 304, 404, '101 Pine Ave, Abbotsford, BC V2S 5K1, Canada', 80.0),
    ('105', 205, 305, 405, '202 Cedar Blvd, Prince Rupert, BC V8J 6B2, Canada', 90.0);



Select * FROM USERS;
Select * FROM OWNERS;
Select * FROM Soil_Types;
Select * FROM Farms;
Select * FROM Listings;