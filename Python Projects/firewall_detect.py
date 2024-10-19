#! usr/bin/env/ python
# _*_ coding: utf-8 _*_

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet FIREWALL DETECT")



# functions
def detect():
	site = input("Please enter the target address \n")
	os.system("wafw00f " + site)
	
def firewall_list():
	os.system("wafw00f -l")


#proccess section

print("""WELCOME TO FIREWALL DETECT PROGRAM

1-) firewall lists
2-) firewall detect
3-) exit
""")


choose = int(input("please choose which is your request"))


if(choose == 1):
	firewall_list()
	
	pass
elif(choose == 2):
	detect()
	
	pass
else:
	print("you entered the false  number")
	os.system("python firewall_detect.py")
	pass

	


	 

