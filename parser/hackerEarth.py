import json
#imports requests module. You need this to perform requests
import requests

from database import import_to_database

def hackerearth_events(event_list):
    print("connecting to hacker-earth")

    sitedata = requests.get("https://www.hackerearth.com/chrome-extension/events/")
    data = json.loads(sitedata.content)
    print("connected")
    
    current_event_list = []

    for i in data['response']:
        current_event_list.append(i['title'])
        if i['title'] not in event_list:
            event_list.append(i['title'])
            
            if i['challenge_type']=="Hiring Challenges":
            #dataset for data import in database
                dataset = []
                dataset.append("hacker earth")
                dataset.append(i['title'])# event_name = i['title']
                dataset.append(i['url'])  # event_url = str(i['url'])
                dataset.append(i['start_utc_tz'])# starting_date_time = str(i['start_utc_tz']),
                dataset.append(i['end_utc_tz'])# ending_date_time =  i['end_utc_tz']
                dataset.append('NULL') # job_role =  'NULL'
                dataset.append('NULL')# minimum_experience ='NULL'
                dataset.append('NULL')# skills = 'NULL'
                print(dataset)
                #Push into DB Table
                import_to_database.insert_in_database("INSERT INTO Hiring_Event_Data (hosting_website,event_name,event_url,starting_date_time,ending_date_time,job_role, minimum_experience,skills) VALUES (?,?,?,?,?,?,?,?)",dataset)

    # for deleting item from list which is not in the current hacker earth json file
    for i in event_list:
        if i not in current_event_list:
            event_list.remove(i)

    print(event_list)