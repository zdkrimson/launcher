import subprocess
import customtkinter
from nicegui import ui
import os
from threading import Timer
from os import path
import pyngrok
import json
import requests
import shutil
import schedule
import errno
from subprocess import Popen
from PIL import Image
from tkinter import messagebox

# Themes
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("krimson.json")  # Themes: "blue" (standard), "green", "dark-blue"
ui.query('body').style('background-color: #630000')
ui.colors(primary='#bf3a3a')

# check if portablemc module is installed, if not install it
try:
	import portablemc
except ModuleNotFoundError as e:
	def dlmodule(): 
		def checkmodule():
			try:
				import portablemc
				print("works!")
				messagebox.showinfo("Module Installed", "The 'portablemc' Module has successfully been installed!!!\nzdkrimson will now launch.\nIf Minecraft doesn't launch try 'pip freeze' in your terminal and look for 'portablemc' in the list of installed Python modules, if it isn't then try 'pip install portablemc' in your terminal.\nzdkrimson will now close so you may reopen it if you'd like.")
				nomod.destroy()
			except ModuleNotFoundError as e:
				print("Retrying in 3 seconds...")
				Timer(3, checkmodule).start()
		subprocess.Popen("pip install portablemc")
		nmtitle.configure(text="\n\nInstalling...")
		nmmsg.configure(text="\n\n'portablemc' Module is being installed...\nPlease Wait")
		nmbtn.pack_forget()
		checkmodule()

	print("Missing Module! 'portablemc' Module is missing!")
	
	nomod = customtkinter.CTk()
	nomod.geometry("700x600")
	nomod.title("zdkrimson : Minecraft Launcher - Required Module not Installed!")
	nomod.iconbitmap("zdicon.ico")
	mainframen = customtkinter.CTkFrame(master=nomod, fg_color="#3D0A11")
	mainframen.pack(pady=0, padx=0, fill="both", expand=True)

	nmtitle = customtkinter.CTkLabel(master=mainframen, text="\n\nOh No!")
	nmtitle.pack(pady=0, padx=0)

	nmframe = customtkinter.CTkFrame(master=mainframen, fg_color="#630000")
	nmframe.pack(pady=20, padx=40, fill="both", expand=True)
 
	nmmsg = customtkinter.CTkLabel(master=nmframe, text="\n\nThe 'portablemc' Module has not been found\non your system!")
	nmmsg.pack(pady=0, padx=0)

	nmbtn = customtkinter.CTkButton(master=nmframe, text="Install Module (Requires Python Installed!)", command=dlmodule)
	nmbtn.pack(padx=20, pady=10)

	nomod.mainloop()

	



print(r"""
	      _  _           _                               
         | || |         (_)                              
 ____  __| || | __ _ __  _  _ __ ___   ___   ___   _ __  
|_  / / _` || |/ /| '__|| || '_ ` _ \ / __| / _ \ | '_ \ 
 / / | (_| ||   < | |   | || | | | | |\__ \| (_) || | | |
/___| \__,_||_|\_\|_|   |_||_| |_| |_||___/ \___/ |_| |_|
                                 	Written by ItsIceCreeperPE Dev & Artsign                  
                                                         
		""")

appdata=path.expandvars(r'%APPDATA%')
print("{}\\.minecraft".format(appdata))
authtype=0
CDDIR=os.getcwd()
global lastcrack
global firstime
global __version__
lastcrack=""
firstime=0
__version__="alpha5"
instances=[]
print(CDDIR)
global zdusername
global zdemail
global zduuid
zdusername=""
zdemail=""
zduuid=""

# File/Folder Checking
if os.path.exists(".zdkrimson")==False:
	print(".zdkrimson folder doesn't exist, created one just now.")
	os.mkdir(".zdkrimson")

if os.path.exists(".zdkrimson\\crackedusers")==False:
	print("crackedusers folder doesn't exist, created one just now.")
	os.mkdir("{}\\.zdkrimson\\crackedusers".format(CDDIR))

if os.path.exists(".zdkrimson\\settings.json")==False:
	print("settings file(settings.json) doesn't exist, created one just now.")
	config = {
	    "lastcrack": "",
	    "firsttime": 1,
	    "lastinstance": ""
	}
	configjson = json.dumps(config, indent=2)
	with open(".zdkrimson\\settings.json", "w") as outfile:
	    outfile.write(configjson)
	lastcrack=""													
	firstime=1
	lastinstance=""

