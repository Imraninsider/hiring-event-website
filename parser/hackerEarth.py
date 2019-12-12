import json
import time
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
                
                #class for event details list
                event_details = scarp_link(i['url']) 

                dataset.append( event_details.role) #job role 
                dataset.append(event_details.experience) #minimum experience
                dataset.append(event_details.salary) #job salary
                # print(dataset)
                #Push into DB Table
                import_to_database.insert_in_database("INSERT INTO Hiring_Event_Data (hosting_website,event_name,event_url,starting_date_time,ending_date_time,job_role, minimum_experience,salary) VALUES (?,?,?,?,?,?,?,?)",dataset)
                print("inserted event: ", i['title'])
    # for deleting item from list which is not in the current hacker earth json file
    for i in event_list:
        if i not in current_event_list:
            event_list.remove(i)

    print(event_list)

import scrapy
from lxml import html

class scarp_link:

    def __init__(self,url):
        print("scarping for job role")
        page = requests.get(url)
        tree = html.fromstring(page.content)
        # print(page.content)
        event_details = tree.xpath('//span[@class="light regular"]/text()')
        # print(buyers)
        self.role = event_details[1]
        self.experience = event_details[2]
        self.salary = tree.xpath('//span[@class="light regular ctc-string"]/text()')[0]
        # print(event_details)
        # print(self.salary)
    