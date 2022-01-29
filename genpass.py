from random import choice, randint
import string
from tkinter import END


def generate_pass():
    passmin = 24
    passmax = 32
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(passmin, passmax)))
    with open("mdp.txt", "a+") as file:
        file.write(password + "\n")
        file.close()
    return password

x = 0

for x in range(0, 20000):
    x+1
    tutu = generate_pass()
    print(tutu)
else:
    print("valeur de x max atteinte " + str(x))