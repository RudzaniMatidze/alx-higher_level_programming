-- Lists all the cities of Califonia that can be found in the database hbtn_0d_usa
-- Lists all the rows of a column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
