#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM states")
    rows = mycur.fetchall()
    for row in rows:
        print(row)
    mycur.close()
    mydb.close()
