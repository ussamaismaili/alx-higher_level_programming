#!/usr/bin/python3
"""Module for states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    curs = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name\
        FROM `cities` INNER JOIN `states`\
        ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    curs.execute(query)
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    conn.close()
