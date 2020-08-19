#!usr/bin/python

import os 
import sys
import lib
from lib.core import ArgumentParser
from lib.controller import *
from lib.output import *

li = 25 * '-'

TARGET = sys.argv[1]
 

USAGE = '[*] python AuT0Enum.py <all/dir/service/smtp/smb> <ip> '


def service_scan():
	print li

	if len(sys.argv) != 2:
		print USAGE
	else:
		os.system('nmap -sV -sC -oN n1.txt' + TARGET)
		

service_scan()

class Program(object):
    def __init__(self):
        self.script_path = os.path.dirname(os.path.realpath(__file__))
        
        self.arguments = ArgumentParser(self.script_path)
        
        if self.arguments.clean_view:
            self.output = PrintOutput()
        else:
            self.output = CLIOutput()
            
        self.controller = Controller(self.script_path, self.arguments, self.output)


if __name__ == "__main__":
    main = Program()

########################### phesdo #################################################
##lineout = 25 * '-'

##print 'Running nmap script/service scan'
##print lineout
##os.system('mkdir nmap && cd nmap && nmap -sV -sC ' + sys.argv[1] + ' > nmapscan.txt')##
##os.system('cd nmap && cat nmapscan.txt | grep open')##
##print lineout##
##print "Scan completed - saved as nmapscan.txt"##
##print lineout##
##print 'Running dirb scan'
##print lineout
###os.system('mkdir dirb && cd dirb && dirb https://' + sys.argv[1] + ' > dirbscan.txt')
##print lineout
##print 'Scan completed - saved as dirbscan.txt'
##print lineout
##os.system('mkdir dirsearch && python3 dirsearch.py -u http://' + sys.argv[1] + ' -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -E > dirsearch/dirsearch-res.txt')
#os.system('cd dirsearch && cat dirsearch-res.txt | grep 200')
##rint lineout