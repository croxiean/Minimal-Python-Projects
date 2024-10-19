#!/usr/bin/share/env python
# -*- coding: utf-8 -*-

import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("figlet VPN KONTROL")

print("""
This tool created by samet TAŞ
croxilex@proton.me
\n
""")

print("VPN kontrol sistemine hoşgeldiniz.")

target = input("ip adresiniz : ")


for i in range(3):
	if(i<3):
		print("taranıyor.")
		time.sleep(1)
		pass
	elif(i == 3):
		print("tarandı ! sonuc ; ")
		pass
		



os.system("ike-scan " + target + "\n")

print("\n sonuclar hakkında bilgi sahibi değilseniz lütfen verilen bağlantıya giderek sonuçlarınızı analiz ediniz. \n")
print("https://kernelblog.org/2020/12/ike_scan-nedir/")
