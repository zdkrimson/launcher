import subprocess
import customtkinter
import os
import pyngrok
import json
import requests
from subprocess import Popen
from PIL import Image
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("krimson.json")  # Themes: "blue" (standard), "green", "dark-blue"

print(r"""
	      _  _           _                               
         | || |         (_)                              
 ____  __| || | __ _ __  _  _ __ ___   ___   ___   _ __  
|_  / / _` || |/ /| '__|| || '_ ` _ \ / __| / _ \ | '_ \ 
 / / | (_| ||   < | |   | || | | | | |\__ \| (_) || | | |
/___| \__,_||_|\_\|_|   |_||_| |_| |_||___/ \___/ |_| |_|
                                 	Written by ItsIceCreeperPE Dev                       
                                                         
		""")

authtype=0
CDDIR=os.getcwd()
global lastcrack
global firstime
global __version__
global instnum
lastcrack=""
firstime=0
__version__="alpha2"
instances=[]
instnum=0
print(CDDIR)

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
	    "lastinstance": "",
	    "instnum": 0
	}
	configjson = json.dumps(config, indent=2)
	with open(".zdkrimson\\settings.json", "w") as outfile:
	    outfile.write(configjson)
	lastcrack=""
	firstime=1
	lastinstance=""
	instnum=0
if os.path.exists(".zdkrimson\\instances.json")==False:
	print("instances file(instances.json) doesn't exist, created one just now.")
	instancesfile = {
	    "instance0": "",
	    "instance1": "",
	    "instance2": "",
	    "instance3": "",
	    "instance4": "",
	    "instance5": "",
	    "instance6": "",
	    "instance7": "",
	    "instance8": "",
	    "instance9": "",
	}
	instjson = json.dumps(instancesfile, indent=2)
	with open(".zdkrimson\\instances.json", "w") as outfile:
	    outfile.write(instjson)

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
	except KeyError:
		print("Settings file isn't up-to-date")
		config = {
		    "lastcrack": "",
		    "firsttime": 1,
		    "lastinstance": "",
		    "instnum": 0
		}
		configjson = json.dumps(config, indent=2)
		with open(".zdkrimson\\settings.json", "w") as outfile:
		    outfile.write(configjson)
		lastcrack=""
		firstime=1
		lastinstance=""
		instnum=0

with open('.zdkrimson\\instances.json', 'r') as openfile:
	instjson = json.load(openfile)
	print(instjson['instance0'])
	print(instjson['instance1'])
	print(instjson['instance2'])
	print(instjson['instance3'])
	print(instjson['instance4']) 
	print(instjson['instance5'])
	print(instjson['instance6'])
	print(instjson['instance7'])
	print(instjson['instance8'])
	print(instjson['instance9']) 
	inst0=instjson['instance0']
	inst1=instjson['instance1']
	inst2=instjson['instance2'] 
	inst3=instjson['instance3']
	inst4=instjson['instance4']
	inst5=instjson['instance5'] 
	inst6=instjson['instance6']
	inst7=instjson['instance7']
	inst8=instjson['instance8'] 
	inst9=instjson['instance9'] 
	instancelist=json.dumps(instjson)
	print(instancelist)

splash = customtkinter.CTk()
splash.title("zdkrimson : Minecraft Launcher - Starting")
splash.geometry("350x262")
splash.overrideredirect(True)
splash.eval('tk::PlaceWindow . center')

splashScreen = customtkinter.CTkImage(dark_image=Image.open("assets/splashScreen.png"), size=(350, 262))

splashimg = customtkinter.CTkLabel(master=splash, text="", image=splashScreen, justify=customtkinter.LEFT)
splashimg.pack(side=customtkinter.LEFT, pady=0, padx=0)

def main_win():
	splash.destroy()
	app = customtkinter.CTk()
	app.geometry("700x600")
	app.title("zdkrimson : Minecraft Launcher")
	app.iconbitmap("zdicon.ico")
