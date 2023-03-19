#!/usr/bin/python3
"""

create a MySQLdb instance and connect
create a curosr instance from MySQLdb instance and run the SQL query
then get rows
close the instances then
"""
import MySQLdb
import sys

if name("__main__"):
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
