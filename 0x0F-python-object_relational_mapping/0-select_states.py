#!/usr/bin/python3
"""scripts that lists all states"""

import sys
import MySQLdb

if __name__ == "__main__":

    u_name = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    host_name = 'localhost'

    db = MySQLdb.connect(host=host_name, post=3306, user=u_name, passwd=passw, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT states.id, states.name FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close
    db.close



