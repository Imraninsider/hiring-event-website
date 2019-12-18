import time
import requests
from lxml import html
from database import import_to_database

def techgig_events(event_list):
    current_event_list = []
    TECHGIG_URL = "https://www.techgig.com/challenge"
    print("connecting to TechGig...")
    page = requests.get(TECHGIG_URL)
    tree = html.fromstring(page.content)
    print("connected to TechGig")

    for doc in tree.xpath('//div[@id="live-contest-listing"]/div'):
        # info = str(doc.xpath('string(*)'))
        # print(info.translate({ord(i) : None for i in '\n\t\r'}))
        contest_title = str(doc.xpath('header//div[@class="details"]/div/h3/text()')[0])
        current_event_list.append(contest_title)
        if contest_title in event_list:
            continue

        contest_info = []

        contest_url = str(doc.xpath('header/a/@href')[0])
        contest_type = str(doc.xpath('header//div[@class="details"]/div/p/span/text()')[0]).strip(" by")
        # contest_registered = str(doc.xpath('header//dl[@class="description-list"]/dd[1]/text()')[0])
        contest_ends_on = str(doc.xpath('header//dl[@class="description-list"]/dd[2]/text()')[0])
        contest_tests =  str(doc.xpath('div[@class="content clearfix"]//dl[@class="description-list"][1]/dd[1]/text()')[0])
        contest_skills =  str(doc.xpath('div[@class="content clearfix"]//dl[@class="description-list"][1]/dd[2]/text()')[0])
        contest_benefit =  str(doc.xpath('div[@class="content clearfix"]//dl[@class="description-list"][2]/dd/text()')[0])

        contest_benefit = contest_benefit.translate({ord(i): None for i in '\n\t\r'}) # if 'contest_type' is 'Hiring  Challenge' then benefit will be 'JOB DETAILS' otherwise benefit will be prize value

        if(contest_type == 'Hiring Challenge'):
            [job_role, job_salary, minimum_experience, job_location] = contest_benefit.split('|')
            contest_info = ["TechGig", contest_title, contest_type, contest_url, None, contest_ends_on, job_role, contest_skills, minimum_experience, job_salary, job_location]
            import_to_database.insert_in_database("INSERT INTO TechGig_Hiring_Event_Data (hosting_website,event_name,event_type,event_url,starting_date_time,ending_date_time,job_role, skill_required, minimum_experience,job_salary,job_location) VALUES (?,?,?,?,?,?,?,?,?,?,?)",contest_info)
        else:
            contest_info = ["TechGig", contest_title, contest_type, contest_url, None, contest_ends_on, contest_benefit, contest_skills]
            import_to_database.insert_in_database("INSERT INTO TechGig_Coding_Event_Data (hosting_website,event_name,event_type,event_url,starting_date_time,ending_date_time,contest_prize, skill_required) VALUES (?,?,?,?,?,?,?,?)",contest_info)

        print(contest_info)
    
    event_list = current_event_list
    print(event_list)
    return event_list
        


if __name__ == "__main__":
    techgig_event_list = []
    while(1):
        techgig_event_list = techgig_events(techgig_event_list)
        for i in techgig_event_list:
            print(i)
        print("********************************************************************")
        time.sleep(10)


