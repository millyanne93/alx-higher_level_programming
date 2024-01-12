#!/usr/bin/python3
"""
Script that lists all cities of a given state from the hbtn_0e_4_usa database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Get the state name from command line arguments
    state_name = sys.argv[4]

    # Create a cursor and execute the query
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name LIKE BINARY (%s) ORDER BY cities.id ASC",
                (state_name,))

    # Fetch all rows and close the cursor and database connection
    table = cur.fetchall()
    cur.close()
    db.close()

    # Use list comprehension and join to create a comma-separated string
    str_cities = ", ".join(row[0] for row in table)

    # Print the result
    print(str_cities)
