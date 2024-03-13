-- Creates the database hbtn_0d_usa and the table cities (in the databse hbtn_0d_usa) on your MySQL server
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use a database
USE hbtn_0d_usa;
-- Create a table
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