#	app.overrideredirect(True)

	# image loading
	crim1 = customtkinter.CTkImage(dark_image=Image.open("assets/bg/blur/crim1.png"), size=(700, 500))
	whitelogoshaded = customtkinter.CTkImage(dark_image=Image.open("assets/logo/image/shaded/white.png"), size=(100, 100))
	whitetextshaded = customtkinter.CTkImage(dark_image=Image.open("assets/logo/full/white.png"), size=(200, 45))
	amlshaded = customtkinter.CTkImage(dark_image=Image.open("assets/logo/sub/shaded/white.png"), size=(200, 25))

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
			zdemail=usermaills.get()
			zduuid=uuidls.get()
			print(authtype)
			print(authtypeop.get())
			if (authtypeop.get())=="Microsoft":
				messagebox.showinfo("Note", "The Application will stop responding until the authentication as been completed.\nThe Authentication page should open in your default browser.\nClick OK to continue the authentication process.")
				loginprocms=subprocess.call("{}\\portablemc login -m {}".format(CDDIR, zdemail))
				print(loginprocms)
				if loginprocms==14:
					statusls.configure(text="Your Microsoft account doesn't have a legitmate copy of Minecraft. :(")
				else:
					statusls.configure(text="You own Minecraft, you are logged in! :D")
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
			elif authtypeop.get()=="Cracked/Offline Mode":
