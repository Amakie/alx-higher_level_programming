#!/usr/bin/python3
"""scripts that lists all states"""

import sys
import MySQLdb

if __name__ == "__main__":

    u_name = sys.argv[1]
    p = sys.argv[2]
    db_name = sys.argv[3]
    h = 'localhost'

    db = MySQLdb.connect(host=h, port=3306, user=u_name, passwd=p, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE \
                   name LIKE BINARY 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close
    db.close
