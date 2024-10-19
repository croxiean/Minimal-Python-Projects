#!/usr/bin/share/env python
# -*- coding: utf-8 -*-

import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("figlet ZAFIYET ANALIZI")

print("""
This tool created by samet TAŞ
croxilex@proton.me
\n
""")

print("Zafiyet analizi programına hoşgeldiniz. \n")
 
target = input("hedef ip gir : ")

os.system("nikto -h " + target)

