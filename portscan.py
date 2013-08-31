#!/usr/bin/env python
#
# Raw TCP Port Scanner - Beta
# 
# Script by Steven Grove (@sigwo)
#           www.sigwo.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# 21Jan13 - Initial version
# 09Mar13 - Added RPi compatibility. Renamed "Results.csv" to "results.csv"
#
# Raw TCP port scanner.
#
#
# make the output go to file and pull that file into a GUI, load new window if payload is
# started, make a well known port scanner and complete port scanner, make an IP range selector
#
import datetime
import socket
import sys
#import subprocess
#step in from port-scan.py
host = raw_input("Please put in IP address: ")
timestart = datetime.datetime.today() #time the script started
t1 = str(timestart)
port = 0 #needs to be an int
while port <= 1024 : #max 65536
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "....................."
    with open('results.csv', 'a') as f:
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
#step back to port-scan.py
