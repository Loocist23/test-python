from tkinter import *
from tkinter import font 
import webbrowser

def openchannel():
    webbrowser.open_new("https://www.youtube.com/channel/UCfYMKunf1CRJCGv9WhiEFXg")


fenetre = Tk()

fenetre.title("Mon Application")
fenetre.geometry("1080x720")
fenetre.minsize(480, 360)
fenetre.iconbitmap("logo.ico")
fenetre.config(background="grey")


frame = Frame(fenetre, bg="grey")

label_title = Label(frame, text="Bienvenue sur ma premiere app.", font=("Courrier", 40), bg="grey", foreground="white")
label_title.pack()

label_subtitle = Label(frame, text="Une app ou je vais tester des choses.", font=("Courrier", 25), bg="grey", foreground="white")
label_subtitle.pack()

bunton1 = Button(frame, text="Clique ta mere", font="Courrier" , bg="white", fg="grey", command=openchannel)

frame.pack(expand=YES)
bunton1.pack(pady=25, fill=X)

fenetre.mainloop()