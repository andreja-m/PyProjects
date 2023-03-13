#!/usr/bin/env python3

import sqlite3
import os
import time
from datetime import datetime
import datetime

while True:
    os.system('rm -rf His && cp -r $HOME/.config/BraveSoftware/Brave-Browser/Default/History $HOME/browser_history/His')
    conn = sqlite3.connect('His')
    c = conn.cursor()
    his = c.execute('''SELECT url, title, last_visit_time FROM urls''')

    for i in c:
        pass
        #ts = int(i[2])
        #unixToDatetime = datetime.datetime.fromtimestamp(ts) # Unix Time
        #print(unixToDatetime)
        #print(i[0], "==", i[1], '==')

    #dt_object = datetime.datetime.fromtimestamp(i[2]/1000000.0)
    value = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=i[2]+3600000000)

    print(i[1], value)

    time.sleep(5)

#print(his)
