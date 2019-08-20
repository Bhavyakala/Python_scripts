# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:12:18 2019

@author: hp
"""

import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from smtplib import SMTP
f = open("password.dat","rb")
password = f.read()
password = password.decode()
f.close()
class my_handler(FileSystemEventHandler):
    def on_created(self, event):
        m = "created"
        s = SMTP(host='smtp.gmail.com',port = 587)
        s.starttls()
        s.login("email_sender",password)
        message = "file "+ m
        s.sendmail("email_sender","email_receiver",message)
        s.quit()
    def on_modified(self,event):
        m = "modified"
        s = SMTP('smtp.gmail.com', port = 587)
        s.starttls()
        s.login("email_sender",password)
        message = "file "+ m
        s.sendmail("email_sender","email_receiver",message)
        s.quit()
    def on_deleted(self,event):
        m = "deleted"
        s = SMTP('smtp.gmail.com', port = 587)
        s.starttls()
        s.login("email_sender",password)
        message = "file "+ m
        s.sendmail("email_sender","email_receiver",message)
        s.quit()
obs = Observer()
event = my_handler()
obs.schedule(event,path = 'C:/Users/hp/Desktop/python_scripts/target', recursive = True)
obs.start()
try:
    while True :
        time.sleep(1)
except KeyboardInterrupt:
        obs.stop()
obs.join()        