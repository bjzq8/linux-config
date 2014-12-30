#!/usr/bin/python

#from subprocess import popen
import subprocess
import datetime
import binascii
import MySQLdb
import time
starttime=time.time()

logvar=open('/var/log/sshd_logged','r')

#newlogvar=open('/var/www/html/newlog','w')
inserted=0
notinserted=0
mailtext=[]
charttext=[]

db=MySQLdb.connect("localhost","root","blank","sshd")
cursor=db.cursor()

#for line in logvar:
#	if (line.find("9537.53") != -1
#		):
#		foundline=line.split()
#		print foundline[3]
for line in logvar:
		splitline=line.split('|')
#		print splitline
		lineuuid=splitline[0]
		uuidnodash=lineuuid.translate(None,'-')
#		uuidnodash="0x"+uuidnodash
#		uuidbin=bin(uuidnodash)
		uuidbin=binascii.unhexlify(uuidnodash)
		linedate=splitline[1]
		lineip=splitline[2]
		lineuname=splitline[3]
		linepword=splitline[4]
		linepword=linepword[:-1]
		linepword=linepword.rstrip()
#		print line
#		print uuidnodash,linedate,lineip,lineuname,linepword
#		print uuidnodash

		sql='select username from pwd where uuid=unhex("%s")' % uuidnodash
		cursor.execute(sql)
#		cursor.execute("SELECT username from pwd where uuid=UNHEX('%s')",(uuidnodash))
#		cursor.execute("""SELECT username from pwd where uuid=UNHEX('FFEC5DAAD0944BB7A420EBDB74ECDC46')""")

	        results='None'	
#		print "results=",results
		results=cursor.fetchall()
#	        print "results=",results
		if results==():
#			print"Inserting"
	        	cursor.execute("""INSERT INTO `pwd` (uuid,date,ip,username,pword) VALUES (UNHEX (%s),%s,INET_ATON(%s),%s,%s)""",[uuidnodash,linedate,lineip,lineuname,linepword])
			inserted=inserted+1
		else:
#			print"Not Inserting"
			notinserted=notinserted+1

#               rawline=line.split()
#		dateline=rawline[3]
#		print dateline
#               datetimestring=dateline.split(':')
#		print datetimestring
#		foundhour=datetimestring[1]
#		print foundhour
#		datestring=datetimestring[0]
#		datestring=datestring[1:]
#		print datestring
#		datesplitstring=datestring.split('/')
#		print datesplitstring
#		actualday=datesplitstring[0]
#		print actualday
#		#foundday=foundhour
#		#splitday=foundday.split('/')
#		#actualday=splitday[0]
#		#actualday=actualday[1:]
#		timenow=datetime.datetime.now()
#               hoursplit=timenow.strftime('%H')
#		daysplit=timenow.strftime('%d')
#		print foundhour,hoursplit,actualday,daysplit
#		if foundhour==hoursplit and actualday==daysplit:
#			sendblock=1
#		        mailtext.append("\\n")
#			mailtext.append(line)
db.commit()
print inserted
print notinserted
#if sendblock==1:
#	#subprocess.call("echo '%s' | mailx -s "PING" bjzqtyphoon@gmail.com" % mailtext)
#	subprocess.call("echo -e %s | mailx -s '9537' bjzqtyphoon@gmail.com" % mailtext, shell=True)
endtime=time.time()
totaltime=endtime-starttime
print totaltime
totalops=inserted+notinserted
charttext.append(totalops)
opspersec=totalops/totaltime
charttext.append(opspersec)
totalops="Total ops "+str(totalops)
opspersec=str(opspersec)+" per second"
totaltime=str(totaltime)+" seconds"
print totalops
print opspersec
mailtext.append(totaltime)
#mailtext.append("\n")
mailtext.append(totalops)
#mailtext.append("\n")
mailtext.append(str(inserted)+" inserted")
#mailtext.append("\n")
mailtext.append(str(notinserted)+" skipped")
#mailtext.append("\n")
mailtext.append(opspersec)
#mailtext.append("\n")
timenow=datetime.datetime.now()
timestr=str(timenow)
charttext.insert(0,timestr[11:13])
charttext.insert(0,timestr[:10])
mailtext=str(timenow)+str(mailtext)+"\n"
print mailtext
#subprocess.call("echo -e %s | mailx -s 'sshdreport' bjzqtyphoon@gmail.com" % mailtext, shell=True)
opsfile=open('/var/www/html/sshdops','a')

#chartdata=(charttext[0]+","+str(charttext[1])+","+str(charttext[2])+","+str(charttext[3])+"\n")
chartdata=(str(charttext[2])+","+str(charttext[3])+"\n")


chartfile=open('/var/www/html/chartfile','a')
opsfile.write(str(mailtext))
chartfile.write(str(chartdata))

