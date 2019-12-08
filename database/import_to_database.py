import sqlite3

# SQLite DB Name
DB_Name =  "event.db"

def insert_in_database(sql_query,argument):
	print("inserting in database")
	conn = sqlite3.connect(DB_Name)
	#print("connected")
	c = conn.cursor()
	#print("c ready")
	c.execute(sql_query,argument)
	#print("executed")
	conn.commit()
	#print("commited")
	c.close()
	#print("c closed")
	conn.close()
	#print("conn closed")
	print("inserted")
	return