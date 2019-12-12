#------------------------------------------
#--- Author: 
#--- Date: 8th July 2019
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import sqlite3

# SQLite DB Name
DB_Name =  "event.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists Hiring_Event_Data ;
create table Hiring_Event_Data (
  id integer primary key autoincrement,
  hosting_website text,
  event_name text,
  event_url text,
  starting_date_time text,
  ending_date_time text,
  job_role text,
  minimum_experience text,
  salary text
);

drop table if exists Coding_Event_Data ;
create table Coding_Event_Data (
  id integer primary key autoincrement,
  hosting_website text,
  event_name text,
  event_url,
  event_id text,
  starting_date text,
  starting_time text,
  ending_date text,
  ending_time text,
  difficulty text,
  supported_language text
);

"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()