if os.path.exists(".zdkrimson\\instances")==False:
	print("instances folder doesn't exist, created one just now.")
	os.mkdir(".zdkrimson\\instances")

# loading json files
with open('.zdkrimson\\settings.json', 'r') as openfile:
	configjson = json.load(openfile)
	try:
		print(configjson['lastcrack'])
		print(configjson['firsttime'])
		print(configjson['lastinstance'])
		lastcrack=configjson['lastcrack']
		firsttime=configjson['firsttime']
		lastinstance=configjson['lastinstance']
		print("imported settings json")
		print(lastcrack)
	except KeyError:
		print("Settings file isn't up-to-date")
		config = {
		    "lastcrack": "",
		    "firsttime": 1,
		    "lastinstance": ""
		}
		configjson = json.dumps(config, indent=2)
		with open(".zdkrimson\\settings.json", "w") as outfile:
		    outfile.write(configjson)
		lastcrack=""
		firstime=1
		lastinstance=""

splash = customtkinter.CTk()
splash.title("zdkrimson : Minecraft Launcher - Starting")
splash.geometry("350x262")
splash.overrideredirect(True)
splash.eval('tk::PlaceWindow . center')

splashScreen = customtkinter.CTkImage(dark_image=Image.open("assets/splashScreen.png"), size=(350, 262))

splashimg = customtkinter.CTkLabel(master=splash, text="", image=splashScreen, justify=customtkinter.LEFT)
splashimg.pack(side=customtkinter.LEFT, pady=0, padx=0)

@ui.page('/home')
def main_win():
	splash.destroy()

	# image loading
	crim1 = "assets/bg/blur/crim1.png"
	whitelogoshaded = "assets/logo/image/shaded/white.png"
	whitetextshaded = "assets/logo/full/white.png"
	amlshaded = "assets/logo/sub/shaded/white.png"

	def move_app(e):
		app.geometry(f'+{e.x_root}+{e.y_root}')

	def quit():
		app.quit()	

	def download():
		minecraft_directory = str(path.get())
		print(str(path.get()))
		minecraft_launcher_lib.install.install_minecraft_version(version.get(), minecraft_directory)

	def play():
		print("text")

	@ui.page('/login')
	def loginscrn():
		def selectedauth(value):
			if value=="Microsoft":
				usermaills.configure(placeholder_text="E-Mail")
				authtype="Microsoft"
				print(authtype)
				uuidls.pack_forget()
			else:
				usermaills.configure(placeholder_text="Username")
				uuidls.pack_forget()

			if value=="Cracked/Offline Mode":
				authtype="Cracked/Offline Mode"
				print(authtype)
				logls.pack_forget()
				uuidls.pack(pady=10, padx=10)
				logls.pack(padx=20, pady=0)

		def login():
			zdusername=userls
			zdemail=maills
			zduuid=uuidls
			zdoption=authtypeop
			print(zdusername)
			print(zdemail)
			print(zduuid)
			print(zdoption)
#			print(authtype)
#			print(authtypeop)
			if zdoption=="Microsoft":
				with ui.dialog() as dialog, ui.card():
				    ui.markdown('**Notice!**')
				    ui.label("The Application will stop responding until the authentication as been completed.\nThe Authentication page should open in your default browser.\nClick 'OK' to continue the authentication process.\nClick 'Escape' on your keyboard to cancel.")
				    ui.button('OK', on_click=dialog.close)
				dialog.open()
				loginprocms=subprocess.call("{}\\portablemc login -m {}".format(CDDIR, zdemail))
				print(loginprocms)
				if loginprocms==14:
					ui.notify("Your Microsoft account doesn't have a legitmate copy of Minecraft.", closeBtn="OK")
				else:
					ui.notify("You own Minecraft, you are logged in!", closeBtn="OK")
					user = {
					    "name": "{}".format(zdemail),
					    "uuid": "microsoft"
					}
					jsonfilezd = json.dumps(user, indent=2)
					with open(".zdkrimson\\crackedusers\\{}.json".format(zdemail), "w") as outfile:
	   					outfile.write(jsonfilezd)
					cadb = open(".zdkrimson\\crackedusers\\crackaccount.txt", "a")
					print(cadb)
					cadb.write("{}\n".format(zdemail))
					cadb.close()
			elif zdoption=="Cracked/Offline Mode":
