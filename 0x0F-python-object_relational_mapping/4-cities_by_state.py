#!/usr/bin/python3
""" list cities from db """
import MySQLdb
import sys


def connect_db(username, password, db_name):
    """ connect function """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities JOIN states ON cities.state_id =
               states.id ORDER BY states.id"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    connect_db(sys.argv[1], sys.argv[2], sys.argv[3])
