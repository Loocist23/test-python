from random import choice, randint
import string
from tkinter import *



def generate_pass():
    passmin = 24
    passmax = 64
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(passmin, passmax)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    with open("mdp.txt", "a+") as file:
        file.write(password + "\n")
        file.close()




fenetre = Tk()
fenetre.title("Generateur de mots de passe")
fenetre.geometry("720x480")
fenetre.minsize(360, 240)
fenetre.config(background="lightblue")

frame = Frame(fenetre, bg="lightblue")


width = 300
height = 300
image = PhotoImage(file="lock.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width , height=height, bg="lightblue", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

rightframe = Frame(frame, bg="lightblue")

#
label_title = Label(rightframe, text="Mot de passe", font=("Helvetica", 20), bg="lightblue", fg="white")
label_title.pack()


# creer un champs/entrée/input
password_entry = Entry(rightframe, font=("Helvetica", 20), bg="lightblue", fg="white")
password_entry.pack()

# creer un bouton
generate_button = Button(rightframe, text="Generer", font=("Helvetica", 20), bg="lightblue", fg="white", command=generate_pass)
generate_button.pack(fill=X)

# on place la sous boite à droite de la frame principale
rightframe.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# creation d'une barre de menu
menu_bar = Menu(fenetre)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_pass)
file_menu.add_command(label="Quitter", command=fenetre.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

fenetre.config(menu=menu_bar)



# afficher la fenetre
fenetre.mainloop()