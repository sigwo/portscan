#!/usr/bin/env python
#
# Raw TCP Port Scanner - v0.3 Beta
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
# 20Nov13 - Added sound beep on confirmed port open
#
# Raw TCP port scanner.
#
# What I'm working on...
# make the output file (results.csv), load results for eventual payload delivery
# make a well known port scanner and complete port scanner, make an IP range selector
#
import datetime
import socket
import sys

host = raw_input("Please put in IP address or domain name: ")
timestart = datetime.datetime.today() #time the script started
t1 = str(timestart)
port = 0 #needs to be an int

while port <= 65536 : #max 65536
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "....................."
    with open('results.csv', 'a') as f:
        f.write(t1)
        try:
			s.settimeout(.1) #speeds things up
			s.connect((host,port))
			value = ", %s,%s,OPEN\n" % (host, port)
			v = str(value)
			f.write(v)
			s.shutdown(2)
			s.close()
			print "!!!!!!!!FOUND ONE!!!!!!!!!"
			print '\a' # beeps on open port
			port += 1
			continue
        except:
            value =  ", %s,%s,CLOSED\n" % (host, port)
            v = str(value)
            f.write(v)
            port += 1
            print "..CLOSED"
    f.closed
