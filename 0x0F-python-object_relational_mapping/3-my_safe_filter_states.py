#!/usr/bin/python3
""" list states from db """
import MySQLdb
import sys


def connect_db(username, password, db_name, state_name):
    """ connect function """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
                    ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    connect_db(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
