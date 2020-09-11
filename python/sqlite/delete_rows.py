#! /usr/bin/env python

import sqlite3
 
def create_connection(db_file):
    try: conn = sqlite3.connect(db_file)
    except sqlite3.Error as e: print(e)
    return conn
 
def delete_task(conn, id):
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
 
def delete_all_tasks(conn):
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
 
def main():
    database = "pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2);
        # delete_all_tasks(conn);
 
if __name__ == '__main__': main()

