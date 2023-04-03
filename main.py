import minecraft_launcher_lib
import customtkinter
import os
import pyngrok

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

splash = customtkinter.CTk()
splash.title("zdkrimson : Minecraft Launcher - Starting")
splash.geometry("350x200")
splash.overrideredirect(True)
splash.eval('tk::PlaceWindow . center')

splashFrame = customtkinter.CTkFrame(master=splash, fg_color="darkred")
splashFrame.pack(pady=0, padx=0, fill="both", expand=True)

splashTitle = customtkinter.CTkLabel(master=splashFrame, text="\nzdkrimson\nMinecraft Launcher\nWritten by ItsIceCreeperPE Dev", justify=customtkinter.CENTER)
splashTitle.pack(pady=60, padx=10)

splashGH = customtkinter.CTkLabel(master=splashFrame, text="https://www.github.com/Official-IceCreeperPE/zdkrimson", justify=customtkinter.CENTER)
splashGH.pack(pady=0, padx=10)

# crim1 = PhotoImage(file = "assets/bg/blur/crim1.png")

def main_win():
	splash.destroy()
	app = customtkinter.CTk()
	app.geometry("700x500")
	app.title("zdkrimson : Minecraft Launcher")
	app.overrideredirect(True)

	def move_app(e):
		app.geometry(f'+{e.x_root}+{e.y_root}')

	def quit():
		app.quit()	

	bar = customtkinter.CTkFrame(master=app, fg_color="black")
	bar.pack(pady=0, padx=0, fill="x", expand=False)

	title = customtkinter.CTkLabel(master=bar, text="zdkrimson : Minecraft Launcher", justify=customtkinter.LEFT)
	title.pack(side=customtkinter.LEFT, pady=10, padx=10)

	button_1 = customtkinter.CTkButton(master=bar, fg_color="black", hover_color="red", text="X", command=quit)
	button_1.pack(side=customtkinter.RIGHT, pady=10, padx=10)

	bar.bind("<B1-Motion>", move_app)
	title.bind("<B1-Motion>", move_app)

	main = customtkinter.CTkFrame(master=app)
	main.pack(pady=20, padx=20, fill="both", expand=True)

	label_1 = customtkinter.CTkLabel(master=main, text="is kool launcha bruh :0\nVERY MUCH WORK IN PROGRESS\nBut you can watch the project on github and perhaps star it :)\nhttps://www.github.com/Official-IceCreeperPE/zdkrimson", justify=customtkinter.LEFT)
	label_1.pack(side=customtkinter.LEFT, pady=10, padx=10)

	app.mainloop()

splash.after(3000, main_win)

splash.mainloop()