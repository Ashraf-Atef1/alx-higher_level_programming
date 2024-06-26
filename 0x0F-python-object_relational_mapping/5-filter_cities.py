#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    results = [row[0] for row in rows]
    print(*results, sep=", ")
