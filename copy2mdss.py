#!/usr/bin/python
# @author Bhupendra Raut
#@brief The script submits copyq batch jobs that creates zipped/unzipped tarball named my_subdir.tar.gz, from subdirectory of the input directory, my_subdir/ and copies it into the user's mass storage subdirectory mdss_dir/
#netcp -C -l other=mdss -z -t my_subdir.tar my_subdir/ mass_dir/
#run without options for more info.

import glob, os, sys
from os import getcwd
from popen2 import popen2
import time

#check arguments: city name is folder name, scneario is subfolder 
if(len(sys.argv)<3):
	sys.exit("ERROR: insufficient arguments.\n\t$copy2mdss <city> <scenario>")

city=sys.argv[1]
scenario=sys.argv[2]
root="/g/data3/k10/bar565/h2sim/" #end with "/"

#change to input directory
indir =root+city+"/"+scenario 
os.chdir(indir)
#list subdirectories
dir_list = os.listdir(".")


print("making output directory on mdss")
md_out="CRC-WSC/"+city+"/"+scenario+"/"
output, input = popen2('mdss mkdir -p '+md_out)
print output.read()

print("""Copy Info: \033[1m %s/%s\033[0m  --> on mdss \033[1m %s\033[0m """ % (city, scenario, md_out))


yesno = 'no'
yesno = raw_input("Type 'YeSs' to submit the CDO jobs.\t")
if(yesno != 'YeSs'):
    quit()

for model in dir_list:
	command="netcp -C -l other=mdss -t "+model+".tar ./"+model+"/ "+md_out
	print(command)
	output, input = popen2(command)
	print output.read()
	time.sleep(1.0)
	#quit()
print("Jobs submitted: Check for error.\n")

time.sleep(5.0)
output, input = popen2('nqstat')
print output.read()


