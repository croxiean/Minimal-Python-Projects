#! usr/bin/env python
# _*_ coding: utf-8 _*_



import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet MAC CHANGER")

print("""
1-) MAC Adress 'Random'
2-) MAC Adress 'manuel'
3-) MAC -> original address
""")

request = int(input("enter your request"))

if(request == 1):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mNew MAC is ready !")
	pass
	
elif(request == 2):
	print("\033[91m attention! if you dont have information about the MAC Adress please dont use this seciton.")
	NewMac = input("\033[92menter your new mac : ")
	 
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + NewMac + " eth0") 
	os.system("ifconfig eth0 up")
	print("\033[92mNew MAC is ready !")
	pass
if(request == 3):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth up")
	print("\033[92mYour  MAC have returned to original !")
	pass
	
	
	
	

	
	
