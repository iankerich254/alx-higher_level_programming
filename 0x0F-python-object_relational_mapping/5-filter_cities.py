#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute the query to get all cities in the specified state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the result of the query
    rows = cursor.fetchall()

    # Print the city names, comma-separated
    print(", ".join(row[0] for row in rows))

    # Close the cursor and database connection
    cursor.close()
    db.close()
