#!/usr/bin/python3
"""
Lists all states where 'name' matches the argument from the database hbtn_0e_0_usa, safe from SQL injection
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to get states with the name matching the argument using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows from the result of the query
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
