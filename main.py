import webview
import modelfetch
import json
import os
import psutil
import humanize
import GPUtil
import platform
from os import path

syshost=modelfetch.system.Model

print(r"""
	      _  _           _                               
         | || |         (_)                              
 ____  __| || | __ _ __  _  _ __ ___   ___   ___   _ __  
|_  / / _` || |/ /| '__|| || '_ ` _ \ / __| / _ \ | '_ \ 
 / / | (_| ||   < | |   | || | | | | |\__ \| (_) || | | |
/___| \__,_||_|\_\|_|   |_||_| |_| |_||___/ \___/ |_| |_|
                                 	Written by MTSyntho & Artsign                  
                                                         
		""")

# File/Folder Checking
if os.path.exists(".zdkrimson")==False:
	print(".zdkrimson folder doesn't exist, created one just now.")
	os.mkdir(".zdkrimson")

if os.path.exists(".zdkrimson\\settings.json")==False:
	print("settings file(settings.json) doesn't exist, created one just now.")
	config = {
	    "lastaccount": "",
	    "firsttime": 1,
	    "lastinstance": "",
	    "maximizedefault": False,
	    "winwidth": 854,
	    "winheight": 480,
	    "demomode": False,
	    "multiplayer": True,
	    "gamechat": True,
	    "minmem": 512,
	    "maxmem": 1024,
	    "javapath": "javaw",
	    "jvmargs": "",
	    "customtheme": ""
	}
	configjson = json.dumps(config, indent=2)
	with open(".zdkrimson\\settings.json", "w") as outfile:
	    outfile.write(configjson)
	lastaccount=""													
	firstime=1
	lastinstance=""
	maximizedefault=False
	winwidth=854
	winheight=480
	demomode=False
	multiplayer=True
	gamechat=True
	minmem=512
	maxmem=1024
	javapath="javaw" # a command gets executed instead assuming java's installed already
	jvmargs=""
	customtheme="" # themes aren't implemented yet, but i added this option anyway :p

if os.path.exists(".zdkrimson\\instances")==False:
	print("Instances Folder is missing! Folder has been created for you")
	os.mkdir(".zdkrimson\\instances")

# loading json files
with open('.zdkrimson\\settings.json', 'r') as openfile:
	configjson = json.load(openfile)
	try:
		lastaccount=configjson['lastaccount']
		firsttime=configjson['firsttime']
		lastinstance=configjson['lastinstance']
		maximizedefault=configjson['maximizedefault']
		winwidth=configjson['winwidth']
		winheight=configjson['winheight']
		demomode=configjson['demomode']
		multiplayer=configjson['multiplayer']
		gamechat=configjson['gamechat']
		minmem=configjson['minmem']
		maxmem=configjson['maxmem']
		javapath=configjson['javapath']
		jvmargs=configjson['jvmargs']
		customtheme=configjson['customtheme']
		# print(configjson)
		print("Successfully imported 'settings.json'")
		if lastaccount=="":
			print("Last Used Account: Not Logged In!")
		else:
			print("Last Used Account:" + lastaccount)
	except KeyError:
		print("Settings file isn't up-to-date, settings file should now be updated (info reset)")
		config = {
		    "lastaccount": "",
		    "firsttime": 1,
		    "lastinstance": "",
		    "maximizedefault": False,
		    "winwidth": 854,
		    "winheight": 480,
		    "demomode": False,
		    "multiplayer": True,
		    "gamechat": True,
		    "minmem": 512,
		    "maxmem": 1024,
		    "javapath": "javaw",
		    "jvmargs": "",
		    "customtheme": ""
		}
		configjson = json.dumps(config, indent=2)
		with open(".zdkrimson\\settings.json", "w") as outfile:
		    outfile.write(configjson)
		lastaccount=""													
		firstime=1
		lastinstance=""
		maximizedefault=False
		winwidth=854
		winheight=480
		demomode=False
		multiplayer=True
		gamechat=True
		minmem=512
		maxmem=1024
		javapath="javaw" # a command gets executed instead assuming java's installed already
		jvmargs=""
		customtheme="" # themes aren't implemented yet, but i added this option anyway :p

class Api:
	def get_host(self):
		print("System Host: " + syshost)
		return syshost

	def get_username(self, uuid):
		print("Account UUID: " + uuid)
		if uuid=='recent':
			return lastaccount

	def get_recentinstance(self):
		print("Last Instance: " + lastinstance)
		return lastinstance

	def get_settings(self):
		return configjson

	def get_mem(self):
		# print('RAM: ' + psutil.virtual_memory().total)
		print(psutil.virtual_memory().total)
		print(humanize.naturalsize(psutil.virtual_memory().total))
		return humanize.naturalsize(psutil.virtual_memory().total)

	def get_gpu(self):
		gpus = GPUtil.getGPUs()
		if not gpus:
			print('No GPUs Detected.')
			return 'No Dedicated GPUs Found'
		else:
			print('GPU: ' + gpus.name)
			return gpus.name

	def get_cpu(self):
		cpu_info = platform.uname()
		print('CPU: ' + cpu_info.processor)
		return cpu_info.processor
api = Api()
webview.create_window('zdkrimson', background_color="#210202", url="index.html", js_api=api)
webview.start(debug=True)