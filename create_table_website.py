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
  starting_date_time text,
  ending_date_time text,
  difficulty text,
  supported_language text
);

DROP TABLE if exists TechGig_Coding_Event_Data ;
CREATE TABLE TechGig_Coding_Event_Data (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  hosting_website TEXT, 
  event_name TEXT, 
  event_type TEXT, 
  event_url TEXT, 
  starting_date_time TEXT, 
  ending_date_time TEXT, 
  contest_prize TEXT, 
  skill_required TEXT 
);

DROP TABLE if exists TechGig_Hiring_Event_Data ;
CREATE TABLE "TechGig_Hiring_Event_Data" ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  hosting_website TEXT, 
  event_name TEXT, 
  event_type TEXT, 
  event_url TEXT, 
  starting_date_time TEXT, 
  ending_date_time TEXT, 
  job_role TEXT, 
  skill_required TEXT, 
  minimum_experience TEXT, 
  job_salary TEXT, 
  job_location TEXT 
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