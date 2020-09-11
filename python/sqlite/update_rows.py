#! /usr/bin/env python

import sqlite3
 
def create_connection(db_file):
    try: conn = sqlite3.connect(db_file)
    except sqlite3.Error as e: print(e)
    return conn
 
def update_task(conn, task):
    sql = '''UPDATE tasks SET priority = ? , begin_date = ? , end_date = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
 
def main():
    database = "pythonsqlite.db"
    conn = create_connection(database)
    with conn: update_task(conn, (2, '2015-01-04', '2015-01-06', 2))
 
if __name__ == '__main__': main()

