#!/usr/bin/python

#from subprocess import popen
import subprocess
import datetime

logvar=open('/var/log/httpd/access_log','r')

#newlogvar=open('/var/www/html/newlog','w')

#for line in logvar:
#	if (line.find("9537.53") != -1
#		):
#		foundline=line.split()
#		print foundline[3]
mailtext=[]
sendblock=0
#mailtext=""
for line in logvar:
	if (line.find("9537.53") != -1
		):
                rawline=line.split()
		dateline=rawline[3]
#		print dateline
		datetimestring=dateline.split(':')
#		print datetimestring
		foundhour=datetimestring[1]
#		print foundhour
		datestring=datetimestring[0]
		datestring=datestring[1:]
#		print datestring
		datesplitstring=datestring.split('/')
#		print datesplitstring
		actualday=datesplitstring[0]
#		print actualday
		#foundday=foundhour
		#splitday=foundday.split('/')
		#actualday=splitday[0]
		#actualday=actualday[1:]
		timenow=datetime.datetime.now()
                hoursplit=timenow.strftime('%H')
		daysplit=timenow.strftime('%d')
		print foundhour,hoursplit,actualday,daysplit
		if foundhour==hoursplit and actualday==daysplit:
			sendblock=1
		        mailtext.append("\\n")
			mailtext.append(line)

if sendblock==1:
	#subprocess.call("echo '%s' | mailx -s "PING" bjzqtyphoon@gmail.com" % mailtext)
	subprocess.call("echo -e %s | mailx -s '9537' bjzqtyphoon@gmail.com" % mailtext, shell=True)