#				loginprocco=subprocess.call("{}\\portablemc -u {} -u {}".format(CDDIR, zdemail, zduuid))
				lastcrack=zdusername
				user = {
				    "name": "{}".format(zdusername),
				    "uuid": "{}".format(zduuid)
				}
				jsonfilezd = json.dumps(user, indent=2)
				with open(".zdkrimson\\crackedusers\\{}.json".format(zdusername), "w") as outfile:
   					outfile.write(jsonfilezd)
				ui.notify("You are logged in as {} as a Cracked/Offline Mode Player.".format(zdusername), closeBtn="OK")
				cadb = open(".zdkrimson\\crackedusers\\crackaccount.txt", "a")
				print(cadb)
				cadb.write("{}\n".format(zdusername))
				cadb.close()

		ui.query('body').style('background-color: #630000')
		ui.colors(primary='#bf3a3a')

#		logscrnwin = customtkinter.CTk()
#		logscrnwin.geometry("400x500")
#		logscrnwin.title("zdkrimson : Minecraft Launcher - Login")

		ui.markdown('\n\n**Login**\n')

#		authtypeop = customtkinter.CTkOptionMenu(logframls, values=["Microsoft", "Cracked/Offline Mode"], command=selectedauth)
#		authtypeop.pack(pady=10, padx=10)
#		authtypeop.set("None Selected :|")

		authtypeop = ui.select({1: 'Microsoft', 2: 'Cracked/Offline Mode'})

		userls = ui.input(label='Username', placeholder='Enter in a Username',
    		    validation={'Username Longer than Minecraft Supports, May cause problems!': lambda value: len(value) < 16})

		maills = ui.input(label='E-Mail', placeholder='Enter your E-Mail, it must own a legitmate copy of Minecraft')

		uuidls = ui.input(label='UUID (Optional)', placeholder='Player UUID')

		ui.button('Login', on_click=login)

	@ui.page('/settings')
	def settings():
		def userchange(value):
			print(value)
			lastcrack=(value)
			print(lastcrack)
			config = {
			    "lastcrack": "{}".format(value),
			    "firsttime": "{}".format(firsttime),
			    "lastinstance": "{}".format(firsttime)
			}
			configjson = json.dumps(config, indent=2)
			with open(".zdkrimson\\settings.json", "w") as outfile:
			    outfile.write(configjson)

		if os.path.exists(".zdkrimson\\crackedusers\\crackaccount.txt")==True:
			cadb = open(".zdkrimson\\crackedusers\\crackaccount.txt", "r")
			rcadb = cadb.readlines()
			print(rcadb)

		with open('.zdkrimson\\settings.json', 'r') as openfile:
			configjson = json.load(openfile)
			print(configjson['lastcrack'])
			lastcrack=configjson['lastcrack']
			
#		settingswin = customtkinter.CTk()
#		settingswin.geometry("400x500")
#		settingswin.title("zdkrimson : Minecraft Launcher - Settings")

		ui.markdown('\n\nSettings\n')

		ui.label('\nUsers\n')

		ui.select(options=rcadb, with_input=True,
			on_change=lambda e: ui.notify("You Selected '{}'".format(e))).classes('w-40')

	def openinstances():
		def installinstances():
			def dlv():
				dlver=verent.get()
				print(dlver)
				print(lastcrack)
				launchinfo.configure(text="Minecraft Version {}".format(dlver))
				if not lastcrack=="":
					print("starting...")
					lastcrackn=lastcrack.strip()
					print("portablemc start -u {} {}".format(lastcrackn, dlver))
					os.mkdir(".zdkrimson\\instances\\{}".format(dlver))
					os.mkdir(".zdkrimson\\instances\\{}\\saves".format(dlver))
