#!/usr/bin/python

import MySQLdb
# Open database connection
db = MySQLdb.connect("<type db server IP>","<type username>","<type password>","iotdata")
#testing connection:
if db.open:
  print("connection is established")
else:
  print("could not establish connection. Check credentials or connects sysops admin")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
query = "SELECT * FROM data"
try:
   # Execute the SQL command
   cursor.execute(query)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   #print received data:
   print(results)
except:
   print "Error: unable to fetch data"
# disconnect from server
db.close()