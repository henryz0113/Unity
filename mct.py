#Version 1.1.7
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

def Zenlayer():
    print('Reading Input')
    line = txt.get("1.0","end-1c")
    lines = line.split("\n")
    #print (lines)
    for i in lines :
        if 'UTC' in i :
            st_date = i.split()[2]
            st_time = i.split()[3]
            end_date = i.split()[5]
            end_time = i.split()[6]
            x2 = i.split()[0]
            if x2 == 'UTC':
                time_zone = 'UTC'
        #if 'Ending date' in i :
        #    end_dt = i
        if 'Expected Impact' in i :
            impact = i
        if 'Location' in i :
            loct = i
            loc_dt = loct.split()[1]
            if loc_dt == 'Washington' :
                loc_dt = 'Washington DC'
            if loc_dt == 'San' :
                loc_dt = 'San Jose'

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
    event = {
          #'summary': 'Zenlayer-Seoul-Impact',
      'summary': 'Zenlayer'+'-' + loc_dt+ '-' +'Impacting',
      'location': loc_dt,
      'description': line,
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
    print ("Added to the calendar")
    msgbox.showinfo("Info","Added to the calendar")

def Serverdotcom():
    print('Reading Input')
    line = txt.get("1.0","end-1c")
    lines = line.split("\n")
    #print (lines)
    for i in lines :
        if 'Starting date' in i :
            x = i.split()[2:5]
            dt = ''.join(x)
            dtObject = datetime.strptime(dt,"%B%d,%Y")
            dtConverted = dtObject.strftime("%Y-%m-%d")
            st_date = dtConverted
            st_time = i.split()[5]
            x2 = i.split()[6]
            if x2 == 'UTC':
                time_zone = 'UTC'
        if 'Ending date' in i :
            x = i.split()[2:5]
            dt = ''.join(x)
            dtObject = datetime.strptime(dt,"%B%d,%Y")
            dtConverted = dtObject.strftime("%Y-%m-%d")
            end_date = dtConverted
            end_time = i.split()[5]
        if 'Impact' in i :
            impact = i
        if 'Note' in i :
            loct = i
            loc_dt = loct.split()[11]
            if loc_dt == 'Washington' :
                loc_dt = 'Washington DC'
            if loc_dt == 'San' :
                loc_dt = 'San Jose'
    print (st_date)
    print (st_time)
    print (end_date)
    print (end_time)
    print (impact)
    print(loc_dt)

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
    event = {
          #'summary': 'Zenlayer-Seoul-Impact',
      'summary': 'Servers.com'+'-' + loc_dt+ '-' +'Impacting',
      'location': loc_dt,
      'description': line,
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
    print ("Added to the calendar")
    msgbox.showinfo("Info","Added to the calendar")

def Performive():
    print('Reading Input')
    line = txt.get("1.0","end-1c")
    lines = line.split("\n")
    #print (lines)
    for i in lines :
        if 'Planned Start' in i :
            x = i.split()[2:5]
            dt = ''.join(x)
            dtObject = datetime.strptime(dt,"%B%d,%Y")
            dtConverted = dtObject.strftime("%Y-%m-%d")
            st_date = dtConverted
            st_time = i.split()[5]
            st_time = datetime.strptime(st_time, '%I:%M%p')
            st_time = st_time.strftime("%H:%M %p")
            st_time = st_time[:-3]
            x2 = i.split()[6]
            if x2 == 'UTC':
                time_zone = 'UTC'
            if x2 == 'EDT' :
                time_zone = 'EST5EDT'

        if 'Expected End' in i :
            x = i.split()[2:5]
            dt = ''.join(x)
            dtObject = datetime.strptime(dt,"%B%d,%Y")
            dtConverted = dtObject.strftime("%Y-%m-%d")
            end_date = dtConverted
            end_time = i.split()[5]
            end_time = datetime.strptime(end_time, '%I:%M%p')
            end_time = end_time.strftime("%H:%M %p")
            end_time = end_time[:-3]
        if 'Expected Impact' or 'IMPACT' in i :
            impact = i
        if 'Title' in i :
            loct = i
            loc_dt = loct.split()[1]
            if loc_dt == 'Washington' :
                loc_dt = 'Washington DC'
            if loc_dt == 'San' :
                loc_dt = 'San Jose'
    print (st_date)
    print (st_time)
    print (end_date)
    print (end_time)
    print (impact)
    print(loc_dt)

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
    event = {
          #'summary': 'Zenlayer-Seoul-Impact',
      'summary': 'Performive'+'-' + loc_dt+ '-' +'Impacting',
      'location': loc_dt,
      'description': line,
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
    print ("Added to the calendar")
    msgbox.showinfo("Info","Added to the calendar")

def Velia():
    print('Reading Input')
    line = txt.get("1.0","end-1c")
    lines = line.split("\n")
    #print (lines)
    for i in lines:
        if 'Status: GREEN Event' in i :
            print("Green")
            for i in lines :
                if 'Start Date and Time' in i :
                    st_date = i.split()[4]
                    st_time = i.split()[5]
                    time_zone = i.split()[6]
                if 'End Date and Time' in i :
                    end_date = i.split()[4]
                    end_time = i.split()[5]
                if 'Action and Reason' in i :
                    impact = i
                if 'Location' in i :
                    loct = i
                    loc_dt = loct.split()[4]
                    if loc_dt == 'Frankfurt,':
                        loc_dt = 'Frankfurt'
                    if loc_dt == 'Washington' :
                        loc_dt = 'Washington DC'
                    if loc_dt == 'San' :
                        loc_dt = 'San Jose'
            print (st_date)
            print (st_time)
            print (end_date)
            print (end_time)
            print (impact)
            print (loc_dt)
            print(time_zone)
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
            event = {
                  #'summary': 'Zenlayer-Seoul-Impact',
              'summary': 'Velia'+'-' + loc_dt+ '-' +'NON-Impacting',
              'location': loc_dt,
              'description': line,
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
            print ("Added to the calendar")
            msgbox.showinfo("Info","Added to the calendar")
            break;
        else :
            print("Red")
            for i in lines :
                if 'Start Date and Time' in i :
                    st_date = i.split()[4]
                    st_time = i.split()[5]
                    time_zone = i.split()[6]
                if 'End Date and Time' in i :
                    end_date = i.split()[4]
                    end_time = i.split()[5]
                if 'Impact' in i :
                    impact = i
                if 'Location' in i :
                    loct = i
                    loc_dt = loct.split()[4]
                    if loc_dt == 'Frankfurt,':
                        loc_dt = 'Frankfurt'
                    if loc_dt == 'Washington' :
                        loc_dt = 'Washington DC'
                    if loc_dt == 'San' :
                        loc_dt = 'San Jose'
                    if loc_dt == 'Amsterdam,':
                        loc_dt = 'Amsterdam'
            print (st_date)
            print (st_time)
            print (end_date)
            print (end_time)
            print (impact)
            print (loc_dt)
            print(time_zone)
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
            event = {
                  #'summary': 'Zenlayer-Seoul-Impact',
              'summary': 'Velia'+'-' + loc_dt+ '-' +'Impacting',
              'location': loc_dt,
              'description': line,
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
            print ("Added to the calendar")
            msgbox.showinfo("Info","Added to the calendar")
            break;

def HUNDERADTB():
    print('Reading Input')
    line = txt.get("1.0","end-1c")
    lines = line.split("\n")
    #print (lines)
    for i in lines:
        if 'On the' in i :
            x1 = i.split()[2]
            if len(x1) == 3:
                st_dd = x1[0:1]
            else :
                st_dd = x1[0:2]
            st_mm = i.split()[4]
            st_yy = i.split()[5]
            x = st_dd + st_mm + st_yy
            dt = ''.join(x)
            dtObject = datetime.strptime(dt,"%d%B,%Y")
            dtConverted = dtObject.strftime("%Y-%m-%d")
            st_date = dtConverted
            end_date = st_date
            x2 = i.split()[7]
            st_time = x2
            x3 = i.split()[10]
            end_time = x3
            x4 = i.split()[8]
            zone = str(x4)
            if zone == 'BST':
               time_zone = 'Europe/London'
            if zone == 'MST':
               time_zone = 'MST7MDT'
        if 'impact' in i :
            x1 = i[12:]
            impact = x1

    loc_dt = 'CHANGE LOCATION'

    print(st_date)
    print(st_time)
    print(end_time)
    print(end_date)
    print(impact)
    print(loc_dt)
    print(time_zone)
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
    #end_tp = end_date + 'T' +end_time+zone
    print(end_tp)
    event = {
          #'summary': 'Zenlayer-Seoul-Impact',
      "summary": '100TB'+'-' + loc_dt+ '-' +'Impacting',
      "location": loc_dt,
      "description": line,
      "start": {
        "dateTime": st_tp,
        "timeZone": time_zone
      },
       "end": {
         "dateTime": end_tp,
         "timeZone": time_zone
       },
         "reminders": {
           "useDefault": False,
           "overrides": [
                        {'method': 'popup', 'minutes': 60},
        ],
        },
    }
    event = service.events().insert(calendarId='henry.lee@unity3d.com', body=event).execute()
    print ("Added to the calendar")
    msgbox.showinfo("Info","Added to the calendar")

def formatreq():
    txt.insert(END, "Starting date: YYYY-MM-DD HH:MM \n" "Ending date: YYYY-MM-DD HH:MM\n" "Provider:\n" "Overview:\n" "Impact:\n" "Affected Regions:\n" "Impacted Servers:")

#Start menu
root = Tk()
root.title("Welcome to Maintenance Calendar Assistance")
root.geometry("700x380+500+200")
txt1 = Text(root,width=20, height=2)
txt1.insert(END, "Multiplay V.1.1.7")
txt = Text(root, width=75, height=20)
#label1 = Label(root, text= "NEW")
#E1 = Entry(root, bd =1, width = 60)

Zenlayer = Button(root, bg="light goldenrod", text ="Zenlayer", command=Zenlayer, textvariable=StringVar)
Zenlayer.place(x=10, y=20)
Serverdotcom = Button(root, bg="sky blue", text ="Server.com", command=Serverdotcom, textvariable=StringVar)
Serverdotcom.place(x=10, y=60)
Performive = Button(root, bg="coral", text ="Performive", command=Performive, textvariable=StringVar)
Performive.place(x=10, y=100)
Velia = Button(root, bg="SeaGreen1", text ="Velia", command=Velia, textvariable=StringVar)
Velia.place(x=10, y=140)
HUNDERADTB = Button(root, bg="wheat1", text ="100TB", command=HUNDERADTB, textvariable=StringVar)
HUNDERADTB.place(x=10, y=180)
formatreq = Button(root, bg="MediumPurple1", text ="Format", command=formatreq, textvariable=StringVar)
formatreq.place(x=630, y=10)



#submit = Button(root, text ="Submit", command=save, textvariable=StringVar )
#bt1 = Button(root, bg="yellow", text = "Zenlayer", command=Zenlayer)
#bt1.pack()
#label1.pack()
#E1.pack()
txt.pack()
txt1.place(x=500,y=300)
#submit.pack()


root.mainloop()
