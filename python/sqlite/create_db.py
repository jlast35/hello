#! /usr/bin/env python

import sqlite3
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print sqlite3.version
    except sqlite3.Error as e: print e
    finally:
        if conn: conn.close()
 
if __name__ == '__main__': create_connection("pythonsqlite.db")
