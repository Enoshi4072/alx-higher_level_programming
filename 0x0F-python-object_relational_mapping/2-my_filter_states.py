#!/usr/bin/python3
""" A script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=passwd, db=database_name)
        cursor = db.cursor()
        query = "SELECT * FROM states where name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name_searched,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
