#Version Beta 1.1
#Created by Henry Lee  (henry.lee@unity3d.com)
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import datetime
from datetime import datetime
import tkinter.messagebox as msgbox
from tkinter import *
SCOPES = ['https://www.googleapis.com/auth/calendar']

def formatreq():
    txt.insert(END, "Identifying Code: \n" "Starting date: YYYY-MM-DD HH:MM TimeZone \n" "Ending date: YYYY-MM-DD HH:MM TimeZone\n" "Provider:\n" "Overview:\n" "Impact:\n" "Affected Regions:\n" "Affected Customer:\n" "GF entries link:")

def add():
    k1 = b_var1.get()
    if k1 == 0 :
            print('Reading Input')
            line = txt.get("1.0","end-1c")
            lines = line.split("\n")
            for i in lines :
                if 'Identifying Code' in i :
                    idcode = i.split()[2]
                if 'Starting date' in i :
                    st_date = i.split()[2]
                    st_time = i.split()[3]
                if 'Ending date' in i :
                    end_date = i.split()[2]
                    end_time = i.split()[3]
                    zone = i.split()[4]
                    if zone == 'UTC' :
                        time_zone = 'UTC'
                    if zone == 'BST':
                        time_zone = 'Europe/London'
                    if zone == 'MST' :
                        time_zone = 'MST7MDT'
                    if zone == 'MDT':
                        time_zone = 'MST7MDT'
                    if zone == 'EST' :
                        time_zone = 'EST5EDT'
                    if zone == 'EDT':
                        time_zone = 'EST5EDT'
                if 'Provider' in i :
                    provider = i[10:]
                if 'Impact' in i :
                    impact = i[7:]
                if 'Overview' in i :
                    overview = i[9:]
                if 'Regions' in i :
                    loc_dt = i[17:]
                if 'Customer' in i :
                    cust = i[18:]
                if 'GF entries link' in i :
                    GFlink = i[17:]

            print(idcode)
            print (st_date)
            print (st_time)
            print (end_date)
            print (end_time)
            print("here")
            print (time_zone)
            print (impact)
            print (overview)
            print (cust)
            print(loc_dt)
            print(GFlink)

            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            service = build('calendar', 'v3', credentials=creds)
            print("you are logged in")
            st_tp = st_date + 'T' +st_time+':00'
            print(st_tp)
            end_tp = end_date + 'T' +end_time+':00'
            print(end_tp)
            st_format = st_date + ' ' + st_time  + ' ' + time_zone
            end_format = end_date + ' ' + end_time  + ' ' + time_zone
            desp = 'Starting date: ' + st_format + '\n' + 'Ending date: ' + end_format + '\n' + 'Provider: ' + provider + '\n' + 'Overview: ' + overview + '\n' +  'Impact :' + impact + '\n' + "Affected Regions: " + loc_dt +'\n'+ "Affected Customer: " + cust +'\n'+ "Impacted Servers:" + GFlink + "\n"
            #"Starting date: YYYY-MM-DD HH:MM TimeZone \n" "Ending date: YYYY-MM-DD HH:MM TimeZone\n" "Provider:\n" "Overview:\n" "Impact:\n" "Affected Regions:\n" "Affected Customer:\n" "GF entries link:")
            event = {
                  #'summary': 'Zenlayer-Seoul-Impact',
              'summary': provider +'-' + idcode + '-'+ loc_dt+ '-' +'Impacting',
              'location': loc_dt,
              'description': desp,
              'start': {
                'dateTime': st_tp,
                'timeZone': time_zone
              },
               'end': {
                 'dateTime': end_tp,
                 'timeZone': time_zone
               },
                 'reminders': {
                   'useDefault': False,
                   'overrides': [
                                {'method': 'popup', 'minutes': 60},
                ],
                },
            }
            event = service.events().insert(calendarId='unity3d.com_a9mh8fg2cmoe9mv0p18jc5vptk@group.calendar.google.com', body=event).execute()
            #event = service.events().insert(calendarId='henry.lee@unity3d.com', body=event).execute()
            print ("Added to the calendar")
            msgbox.showinfo("Info","Added to the calendar")
    else :
            print('Reading Input')
            line = txt.get("1.0","end-1c")
            lines = line.split("\n")
            for i in lines :
                if 'Identifying Code' in i :
                    idcode = i.split()[2]
                if 'Starting date' in i :
                    st_date = i.split()[2]
                    st_time = i.split()[3]
                if 'Ending date' in i :
                    end_date = i.split()[2]
                    end_time = i.split()[3]
                    zone = i.split()[4]
                    if zone == 'UTC' :
                        time_zone = 'UTC'
                    if zone == 'BST':
                        time_zone = 'Europe/London'
                    if zone == 'MST' :
                        time_zone = 'MST7MDT'
                    if zone == 'MDT':
                        time_zone = 'MST7MDT'
                    if zone == 'EST' :
                        time_zone = 'EST5EDT'
                    if zone == 'EDT':
                        time_zone = 'EST5EDT'
                if 'Provider' in i :
                    provider = i[10:]
                if 'Impact' in i :
                    impact = i[7:]
                if 'Overview' in i :
                    overview = i[9:]
                if 'Regions' in i :
                    loc_dt = i[17:]
                if 'Customer' in i :
                    cust = i[18:]
                if 'GF entries link' in i :
                    GFlink = i[17:]

            print(idcode)
            print (st_date)
            print (st_time)
            print (end_date)
            print (end_time)
            print (time_zone)
            print (impact)
            print (overview)
            print (cust)
            print(loc_dt)
            print(GFlink)

            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            service = build('calendar', 'v3', credentials=creds)
            print("you are logged in")
            st_tp = st_date + 'T' +st_time+':00'
            print(st_tp)
            end_tp = end_date + 'T' +end_time+':00'
            print(end_tp)
            st_format = st_date + ' ' + st_time  + ' ' + time_zone
            end_format = end_date + ' ' + end_time  + ' ' + time_zone
            desp = 'Starting date: ' + st_format + '\n' + 'Ending date: ' + end_format + '\n' + 'Provider: ' + provider + '\n' + 'Overview: ' + overview + '\n' +  'Impact :' + impact + '\n' + "Affected Regions: " + loc_dt +'\n'+ "Affected Customer: " + cust +'\n'+ "Impacted Servers:" + GFlink + "\n"
            #"Starting date: YYYY-MM-DD HH:MM TimeZone \n" "Ending date: YYYY-MM-DD HH:MM TimeZone\n" "Provider:\n" "Overview:\n" "Impact:\n" "Affected Regions:\n" "Affected Customer:\n" "GF entries link:")
            event = {
                  #'summary': 'Zenlayer-Seoul-Impact',
              'summary': provider +'-' + idcode + '-'+ loc_dt+ '-' +'Non-Impacting',
              'location': loc_dt,
              'description': desp,
              'start': {
                'dateTime': st_tp,
                'timeZone': time_zone
              },
               'end': {
                 'dateTime': end_tp,
                 'timeZone': time_zone
               },
                 'reminders': {
                   'useDefault': False,
                   'overrides': [
                                {'method': 'popup', 'minutes': 60},
                ],
                },
            }
            #event = service.events().insert(calendarId='unity3d.com_a9mh8fg2cmoe9mv0p18jc5vptk@group.calendar.google.com', body=event).execute()
            event = service.events().insert(calendarId='unity3d.com_a9mh8fg2cmoe9mv0p18jc5vptk@group.calendar.google.com', body=event).execute()
            print ("Added to the calendar")
            msgbox.showinfo("Info","Added to the calendar")



root = Tk()
root.title("Welcome to Maintenance Calendar Assistance Beta 1.1")
root.geometry("800x350+500+300")
txt1 = Text(root,width=20, height=2)
txt1.insert(END, "Multiplay Beta 1.1")
txt = Text(root, width=75, height=20,borderwidth=2)

b_var1 = IntVar()
btn1 = Checkbutton(root, text="Non-Impact", variable=b_var1)
btn1.place(x=700, y=40)

formatreq = Button(root, bg="MediumPurple1", text ="Format", command=formatreq, textvariable=StringVar)
formatreq.place(x=700, y=10)
add = Button(root, bg="light goldenrod", text ="Add to Calendar", command=add, textvariable=StringVar)
add.place(x=10, y=20)

txt.pack()
txt1.place(x=600,y=300)
root.mainloop()
