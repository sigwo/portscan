#! /usr/bin/env python
#
# Python Script by Steven Grove (@sigwo)
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
# Date: 09-01-13
#
# Scans subnet.
#
# make the output go to file and pull that file into a GUI, load new window if payload is
# started, make a well known port scanner and complete port scanner, make an IP range selector
#
import datetime
import socket
import sys

# Get address string and CIDR string from command line
xaddr = raw_input("IP address: ")
xcidr = raw_input("CIDR notation, NO / mark!: ")
while xcidr < 16:
	xcidr = raw_input("Please try again. Subnets must be longer than /16. NO / mark!: ")
continue
addr = xaddr.split('.')
cidr = int(xcidr)

# Initialize the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(cidr):
    mask[i/8] = mask[i/8] + (1 << (7 - i % 8))

# Initialize net and binary and netmask with addr to get network
net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])

# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
    broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))
	
# Timestamp for future use in storing results
timestart = datetime.datetime.now()
t1 = str(timestart)

# Cleaning up the raw output from net and broad from above
anet = net , ".".join(map(str, net))
abroad = broad , ".".join(map(str, broad))

# Start scanning network based upon input and calculations from above
while anet < abroad: 
	s = socket.getprotobyname('icmp')
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, 'anet')
	with open('results.csv', 'a') as f:
		f.write(t1)
		try:
			s.settimeout(.007) #speeds things up
			s.connect((anet))
			value = ", %s,OPEN\n" % (anet)
			v = int(value)
			f.write(v)
			s.shutdown(2)
			s.close()
			print "!!!!!!!!FOUND ONE!!!!!!!!!"
			print '\a' # beeps on open port
			anet += 1
			continue
		except:
			value =  ", %s,CLOSED\n" % (anet)
			v = int(value)
			f.write(v)
			anet += 1
			print "..CLOSED"
	f.closed
