#!/usr/bin/python3

#connect to a db with MySQLdb
#get a cursor object 
#run the sql command then
#get rows and print them then
#close the cursor and mysql instances

import MySQLdb, sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

