#Script by Sigwo
# 21Jan13
#
#Raw TCP port scanner. You will need the tcp-port-scan.py file in the same 
#directory as this file.

import os

base = 'port-scan'
Series = ['tcp-']
for series in Series:
    ffile = series+base+'.py'
    os.system( ffile )

#Now time to do something with the results in a future release   
#file = open("Results.csv")

#for line in file:
#    pass # do something
