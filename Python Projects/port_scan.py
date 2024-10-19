#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket


os.system("apt install figlet") # figlet aracını indirdim
os.system("clear")
os.system("figlet PORT SCAN")

print("""created by samet taş
croxilex@proton.me
""")

host = socket.gethostname()
ip_address = socket.gethostbyname(host)
print("ip : " + ip_address)



print("""
Port tarama programına hoşgeldiniz.

1-) Hızlı tarama
2-) Servis ve Versiyon Bilgisi
3-) işletim sistemi bilgisi

""")

while True:
	print("sistemden çıkış için '4' e bas.")
	islem = int(input("yapmak istediğin işlem numarasını seçer misin. :)"))

	if (islem ==  1):
		target_ip = input("hedef ip nedir ? ")
		os.system("nmap " + target_ip)
		pass
	elif (islem == 2):
		target_ip = input("hedef ip nedir ? ")
		os.system("nmap -sS -sV " + target_ip)
		pass
	elif(islem == 3):
		target_ip = input("hedef ip nedir ? ")
		os.system("nmap -O " + target_ip)
		pass
	elif(islem == 4):
		print("sistemden çıkılıyor.")
		break
		
	else:
		print("eksik veya hatalı tuşlama yaptın. Lütfen tekrar dene.")
	


	
	


