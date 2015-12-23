#!/usr/bin/python
# author: Bhupendra Raut
#Kill PBS jobs for all the jobs in the range of id.

from popen2 import popen2
import subprocess
import time
from os import getcwd
import os, sys
if (len(sys.argv)<3):
	print("provide 'start' and 'end' ids for killing the jobs")
	quit()
argv1=int(sys.argv[1])
argv2=int(sys.argv[2])+1
#-------------------------------------------------------------------------
yesno='n'
yesno = raw_input("Type 'YeSs' to KILL all the jobs with id. " + str(argv1) + "-" + str(argv2) + "\n")

if(yesno!='YeSs'):
    print("Doing nothing.")
    quit()
#-------------------------------------------------------------------------
jobs=0
# Open a pipe to the nqstat command.
output, input = popen2('nqstat')
for id  in range(argv1, argv2):
	print("killing " + str (id))
	delout, delin = popen2('qdel ' + str(id))
	delin.write(str(id))
	delin.close()
	print(delout.read())
	jobs=jobs+1
print(str(jobs)+" jobs killed. Check status in a minute.")
