import os
import webbrowser
from threading import Thread
import urllib3
    
def start_server():
    os.system("python manage.py runserver")

def open_browser():
    http = urllib3.PoolManager()
    r = http.request('GET','http://127.0.0.1:8000/')
    while r.status != 200:
        http = urllib3.PoolManager()
        r = http.request('GET','http://127.0.0.1:8000/')
    if r.status == 200:
        webbrowser.open('http://127.0.0.1:8000/')
        
Thread(target = start_server).start()
Thread(target = open_browser).start()


