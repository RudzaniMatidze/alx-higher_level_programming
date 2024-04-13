#!/usr/bin/python3
"""Module that lists all the states from the MySQL server"""
import sys
import MySQLdb


def filter_states(username, password, database):
    try:
        # Connect to MySQL server
        with MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
        ) as db:
            cursor = db.cursor()

            # Execute SQL query to retrieve states starting with 'N'
            cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

            # Fetch all the rows
            rows = cursor.fetchall()

            # Print the results
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    except Exception as e:
        print("Error:", e)

# Example usage:
username = "your_username"
password = "your_password"
database = "your_database_name"
filter_states(username, password, database)
