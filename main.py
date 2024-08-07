import webview
import modelfetch
import json
import os
import psutil
import humanize
import GPUtil
import platform
import portablemc

# Note 2 Self (2024/07/09 - 3:40AM (it's my birthday wowzers))
# https://github.com/mindstorm38/portablemc/blob/main/doc/API.md
# I'm adding accounts

# Global variables declaration
global lastaccount, firsttime, lastinstance, maximizedefault, winwidth, winheight
global demomode, multiplayer, gamechat, minmem, maxmem, javapath, jvmargs, customtheme

syshost = modelfetch.system.Model

print(r"""
	      _  _           _                               
         | || |         (_)                              
 ____  __| || | __ _ __  _  _ __ ___   ___   ___   _ __  
|_  / / _` || |/ /| '__|| || '_ ` _ \ / __| / _ \ | '_ \ 
 / / | (_| ||   < | |   | || | | | | |\__ \| (_) || | | |
/___| \__,_||_|\_\|_|   |_||_| |_| |_||___/ \___/ |_| |_|
                                 	Written by MTSyntho & Artsign                  
                                                         
		""")

# Function to initialize or reset settings
def initialize_settings():
    global lastaccount, firsttime, lastinstance, maximizedefault
    global winwidth, winheight, demomode, multiplayer, gamechat, accounts
    global minmem, maxmem, javapath, jvmargs, customtheme, configjson
    
    config = {
        "lastaccount": "",
        "firsttime": 1,
        "lastinstance": "",
        "maximizedefault": False,
        "winwidth": 854,
        "winheight": 480,
        "demomode": False,
        "nomultiplayer": True,
        "nogamechat": True,
        "minmem": 512,
        "maxmem": 1024,
        "javapath": "javaw",
        "jvmargs": "",
        "customtheme": ""
    }

    accounts = {}
    
    # File/Folder Checking
    if not os.path.exists(".zdkrimson"):
        print(".zdkrimson folder doesn't exist, created one just now.")
        os.mkdir(".zdkrimson")

    if not os.path.exists(".zdkrimson\\settings.json"):
        print("settings file(settings.json) doesn't exist, created one just now.")
        with open(".zdkrimson\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)

    if not os.path.exists(".zdkrimson\\accounts.json"):
        print("accounts file(accounts.json) doesn't exist, created one just now.")
        with open(".zdkrimson\\accounts.json", "w") as outfile:
            json.dump(accounts, outfile, indent=2)
    
    # Loading settings from JSON
    try:
        with open('.zdkrimson\\settings.json', 'r') as openfile:
            configjson = json.load(openfile)
            lastaccount = configjson['lastaccount']
            firsttime = configjson['firsttime']
            lastinstance = configjson['lastinstance']
            maximizedefault = configjson['maximizedefault']
            winwidth = configjson['winwidth']
            winheight = configjson['winheight']
            demomode = configjson['demomode']
            nomultiplayer = configjson['multiplayer']
            nogamechat = configjson['gamechat']
            minmem = configjson['minmem']
            maxmem = configjson['maxmem']
            javapath = configjson['javapath']
            jvmargs = configjson['jvmargs']
            customtheme = configjson['customtheme']
            print("Successfully imported 'settings.json'")
            if lastaccount == "":
                print("Last Used Account: Not Logged In!")
            else:
                print("Last Used Account:", lastaccount)
    
    except KeyError:
        print("Settings file isn't up-to-date, settings file should now be updated (info reset)")
        with open(".zdkrimson\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)
        # Initialize global variables after resetting settings
        lastaccount = ""
        firsttime = 1
        lastinstance = ""
        maximizedefault = False
        winwidth = 854
        winheight = 480
        demomode = False
        nomultiplayer = True
        nogamechat = True
        minmem = 512
        maxmem = 1024
        javapath = "javaw"
        jvmargs = ""
        customtheme = ""

# Initialize or reset settings
initialize_settings()

class Api:
    def get_host(self):
        print("System Host:", syshost)
        return syshost

    def get_username(self, uuid):
        print("Account UUID:", uuid)
        if uuid == 'recent':
            return lastaccount

    def get_recentinstance(self):
        print("Last Instance:", lastinstance)
        return lastinstance

    def get_settings(self):
        return configjson

    def get_mem(self):
        print("Total RAM:", psutil.virtual_memory().total)
        print("Formatted RAM:", humanize.naturalsize(psutil.virtual_memory().total))
        return humanize.naturalsize(psutil.virtual_memory().total)

    def get_gpu(self):
        gpus = GPUtil.getGPUs()
        if not gpus:
            print('No GPUs Detected.')
            return 'No Dedicated GPUs Found'
        else:
            print('GPU:', gpus[0].name)
            return gpus[0].name

    def get_cpu(self):
        cpu_info = platform.uname()
        print('CPU:', cpu_info.processor)
        return cpu_info.processor

    def write_settings(self, name, data):
        global maximizedefault, winwidth, winheight, demomode, multiplayer, gamechat
        global minmem, maxmem, javapath, jvmargs, customtheme
        
        if name == 'maximizedefault':
            maximizedefault = data
        elif name == 'demomode':
            demomode = data
        elif name == 'multiplayer':
            multiplayer = data
        elif name == 'gamechat':
            gamechat = data
        elif name == 'customtheme':
            customtheme = data
        elif name == 'javapath':
            javapath = data
        elif name == 'jvmargs':
            jvmargs = data
        elif name == 'minmem':
            minmem = data
        elif name == 'maxmem':
            maxmem = data
        elif name == 'winwidth':
            winwidth = data
        elif name == 'winheight':
            winheight = data
        print('Loading Settings')

    def save_settings(self):
        print('Saving Settings')
        config = {
            "lastaccount": lastaccount,
            "firsttime": firsttime,
            "lastinstance": lastinstance,
            "maximizedefault": maximizedefault,
            "winwidth": winwidth,
            "winheight": winheight,
            "demomode": demomode,
            "multiplayer": multiplayer,
            "gamechat": gamechat,
            "minmem": minmem,
            "maxmem": maxmem,
            "javapath": javapath,
            "jvmargs": jvmargs,
            "customtheme": customtheme
        }
        print(config)
        with open(".zdkrimson\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)
        print("'settings.json' Saved Successfully")
        return "'settings.json' Saved Successfully"

    # def save_offlineaccount(self, username, uuid):
    # 	pr

        # Big thanks 2 ChatGPT for making the variables work globally throughtout the project, i didnt know how to get it working.

# Instantiate Api class
api = Api()

# Create and start webview window
webview.create_window('zdkrimson', background_color="#210202", url="index.html", js_api=api)
webview.start(debug=True)