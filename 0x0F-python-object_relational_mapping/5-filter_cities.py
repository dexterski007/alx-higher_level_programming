#!/usr/bin/python3
""" list cities from db """
import MySQLdb
import sys


def connect_db(username, password, db_name, state_name):
    """ connect function """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    query = """SELECT cities.name
               FROM cities JOIN states ON cities.state_id =
               states.id WHERE states.name LIKE BINARY %s"""
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    res = list(row[0] for row in result)
    print(*res, sep=", ")
    cursor.close()
    db.close()


if __name__ == "__main__":
    connect_db(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
