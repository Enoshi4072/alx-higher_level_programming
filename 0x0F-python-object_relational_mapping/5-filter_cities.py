#!/usr/bin/python3
"""  takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=passwd, db=database_name)
    cursor = db.cursor()
    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))
    results = cursor.fetchone()
    if results and results[0]:
        print(results[0])
    else:
        print("")
    cursor.close()
    db.close()
