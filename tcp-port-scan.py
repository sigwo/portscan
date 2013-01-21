#Script by Sigwo
# 21Jan13
#
#Raw TCP port scanner.
#
#make the output go to file and pull that file into a GUI, load new window if payload is
#started, make a well known port scanner and complete port scanner, make an IP range selector
#
import datetime
import socket
import sys
#import subprocess

      #step in from port-scan.py

host = raw_input("Please put in IP address or FQDN of host: ")
timestart = datetime.datetime.now()
t1 = str(timestart)
#start-time = datetime.datetime.now() How do I declare a timestamp to use in a calculation
port = 0 #needs to be an int
while port <= 65536 : #max 65536
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "....................."
    with open('Results.csv', 'a') as f:
        f.write(t1)
        try:
            s.settimeout(.187) #speeds things up
            s.connect((host,port))
            value = ", %s,%s,OPEN\n" % (host, port)
            v = str(value)
            f.write(v)
            #s.bind((host,port)) for future use to deliver payload
            s.shutdown(2)
            s.close()
            print "!!!!!!!!FOUND ONE!!!!!!!!!"
            port += 1
            continue
        except:
            value =  ", %s,%s,CLOSED\n" % (host, port)
            v = str(value)
            f.write(v)
            port += 1
            print "..CLOSED"
    f.closed

#need to subtract beginning timestamp from this
         
        #step back to port-scan.py
