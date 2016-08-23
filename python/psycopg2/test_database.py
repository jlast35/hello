#!/usr/bin/env python

import psycopg2
from psycopg2.extensions import AsIs

def insert_dictionary(tablename, dictionary):
	keys = dictionary.keys()
	values = [ dictionary[key] for key in keys ]
	sqlCommand = "INSERT INTO {table} ({keys}) VALUES ({values});"\
	  .format(table=tablename, keys=", ".join(keys),\
	  values=", ".join(['%s' for value in values]))
	#print sqlCommand, values
	return (sqlCommand, values)

# this seems to me the simplest and most straightforward to understand
def insert_row(table, dictionary, cursor):
	columns = AsIs((', ').join(dictionary.keys()))
        values = tuple(dictionary[key] for key in dictionary.keys())
	insert_command="insert into %s (%s) values %s"
	print cursor.mogrify(insert_command,(table,columns,values))
	
# clever but too strange and uses concat
def insert_dictionary3(table, dictionary, cur):
        keys = AsIs((', ').join(dictionary.keys()))
        values = AsIs((', ').join(['%('+key+')s' for key in dictionary.keys()]))
        insert="insert into %s (%s) values (%s)"
        print cur.mogrify(cur.mogrify(insert, (table, keys, values)),dictionary)


connection = psycopg2.connect("dbname=postgres")
cursor = connection.cursor()

table = 'comments'
dictionary = {'comment': 'Comment1', 'extra': 'Comment2'}

insert_row(table, dictionary, cursor)

#sqlCommand, data = insert_dictionary('comments', dictionary)
#cursor.execute(sqlCommand, data)

#cursor.execute(*insert_dictionary(table, dictionary))
#conn.commit()

cursor.execute("select * from comments;")
for row in cursor:
	print row

connection.close()

