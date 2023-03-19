#!/usr/bin/env python3

import sys, MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
	db=sys.argv[3], port=3306)
cur = db.cursor()
#match = sys.argv[4]
cur.execute("""select distinct cities.name from cities inner join states on states.id=cities.state_id where states.name=%s""", (sys.argv[4], ))
rows = cur.fetchall()
tmp_list = list(row[0] for row in rows)
#for city in tmp_list:
#    print(city)
print(*tmp_list, sep=", ")
cur.close()
db.close()