#				loginprocco=subprocess.call("{}\\portablemc -u {} -u {}".format(CDDIR, zdemail, zduuid))
				lastcrack=zdemail
				user = {
				    "name": "{}".format(zdemail),
				    "uuid": "{}".format(zduuid)
				}
				jsonfilezd = json.dumps(user, indent=2)
				with open(".zdkrimson\\crackedusers\\{}.json".format(zdemail), "w") as outfile:
   					outfile.write(jsonfilezd)
				statusls.configure(text="You are logged in as {} as a Cracked/Offline Mode Player.".format(zdemail))
				cadb = open(".zdkrimson\\crackedusers\\crackaccount.txt", "a")
				print(cadb)
				cadb.write("{}\n".format(zdemail))
				cadb.close()

		logscrnwin = customtkinter.CTk()
		logscrnwin.geometry("400x500")
		logscrnwin.title("zdkrimson : Minecraft Launcher - Login")

		mainls = customtkinter.CTkFrame(master=logscrnwin, fg_color="#3D0A11")
		mainls.pack(pady=0, padx=0, fill="both", expand=True)

		lstitle = customtkinter.CTkLabel(master=mainls, text="\n\nLogin")
		lstitle.pack(pady=0, padx=0)

		logframls = customtkinter.CTkFrame(master=mainls, fg_color="#630000")
		logframls.pack(pady=30, padx=30, fill="both", expand=True)

		authtypeop = customtkinter.CTkOptionMenu(logframls, values=["Microsoft", "Cracked/Offline Mode"], command=selectedauth)
		authtypeop.pack(pady=10, padx=10)
		authtypeop.set("None Selected :|")

		usermaills = customtkinter.CTkEntry(master=logframls, placeholder_text="Username/E-Mail")
		usermaills.pack(pady=10, padx=10)

		uuidls = customtkinter.CTkEntry(master=logframls, placeholder_text="UUID (Optional)")
		uuidls.pack_forget()

		logls = customtkinter.CTkButton(master=logframls, text="Login", command=login)
		logls.pack(padx=20, pady=10)

		statusls = customtkinter.CTkLabel(master=logframls, text="")
		statusls.pack(pady=0, padx=0)

		logscrnwin.mainloop()

	def settings():
		def userchange(value):
			print(value)
			lastcrack=(value)
			print(lastcrack)
			config = {
			    "lastcrack": "{}".format(value),
			    "firsttime": firstime
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
			
		settingswin = customtkinter.CTk()
		settingswin.geometry("400x500")
		settingswin.title("zdkrimson : Minecraft Launcher - Settings")
		
		mainset = customtkinter.CTkFrame(master=settingswin, fg_color="#3D0A11")
		mainset.pack(pady=0, padx=0, fill="both", expand=True)

		settitle = customtkinter.CTkLabel(master=mainset, text="\n\n\nSettings")
		settitle.pack(pady=0, padx=0)

		homeset = customtkinter.CTkFrame(master=mainset, fg_color="#630000")
		homeset.pack(pady=40, padx=40, fill="both", expand=True)
 
		userst = customtkinter.CTkLabel(master=homeset, text="\n\n\nUsers")
		userst.pack(pady=0, padx=0)

		usersel = customtkinter.CTkOptionMenu(homeset, values=rcadb, command=userchange)
		usersel.pack(pady=10, padx=10)
		usersel.set(lastcrack)

		settingswin.mainloop()

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
					instnum+=1
					mclogss = subprocess.Popen("portablemc start -u {} {}".format(lastcrackn, dlver), shell=True)
					#logs.insert("0.0", mclogss)
				else:
					print("oh no microsoft no work yet :(")
					lastcrackn=lastcrack.strip()
					print("portablemc start -u {} {}".format(lastcrackn, dlver))
					instnum+=1
					mclogss = subprocess.Popen("portablemc start -u {} {}".format(lastcrackn, dlver), shell=True)

			installwin = customtkinter.CTk()
			installwin.geometry("300x200")
			installwin.title("zdkrimson : Minecraft Launcher - Install Minecraft")

			maininsl = customtkinter.CTkFrame(master=installwin, fg_color="#3D0A11")
			maininsl.pack(pady=0, padx=0, fill="both", expand=True)

			homeinsl = customtkinter.CTkFrame(master=maininsl, fg_color="#630000")
			homeinsl.pack(pady=20, padx=20, fill="both", expand=True)

			verent = customtkinter.CTkEntry(master=homeinsl, placeholder_text="Minecraft Version")
			verent.pack(pady=10, padx=10)

			setbtn = customtkinter.CTkButton(master=homeinsl, text="Download & Play", command=dlv)
			setbtn.pack(padx=20, pady=10)

			installwin.mainloop()

		def openi0():
			lastcrackn=lastcrack.strip()
			print("portablemc start -u {} {}".format(lastcrackn, inst0))
			mclogss = subprocess.Popen("portablemc start -u {} {}".format(lastcrackn, inst0), shell=True)

		instancewin = customtkinter.CTk()
		instancewin.geometry("400x500")
		instancewin.title("zdkrimson : Minecraft Launcher - Instances")

		mainins = customtkinter.CTkFrame(master=instancewin, fg_color="#3D0A11")
		mainins.pack(pady=0, padx=0, fill="both", expand=True)

		homeins = customtkinter.CTkFrame(master=mainins, fg_color="#630000")
		homeins.pack(pady=40, padx=40, fill="both", expand=True)

		if inst0=="" and inst1=="" and inst2=="" and inst3=="" and inst4=="" and inst5=="" and inst6=="" and inst7=="" and inst8=="" and inst9=="":
			statusins = customtkinter.CTkLabel(master=homeins, text="No Instances Found, Work in Progress")
			statusins.pack(pady=30, padx=0)

			getmc = customtkinter.CTkButton(master=homeins, text="Get Minecraft", command=installinstances)
			getmc.pack(padx=20, pady=10)

		else:
			if not inst0=="":
				inst0btn = customtkinter.CTkButton(master=homeins, text="Instance 0", command=openi0)
				inst0btn.pack(padx=20, pady=10)

			if not inst1=="":
				inst1btn = customtkinter.CTkButton(master=homeins, text="Instance 1", command=openi1)
				inst1btn.pack(padx=20, pady=10)

			if not inst2=="":
				inst2btn = customtkinter.CTkButton(master=homeins, text="Instance 2", command=openi2)
				inst2btn.pack(padx=20, pady=10)

			if not inst3=="":
				inst3btn = customtkinter.CTkButton(master=homeins, text="Instance 3", command=openi3)
				inst3btn.pack(padx=20, pady=10)

			if not inst4=="":
				inst4btn = customtkinter.CTkButton(master=homeins, text="Instance 4", command=openi4)
				inst4btn.pack(padx=20, pady=10)

			if not inst5=="":
				inst5btn = customtkinter.CTkButton(master=homeins, text="Instance 5", command=openi5)
				inst5btn.pack(padx=20, pady=10)

			if not inst6=="":
				inst6btn = customtkinter.CTkButton(master=homeins, text="Instance 6", command=openi6)
				inst6btn.pack(padx=20, pady=10)

			if not inst7=="":
				inst7btn = customtkinter.CTkButton(master=homeins, text="Instance 7", command=openi7)
				inst7btn.pack(padx=20, pady=10)

			if not inst8=="":
				inst8btn = customtkinter.CTkButton(master=homeins, text="Instance 8", command=openi8)
				inst8btn.pack(padx=20, pady=10)

			if not inst9=="":
				inst9btn = customtkinter.CTkButton(master=homeins, text="Instance 9", command=openi9)
				inst9btn.pack(padx=20, pady=10)

			getmc = customtkinter.CTkButton(master=mainins, text="Get Minecraft", command=installinstances)
			getmc.pack(padx=20, pady=10)

		instancewin.mainloop()

	# REQUEST
	#verget = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
	#print(verget)
	#print(verget.content)
#-	vergetstr=verget.content


#	bar = customtkinter.CTkFrame(master=app, fg_color="black")
#	bar.pack(pady=0, padx=0, fill="x", expand=False)

#	title = customtkinter.CTkLabel(master=bar, text="zdkrimson : Minecraft Launcher", justify=customtkinter.LEFT)
#	title.pack(side=customtkinter.LEFT, pady=10, padx=10)

#	close = customtkinter.CTkButton(master=bar, fg_color="black", hover_color="red", text="X", command=quit)
#	close.pack(side=customtkinter.RIGHT, pady=10, padx=10)

#	bar.bind("<B1-Motion>", move_app)
#	title.bind("<B1-Motion>", move_app)

	main = customtkinter.CTkFrame(master=app, fg_color="#3D0A11")
	main.pack(pady=0, padx=0, fill="both", expand=True)

	bg = customtkinter.CTkLabel(master=main, text="", image=crim1)
	bg.pack(pady=0, padx=0, fill="both")
	bg.place(x=0, y=0, relwidth=1, relheight=1)

	home = customtkinter.CTkFrame(master=main, fg_color="transparent")
	home.pack(pady=50, padx=100, fill="both", expand=True)

	logoshade = customtkinter.CTkLabel(master=home, text="", image=whitelogoshaded)
	logoshade.pack(pady=0, padx=0)
#	logoshade.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	textshade = customtkinter.CTkLabel(master=home, text="", image=whitetextshaded)
	textshade.pack(pady=0, padx=0)
#	textshade.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	subshade = customtkinter.CTkLabel(master=home, text="", image=amlshaded)
	subshade.pack(pady=0, padx=0)
#	subshade.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	login = customtkinter.CTkButton(master=home, text="Accounts", command=loginscrn)
	login.pack(padx=20, pady=10)
#	login.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	setbtn = customtkinter.CTkButton(master=home, text="Settings", command=settings)
	setbtn.pack(padx=20, pady=10)
#	setbtn.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	openins= customtkinter.CTkButton(master=home, text="Instances", command=openinstances)
	openins.pack(padx=20, pady=10)

	launchinfo = customtkinter.CTkLabel(master=home, text="", justify=customtkinter.LEFT)
	launchinfo.pack(pady=10, padx=10)

	ver = customtkinter.CTkLabel(master=main, text="Launcher Version: {}".format(__version__), justify=customtkinter.LEFT)
	ver.pack(pady=10, padx=10)

#	logs = customtkinter.CTkTextbox(master=home, width=600, height=200)
#	logs.pack(pady=10, padx=10)

#	logs = customtkinter.CTkTextbox(master=home, width=400, height=200)
#	logs.pack(pady=10, padx=10)
#	logs.insert("0.0", "Logs go here but don't work")
#	logs.configure(state="disabled")

#	versel = customtkinter.CTkOptionMenu(home, values=verlist)
#	versel.pack(pady=10, padx=10)
#	versel.set("None Selected :|")



#	ver = customtkinter.CTkLabel(master=main, text="Version: ", justify=customtkinter.LEFT)
#	ver.pack(pady=10, padx=10)

#	version = customtkinter.CTkEntry(master=main, placeholder_text="1.8.9")
#	version.pack(pady=10, padx=10)

#	java = customtkinter.CTkEntry(master=main, placeholder_text="Java Installation Directory")
#	java.pack(pady=10, padx=10)

#	path = customtkinter.CTkEntry(master=main, placeholder_text="Minecraft Download Path")
#	path.pack(pady=10, padx=10)

#	dlb = customtkinter.CTkButton(master=main, text="Download", command=download)
#	dlb.pack(pady=10, padx=10)

#	play = customtkinter.CTkButton(master=main, text="Play", command=play)
#	play.pack(pady=10, padx=10)

	app.mainloop()

splash.after(3000, main_win)

splash.mainloop()