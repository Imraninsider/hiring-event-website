import time

from parser.hackerEarth import hackerearth_events
from parser.techgig import techgig_events

hackerEarth_event_list = []
techgig_event_list = []


while(1):
    hackerearth_events(hackerEarth_event_list)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    techgig_event_list = techgig_events(techgig_event_list)
    print("*****************************************************************")
    print("*********************** WAIT 10 SEC *****************************")
    time.sleep(10)
