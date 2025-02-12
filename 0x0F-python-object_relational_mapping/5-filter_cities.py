#!/usr/bin/python3
"""Module for states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    curs = conn.cursor()

    query = "SELECT cities.name\
        FROM `cities` INNER JOIN `states`\
        ON cities.state_id = states.id\
        WHERE states.name LIKE BINARY %s\
        ORDER BY cities.id ASC"
    curs.execute(query, (argv[4],))
    query_rows = curs.fetchall()
    filtred_cities = ()
    for row in query_rows:
        filtred_cities += row
    print(*filtred_cities, sep=", ", end="\n")
    curs.close()
    conn.close()
