#!/usr/bin/python3
"""list all states"""


import MySQLdb
import sys
import sqlalchemy


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
