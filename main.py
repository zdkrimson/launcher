import subprocess
import customtkinter
import os
import pyngrok
import json
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
lastcrack=""
firstime=0
print(CDDIR)

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
	    "firsttime": 1
	}
	configjson = json.dumps(config, indent=2)
	with open(".zdkrimson\\settings.json", "w") as outfile:
	    outfile.write(configjson)
	lastcrack=""
	firstime=1

# loading settings
with open('.zdkrimson\\settings.json', 'r') as openfile:
	configjson = json.load(openfile)
	print(configjson['lastcrack'])
	print(configjson['firsttime'])
	lastcrack=configjson['lastcrack']
	firsttime=configjson['firsttime']

splash = customtkinter.CTk()
splash.title("zdkrimson : Minecraft Launcher - Starting")
splash.geometry("350x262")
splash.overrideredirect(True)
splash.eval('tk::PlaceWindow . center')

splashScreen = customtkinter.CTkImage(dark_image=Image.open("assets/splashScreen.png"), size=(350, 262))

splashimg = customtkinter.CTkLabel(master=splash, text="", image=splashScreen, justify=customtkinter.LEFT)
splashimg.pack(side=customtkinter.LEFT, pady=0, padx=0)

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def main_win():
	splash.destroy()
	app = customtkinter.CTk()
	app.geometry("700x500")
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
			elif authtypeop.get()=="Cracked/Offline Mode":
#				loginprocco=subprocess.call("{}\\portablemc -u {} -u {}".format(CDDIR, zdemail, zduuid))
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

	home = customtkinter.CTkFrame(master=main, fg_color="#630000")
	home.pack(pady=100, padx=100, fill="both", expand=True)

#	bg = customtkinter.CTkLabel(master=app, text="", image=crim1)
#	bg.pack(pady=0, padx=0)

	logoshade = customtkinter.CTkLabel(master=home, text="", image=whitelogoshaded)
	logoshade.pack(pady=0, padx=0)
#	logoshade.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	textshade = customtkinter.CTkLabel(master=home, text="", image=whitetextshaded)
	textshade.pack(pady=0, padx=0)
#	textshade.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	subshade = customtkinter.CTkLabel(master=home, text="", image=amlshaded)
	subshade.pack(pady=0, padx=0)
#	subshade.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	login = customtkinter.CTkButton(master=home, text="Login", command=loginscrn)
	login.pack(padx=20, pady=10)
#	login.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	setbtn = customtkinter.CTkButton(master=home, text="Settings", command=settings)
	setbtn.pack(padx=20, pady=10)
#	setbtn.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

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