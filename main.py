import webview
import modelfetch
import json
import os
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
	    "lastinstance": ""
	}
	configjson = json.dumps(config, indent=2)
	with open(".zdkrimson\\settings.json", "w") as outfile:
	    outfile.write(configjson)
	lastaccount=""													
	firstime=1
	lastinstance=""

if os.path.exists(".zdkrimson\\instances")==False:
	print("instances folder doesn't exist, created one just now.")
	os.mkdir(".zdkrimson\\instances")

# loading json files
with open('.zdkrimson\\settings.json', 'r') as openfile:
	configjson = json.load(openfile)
	try:
		print(configjson['lastaccount'])
		print(configjson['firsttime'])
		print(configjson['lastinstance'])
		lastaccount=configjson['lastaccount']
		firsttime=configjson['firsttime']
		lastinstance=configjson['lastinstance']
		print("imported settings json")
		print(lastaccount)
	except KeyError:
		print("Settings file isn't up-to-date")
		config = {
		    "lastaccount": "",
		    "firsttime": 1,
		    "lastinstance": ""
		}
		configjson = json.dumps(config, indent=2)
		with open(".zdkrimson\\settings.json", "w") as outfile:
		    outfile.write(configjson)
		lastaccount=""
		firstime=1
		lastinstance=""

class Api:
	def get_host(self):
		print(syshost)
		return syshost

	def get_username(self, uuid):
		print(uuid)
		if uuid=='recent':
			return lastaccount

api = Api()
webview.create_window('zdkrimson', background_color="#210202", url="index.html", js_api=api)
webview.start(debug=True)