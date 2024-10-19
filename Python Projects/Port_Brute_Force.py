# usr/bin/env python
# _*_ coding: utf-8 _*_

import os

os.system("apt install figlet")
os.system("clear")
os.system("PORT BRUTE FORCE")


print("""
welcome to brute-force program
please select your target port 

1-) FTP
2-) SSH
3-) TELNET
4-) HTTP
5-) SMB
6-) RDP
7-) VNC
8-) SIP
9-) REDIS
10-) PostgreSQL

""")

proccess = int(input("select your target port")
terget_ip = input("please enter your ip")
username  = input("please enter your username list pathway")
password = input("please enter your password list pathway")



#ftp
if(proccess == 1):
	os.system("ncrack -p 21 -U" + username + " -P " + password + " " + target_ip)
#ssh	
elif(proccess == 2):
	os.system("ncrack -p 22 -U" + username + " -P " + password + " " + target_ip)

#telnet	
elif(proccess == 3):
	os.system("ncrack -p 23 -U" + username + " -P " + password + " " + target_ip)
	
#http	
elif(proccess == 4):
	os.system("ncrack -p 80 -U" + username + " -P " + password + " " + target_ip)

#smb	
elif(proccess == 5):
	os.system("ncrack -p 139 -U" + username + " -P " + password + " " + target_ip)
	
#rdp	
elif(proccess == 6):
	os.system("ncrack -p 3389 -U" + username + " -P " + password + " " + target_ip)
	
#vnc
elif(proccess == 7):
	os.system("ncrack -p 5900 -U" + username + " -P " + password + " " + target_ip)
	
#sıp
elif(proccess == 8):
	os.system("ncrack -p 5060 -U" + username + " -P " + password + " " + target_ip)
	
#redıs
elif(proccess == 9):
	os.system("ncrack -p 6379 -U" + username + " -P " + password + " " + target_ip)

# postgresql
elif(proccess == 10):
	os.system("ncrack -p 5432 -U" + username + " -P " + password + " " + target_ip)


	
