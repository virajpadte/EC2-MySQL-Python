#!/usr/bin/python

import MySQLdb
import time
import datetime

# Open database connection
db = MySQLdb.connect("<type db server IP>","<type username>","<type password>","iotdata")
#testing connection:
if db.open:
  print("connection is established")
else:
  print("could not establish connection. Check credentials or connects sysops admin")
# prepare a cursor object using cursor() method
cursor = db.cursor()

#get all the needed data elements for constructing the query:
ts = time.time()
gen_timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# Prepare SQL query to INSERT a record into the database.
query = """INSERT INTO data(uid, xaxis, yaxis, zaxis) VALUES ('VIRAJ75B-3168-45D1-94F1-94F3A9D14F25', '0', '0', '7')"""
try:
   # Execute the SQL command
   cursor.execute(query)
   # Commit your changes in the database
   db.commit()
   #debug print:
   print("data inserted in the db table")
except:
   # Rollback in case there is any error
   db.rollback()
# disconnect from server
db.close()