import webview
import modelfetch
import json
import os
import psutil
import humanize
import GPUtil
import platform
# import portablemc
from portablemc.standard import Context, Version, Watcher
from pathlib import Path

# https://github.com/mindstorm38/portablemc/blob/main/doc/API.md

# Global variables declaration
global lastaccount, firsttime, lastinstance, maximizedefault, winwidth, winheight
global demomode, multiplayer, gamechat, minmem, maxmem, javapath, jvmargs, customtheme, lastuuid

syshost = modelfetch.system.Model

print(r"""
	      _  _           _                               
         | || |         (_)                              
 ____  __| || | __ _ __  _  _ __ ___   ___   ___   _ __  
|_  / / _` || |/ /| '__|| || '_ ` _ \ / __| / _ \ | '_ \ 
 / / | (_| ||   < | |   | || | | | | |\__ \| (_) || | | |
/___| \__,_||_|\_\|_|   |_||_| |_| |_||___/ \___/ |_| |_|
                                    Beta 1.1 -Launch Update-
                                 	Written by MTSyntho Dev             
                                                         
		""")

# Function to initialize or reset settings
def initialize_settings():
    global lastaccount, firsttime, lastinstance, maximizedefault
    global winwidth, winheight, demomode, multiplayer, gamechat, accounts
    global minmem, maxmem, javapath, jvmargs, customtheme, configjson, lastuuid
    
    config = {
        "lastaccount": "",
        "lastuuid": "",
        "firsttime": 1,
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
        print("Settings File may be missing! `settings.json` has been created.")
        with open(".zdkrimson\\settings.json", "w") as outfile:
            json.dump(config, outfile, indent=2)

    if not os.path.exists(".zdkrimson\\accounts.json"):
        print("Accounts File may be missing! `accounts.json` has been created.")
        with open(".zdkrimson\\accounts.json", "w") as outfile:
            json.dump(accounts, outfile, indent=2)

    if not os.path.exists(".zdkrimson\\instances.json"):
        print("Instances File may be missing! `instances.json` has been created.")
        with open(".zdkrimson\\instances.json", "w") as outfile:
            json.dump(accounts, outfile, indent=2)

    if not os.path.exists(".zdkrimson\\lastinstance.txt"):
        print("Last Open Instance File may be missing! `lastinstance.txt` has been created.")
        with open(".zdkrimson\\lastinstance.txt", 'w') as outfile:
            outfile.write('')


    
    # Loading settings from JSON
    try:
        with open('.zdkrimson\\settings.json', 'r') as openfile:
            configjson = json.load(openfile)
            lastaccount = configjson['lastaccount']
            lastuuid = configjson['lastuuid']
            firsttime = configjson['firsttime']
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
        lastuuid = ""
        firsttime = 1
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

    
    with open('.zdkrimson\\lastinstance.txt', 'r') as openfile:
        global lastinstance
        lastinstance = openfile.read();
        print('Last Instance: ' + lastinstance)



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

    def get_last_account(self):
        return lastaccount

    def save_account_change(self, name, uuid):
        print('Saving Details for Logged In Account.')
        print('Account Name: ' + name)
        print('Account UUID: ' + uuid)
        # my brain hurt

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
        global minmem, maxmem, javapath, jvmargs, customtheme, lastaccount, lastuuid
        
        if name == 'maximizedefault':
            maximizedefault = data
        elif name == 'lastaccount':
            lastaccount = data
        elif name == 'lastuuid':
            lastuuid = data
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
            "lastuuid": lastuuid,
            "firsttime": firsttime,
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

    def get_recentinstance(self):
        print("Last Instance:", lastinstance)
        return lastinstance

    def save_recentinstance(self, name):
        global lastinstance

        lastinstance = name
        with open(".zdkrimson\\lastinstance.txt", 'w') as outfile:
            outfile.write(lastinstance)


    # def offline_account(self, zdoffline):
    #     print('Offline Username: ' + str(zdoffline[0]))
    #     print('Offline UUID: ' + str(zdoffline[1]))
    #     print(zdoffline)

    # chatgtp wrote this function cuz i struggled with appending offline_account, bruh
    def offline_account(self, username, uuid):
        print('Offline Username: ' + username)
        print('Offline UUID: ' + uuid)
        
        offline_account = {
            "username": username,
            "uuid": uuid
        }

        file_path = '.zdkrimson\\accounts.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                try:
                    accountsjson = json.load(openfile)
                    if not isinstance(accountsjson, list):
                        raise ValueError("JSON data is not a list")
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"Error reading JSON file: {e}")
                    accountsjson = []
        else:
            accountsjson = []

        accountsjson.append(offline_account)

        with open(file_path, 'w') as openfile:
            json.dump(accountsjson, openfile, indent=4)

        print("New account has been appended to the file.")

    def get_accounts(self):
        file_path = '.zdkrimson\\accounts.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                return json.load(openfile)
        else:
            print('Cant fetch accounts.json')

    def get_instances(self):
        file_path = '.zdkrimson\\instances.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                return json.load(openfile)
        else:
            print('Cant fetch instances.json')

    def add_instance(self, name, version, icon):
        new_inst = {
            "name": name,
            "version": version,
            "icon": icon
        }
        file_path = '.zdkrimson\\instances.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as openfile:
                try:
                    instancesjson = json.load(openfile)
                    if not isinstance(instancesjson, list):
                        raise ValueError("JSON data is not a list")
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"Error reading JSON file: {e}")
                    instancesjson = []
        else:
            instancesjson = []

        instancesjson.append(new_inst)

        with open(file_path, 'w') as openfile:
            json.dump(instancesjson, openfile, indent=4)

    def launch_minecraft(self, username, uuid, instancename, version, modloader):
        print(f'\nLaunching Minecraft {version} in instance {instancename} with username: {username} (uuid: {uuid})\n')
        mcver = Version(version)
        mccontext = Context(Path(".zdkrimson\\resources"), Path(".zdkrimson\\.minecraft"))

        class MyWatcher(Watcher):
            def handle(self, event) -> None:
                print("Raw PortableMC Log: ", event)

        mcver.set_auth_offline(username, uuid)
        env = mcver.install(watcher=MyWatcher())
        env.run()

        # Big thanks 2 ChatGPT for making the variables work globally throughtout the project, i didnt know how to get it working.

# Instantiate Api class
api = Api()

# Create and start webview window
webview.create_window('zdkrimson', background_color="#210202", url="index.html", js_api=api)
# webview.start()

# Disable this line prior to compiling and use the one prior, please...
webview.start(debug=True)