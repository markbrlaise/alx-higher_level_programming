#!/usr/bin/env python3
"""

basic protection against a sql injection
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    match = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
