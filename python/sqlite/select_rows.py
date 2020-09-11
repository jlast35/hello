#! /usr/bin/env python

import sqlite3
 
def create_connection(db_file):
    try: conn = sqlite3.connect(db_file)
    except sqlite3.Error as e: print(e)
    return conn
 
def select_all_tasks(conn):
    print("2. Query all tasks")
    for row in conn.cursor().execute("SELECT * FROM tasks"): print(row)
 
def select_task_by_priority(conn, priority):
    print("1. Query task by priority:")
    for row in conn.cursor().execute("SELECT * FROM tasks WHERE priority=?", (priority,)): print(row)
 
def main():
    database = "pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        select_task_by_priority(conn, 1)
        select_all_tasks(conn)
 
if __name__ == '__main__': main()
