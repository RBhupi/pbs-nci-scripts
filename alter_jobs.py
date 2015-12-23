#!/usr/bin/python
#quick dirty script to alter project for PBS job.

from popen2 import popen2
import subprocess
import time
from os import getcwd
import os, sys
if (len(sys.argv)<4):
	print("""provide 'start' & 'end' job ids, and 'to' projects for altering the jobs.
		to change to w58 $alter_jobs.py start_id end_id w58""")
	quit()
argv1 =int(sys.argv[1])
argv2 =int(sys.argv[2])+1
argv3 = str(sys.argv[3])
#-------------------------------------------------------------------------
yesno='n'
yesno = raw_input("Type 'YeSs' to change project to " + argv3 +" for job ids " + str(argv1) + "-" + str(argv2) + "\n")

if(yesno!='YeSs'):
    print("Doing nothing.")
    quit()
#-------------------------------------------------------------------------
jobs=0
# Open a pipe to the nqstat command.
output, input = popen2('nqstat')

for id  in range(argv1, argv2):
	print("altering " + str (id))
	delout, delin = popen2('qalter -P '+ argv3 + " " + str(id))
	delin.write(str(id))
	delin.close()
	print(delout.read())
	jobs=jobs+1
print(str(jobs)+" jobs altered. Check status in a minute.")
