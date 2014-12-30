#!/usr/bin/python

logvar=open('/var/log/httpd/access_log','r')

newlogvar=open('/var/www/html/newlog','w')

for line in logvar:
	if (line.find("bot") == -1
	    and line.find("bc4.cat.com") == -1
	    and line.find("XT1055") == -1
	    and line.find("dd-wrt") == -1
	    and line.find("favicon") == -1
	    and line.find("192.168.0.") == -1
	    and line.find("Baidu") == -1
            and line.find("baidu") == -1
            and line.find("crawler") == -1
            and line.find("scanner") == -1
	    and line.find("dummy") == -1
	    and line.find("404 2") == -1
            and line.find("MSIE") == -1
	    and line.find("x80w") == -1
            and line.find("NerdyBot") == -1
	    and line.find("84.76.215") == -1
	    and line.find("177.68.67") == -1
	    and line.find("192.189.128") == -1
	    and line.find("186.66.67") == -1
	    and line.find("87.25.142") == -1
	    and line.find("180.247.15") == -1
	    and line.find("189.48.168") == -1
	    and line.find("189.81.235") == -1
	    and line.find("189.81.225") == -1
	    and line.find("compute-1.amazonaws.com") == -1
	    and line.find("162.253.66.77") == -1
	    and line.find("win8 - -") == -1
	    and line.find("poneytelecom.eu") == -1
	    and line.find("cianetwork") == -1
	    and line.find("claro.net") == -1
            and line.find("unit-is") == -1
	    and line.find("cnsat.com.cn") == -1
	    and line.find("bc5.cat.com") == -1
            and line.find("veloxzone.com.br") == -1
	    and line.find("virtua.com.br") == -1
	    and line.find("solidseo") == -1
	    and line.find("proxy-us.01") == -1
	    and line.find("drakon.bsd") == -1
	    and line.find("Gecko/2010") == -1
 	    and line.find("29-Headache") == -1
	    and line.find("laajakaista") == -1
	    and line.find(".arm") == -1
	    and line.find("Macintosh") == -1
	    and line.find("mikrocom.sk") == -1
            and line.find("ecatel.net") == -1
	    and line.find("nXSUCCESS") == -1
	    and line.find("bezeqint") == -1
	    and line.find("slurp") == -1
		):
		newlogvar.write(line)
#		newlogvar.write('\n')

