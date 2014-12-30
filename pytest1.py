#! /usr/bin/python

import pygal

line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
#line_chart.x_labels = map(str, range(2002, 2013))
#line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])

chartfile=open('/var/www/html/chart','r')

chartmax=0
chartmin=9999999
slvar=0
dataline=[]
perdata=[]
oprdata=[]
data1=[]

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
	splitlinevalue=line.split(',')
	datavar=int(splitlinevalue[0])
	datavar2=int(splitlinevalue[1])
	
	group=(datavar,datavar2)
	data1.append(group)
#	print group


print data1

#print
#print str(chartmax)+" chartmax"
#print str(chartmin)+" chartmin"

#print type(chartmin)
#print type(chartmax)

#line_chart.y_labels=['1000','2000','3000','4000','5000','6000','7000','8000']
line_chart.x_labels=['2000','3000','4000']

#line_chart.add('data',data1)

#line_chart.render()
line_chart.render_to_file('/var/www/html/chart.svg')

#bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file
