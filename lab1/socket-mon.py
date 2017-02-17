'''Requirements

Use psutil and implement a network socket monitoring tool that can check how many TCP sockets are being created by a web application.
Create a Python script called socket-mon.py.
List all processes that have any socket connections (meaning the laddr and raddr fields exist).
Group by the PID and sort the output by the number of the connections per process.

Author : Sai Ravi Tejabhishek Sreepada
Date : 16th Feb, 2017
Subject : CMPE - 273 - Lab 1'''

import psutil
import collections

res=psutil.net_connections(kind = 'tcp')
res_new = sorted(res, key=lambda x: x[6])

my_list = []
for i in res_new:
    if i.raddr != ():
        my_list.insert(0,i.pid)

cou_dict = collections.Counter(my_list)
cou_dict_sort = dict(sorted(cou_dict.items(), key=lambda x: x[1],reverse=True))

print(""""pid","laddr","raddr","status""")
for key,value in cou_dict_sort.items():
    for l in res_new:
        if key == l.pid:
            laddr = "%s@%s" % l.laddr
            raddr = ""
            if l.raddr:
                raddr = "%s@%s" % l.raddr
                print("\""+str(l.pid)+"\",\""+ str(laddr)+"\",\""+ str(raddr)+"\",\""+ str(l.status)+"\"")