#					if dlver=="1.6.1":
#						os.mkdir(".zdkrimson\\instances\\resourcepacks")
					os.mkdir(".zdkrimson\\instances\\{}\\resourcepacks")
					mclogss = subprocess.Popen("portablemc start -u {} {}".format(lastcrackn, dlver), shell=True)
					
				else:
					print("oh no microsoft no work yet :(")
					lastcrackn=lastcrack.strip()
					print("portablemc start -u {} {}".format(lastcrackn, dlver))
					os.mkdir(".zdkrimson\\instances\\{}".format(dlver))
					os.mkdir(".zdkrimson\\instances\\{}\\saves".format(dlver))
					os.mkdir(".zdkrimson\\instances\\{}\\resourcepacks")
					mclogss = subprocess.Popen("portablemc start -u {} {}".format(lastcrackn, dlver), shell=True)

			installwin = customtkinter.CTk()
			installwin.geometry("300x200")
			installwin.title("zdkrimson : Minecraft Launcher - Install Minecraft")

			maininsl = customtkinter.CTkFrame(master=installwin, fg_color="#3D0A11")
			maininsl.pack(pady=0, padx=0, fill="both", expand=True)

			homeinsl = customtkinter.CTkFrame(master=maininsl, fg_color="#630000")
			homeinsl.pack(pady=20, padx=20, fill="both", expand=True)

			innaent = customtkinter.CTkEntry(master=homeinsl, placeholder_text="Instance Name")
			innaent.pack(pady=10, padx=10)

			verent = customtkinter.CTkEntry(master=homeinsl, placeholder_text="Minecraft Version")
			verent.pack(pady=10, padx=10)

			setbtn = customtkinter.CTkButton(master=homeinsl, text="Download & Play", command=dlv)
			setbtn.pack(padx=20, pady=10)

			installwin.mainloop()

		def lmc():
			lmcver=verins.get()
			lastcrackn=lastcrack.strip()
			print(lmcver)
			print(lastcrack)
			print(lastcrackn)
			if lmcver=="Select Version":
				statusins.configure(text="Pick a Minecraft Version!!!")
			else:
				print("starting...")
#				os.rmdir("{}\\.minecraft\\resourcepacks".format(appdata))
#				os.rmdir("{}\\.minecraft\\saves".format(appdata))
#				shutil.copytree(".zdkrimson\\instances\\{}\\resourcepacks".format(lmcver), "{}\\.minecraft".format(appdata))
#				shutil.copytree(".zdkrimson\\instances\\{}\\saves".format(lmcver), "{}\\.minecraft".format(appdata))
				print("portablemc start -u {} {}".format(lastcrackn, lmcver))
				mclogss = subprocess.Popen("portablemc start -u {} {}".format(lastcrackn, lmcver), shell=True)	

		mcversions=os.listdir("{}\\.minecraft\\versions".format(appdata))		

		instancewin = customtkinter.CTk()
		instancewin.geometry("400x500")
		instancewin.title("zdkrimson : Minecraft Launcher - Instances")

		mainins = customtkinter.CTkFrame(master=instancewin, fg_color="#3D0A11")
		mainins.pack(pady=0, padx=0, fill="both", expand=True)

		homeins = customtkinter.CTkFrame(master=mainins, fg_color="#630000")
		homeins.pack(pady=40, padx=40, fill="both", expand=True)

		if os.path.exists("{}\\.minecraft".format(appdata))==False or mcversions==[]:
			statusins = customtkinter.CTkLabel(master=homeins, text="No Instances Found, Work in Progress")
			statusins.pack(pady=30, padx=0)

			getmc = customtkinter.CTkButton(master=homeins, text="Get Minecraft", command=installinstances)
			getmc.pack(padx=20, pady=10)

		else:
			print(mcversions)
			verins = customtkinter.CTkOptionMenu(homeins, values=mcversions)
			verins.pack(pady=10, padx=10)
			verins.set("Select Version")

			launchbtn = customtkinter.CTkButton(master=homeins, text="Launch", command=lmc)
			launchbtn.pack(padx=20, pady=10)

			getmc = customtkinter.CTkButton(master=mainins, text="Get Minecraft", command=installinstances)
			getmc.pack(padx=20, pady=10)

		instancewin.mainloop()

	# REQUEST FOR MINECRAFT VERSIONS
	#verget = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
	#print(verget)
	#print(verget.content)
#-	vergetstr=verget.content

#	ui.avatar(whitelogoshaded)

#	ui.avatar(whitetextshaded)

#	ui.avatar(amlshaded)

#	ui.query('body').style('background-image: url(file://{}/assets/bg/blur/crim1.png)'.format(CDDIR))

	ui.image(whitelogoshaded)

	ui.button('Accounts', on_click=loginscrn)

	ui.link('temp account btn', '/login')

	ui.button('Settings', on_click=settings)

	ui.link('temp settings btn', '/settings')

	ui.button('Instances', on_click=openinstances)

	ui.label('Launcher Version: {}'.format(__version__))

	ui.run(native=True, reload=False, title="zdkrimson : Minecraft Launcher", window_size=(700, 600), dark=True)

splash.after(3000, main_win)

splash.mainloop()
