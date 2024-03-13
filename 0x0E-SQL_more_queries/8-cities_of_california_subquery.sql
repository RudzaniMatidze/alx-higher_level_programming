-- Lists all the cities of califonia that can be found in the database hbtn_0d_usa
-- Lists all rows of a column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id state WHERE name = 'Califonia') ORDER BY id ASC;
