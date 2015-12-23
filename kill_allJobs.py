#!/usr/bin/python
#author: Bhupendra Raut
#Kills all the jobs for the given user.

from popen2 import popen2
import subprocess
import time
from os import getcwd
import os, sys


#-------------------------------------------------------------------------
yesno='n'
yesno = raw_input("Type 'n' to do nothing\nOR enter user name to KILL all the jobs.\t")

if(yesno=='n'):
    print("Doing nothing.")
    quit()
#-------------------------------------------------------------------------
jobs=0
# Open a pipe to the nqstat command.
output, input = popen2('nqstat')
for line in iter(output.readline,''):
	index=line.find(yesno)
	if(index>0):
		print("killing ==>" + str(line))
		id=line[0:index-2]
		delout, delin = popen2('qdel ' + str(id))
		#subprocess.call(['qdel ', id], shell=True)
		delin.write(str(id))
		delin.close()
		print(delout.read())
		jobs=jobs+1
print(str(jobs)+" jobs killed for user "+yesno+". Check status in a minute.")
