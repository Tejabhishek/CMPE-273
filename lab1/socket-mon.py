'''Requirements

Use psutil and implement a network socket monitoring tool that can check how many TCP sockets are being created by a web application.
Create a Python script called socket-mon.py.
List all processes that have any socket connections (meaning the laddr and raddr fields exist).
Group by the PID and sort the output by the number of the connections per process.

Author : Sai Ravi Tejabhishek Sreepada
Date : 16th Feb, 2017
Subject : CMPE - 273 - Lab 1

Output:

"pid","laddr","raddr","status
"5764","127.0.0.1@50154","127.0.0.1@50153","ESTABLISHED"
"5764","127.0.0.1@50155","127.0.0.1@50156","ESTABLISHED"
"5764","127.0.0.1@50153","127.0.0.1@50154","ESTABLISHED"
"5764","127.0.0.1@50156","127.0.0.1@50155","ESTABLISHED"
"6036","2601:646:8400:d612:302c:25ce:4c9b:3b64@51147","2607:f8b0:400e:c00::bc@5228","ESTABLISHED"
"6036","10.0.0.32@52554","198.252.206.25@443","ESTABLISHED"
"4","10.0.0.32@139","10.0.0.241@58566","ESTABLISHED"
"4","10.0.0.32@139","10.0.0.241@58565","ESTABLISHED"
"3544","127.0.0.1@49162","127.0.0.1@62522","ESTABLISHED"
"3268","10.0.0.32@49237","23.74.64.60@443","CLOSE_WAIT"
"1304","127.0.0.1@62522","127.0.0.1@49162","ESTABLISHED"

Process finished with exit code 0


'''

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

print(""""pid","laddr","raddr","status"""")
for key,value in cou_dict_sort.items():
    for l in res_new:
        if key == l.pid:
            laddr = "%s@%s" % l.laddr
            raddr = ""
            if l.raddr:
                raddr = "%s@%s" % l.raddr
                print("\""+str(l.pid)+"\",\""+ str(laddr)+"\",\""+ str(raddr)+"\",\""+ str(l.status)+"\"")
                
                
