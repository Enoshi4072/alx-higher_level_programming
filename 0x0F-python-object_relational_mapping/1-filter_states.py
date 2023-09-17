#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=passwd, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
