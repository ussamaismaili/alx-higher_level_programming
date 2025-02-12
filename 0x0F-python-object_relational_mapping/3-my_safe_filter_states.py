#!/usr/bin/python3
"""Module for states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    curs = conn.cursor()

    query = "SELECT * FROM `states`\
        WHERE `name` LIKE BINARY %s ORDER BY id ASC"
    state_name = argv[4]
    curs.execute(query, (state_name,))
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    conn.close()
