#! /usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



import pygal


chartfile=open('/var/www/html/chartfile','r')

chartmax=0
chartmin=9999999
slvar=0
dataline=[]
perdata=[]
oprdata=[]
data1=[]
data2=[]
for line in chartfile:
#	print line
	splitlinemax=line.split(',')
#	print splitlinemax[0]
	if splitlinemax[0]>chartmax:
		chartmax=int(splitlinemax[0])
#	print type(splitlinemax)
chartfile.seek(0)	
print

for line in chartfile:
	splitlinemin=line.split(',')
	slvar=int(splitlinemin[0])
#	print splitlinemin[0],chartmin
#	print chartmin
	if slvar<chartmin:
#		print slvar,chartmin
#		print"strange"
		chartmin=slvar
chartfile.seek(0)

for line in chartfile:
	print line
	splitlinevalue=line.split(',')
	datavar=splitlinevalue[0]
	datavar2=splitlinevalue[1]
	
	group=datavar
	group2=datavar2
	data1.append(group)
	data2.append(group2)
	print group


print data1
print data2
#print
#print str(chartmax)+" chartmax"
#print str(chartmin)+" chartmin"

#print type(chartmin)
#print type(chartmax)


plt.plot(data1,data2)
plt.savefig('/var/www/html/myfig')

