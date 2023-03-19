#!/usr/bin/env python3

import sys, MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2]
	db=sys.argv[3], port=3306)
cur = db.cursor()
cur.execute("select * from cities ")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()

