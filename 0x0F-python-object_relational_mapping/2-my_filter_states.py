#!/usr/bin/env python3

#connect to mysql server, execute sql queries, display results

import sys, MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], 
        db=sys.argv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
