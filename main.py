"""
from lib2to3.refactor import get_all_fix_names


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
    
        age_str = input(nom_personne + " Quel est ton age ? ")
        try:
            age_int = int(age_str)
        except:
            print("EREUR: vous devez rentrer un nombre pour l'age")
    return age_int


def demander_nom():
    reponse_nom = ""

    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ? ") 
        try:
            reponse_nom ==""
        except:
            print("EREUR: Veuillez ecrire un nom")
    return reponse_nom


def demander_taille(nom_personne):
    taille_personnes = 0.0
    taille_personnes = input(nom_personne + "Quel est votre taille ? ")
    return taille_personnes

def Afficher_info_pers(nom_personne, age_personne, taille_personne):
    print()
    print("Vous vous apellez " + nom_personne + " et vous avez " + str(age_personne) + " ans.")
    print(f"Vous vous apellez {nom_personne} et vous avez {str(age_personne)}  ans.")
    print("Vous vous apellez %s et vous avez %s ans." %(nom_personne, age_personne))

    print("L'année prochaine vous aurais " + str(age_personne+1) + " ans.")
    print("L'année prochaine vous aurais %s ans." %(age_personne+1))
    print("taille du string : " + str(len(nom_personne)))

    if not taille_personne == 0:
        print("Votre taille est :" + taille_personne + " m.")

    if age_personne == 1 or age_personne == 2:
        print("Vous etes un(e) bébé")
    elif age_personne < 10:
        print("Vous etes un(e) enfant")
    elif age_personne == 17:
        print("Vous etes presque majeur")
    elif 12 <= age_personne < 18:
        print("Vous etes adolescent")
    elif age_personne == 18:
        print("Tout juste majeur : Félicitations")
    elif age_personne > 60:
        print("Vous etes senior")
    elif age_personne >= 18:
        print("Vous etes majeur.")
    else:
        print("Vous etes mineur")
    
    
    


    



# demander le nom et l'age
# nom1 = demander_nom()
nom1 = "Anthony"
age1 = demander_age(nom1)

nom2 = "Loli"
# nom2 = demander_nom()
age2 = demander_age(nom2)

Afficher_info_pers(nom1, age1)
Afficher_info_pers(nom2, age2)




print("Tu t'apelle " + nom1 + " et tu as " + str(age1) + " ans.")
print("L'année prochaine tu auras " + str(age1+1) + " ans.")

print("Tu t'apelle " + nom2 + " et tu as " + str(age2) + " ans.")
print("L'année prochaine tu auras " + str(age2+1) + " ans.")

NB_PERSONNE = 1

for i in range(0, NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    taille = demander_taille(nom)
    Afficher_info_pers(nom, age, taille)"""







"""
def Ecrire():
    for i in range(0, 5):
        fruit = input("Nommer un fruit")
        txt.append(fruit)
    return fruit



car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}



age = 36
txt = " Lol lol"
x = txt[0:2]
y = txt.strip()
u = txt.upper()
uu = txt.lower()
ty = txt.replace("l","P")
print(txt)
print(x)
print(y)
print(u)
print(uu)
print(ty)
txt = "My name is Anthony, and i am {}"
print(txt.format(age))
txt = ["apple", "banana", "cherry"]
print(txt[0])
print(txt[2])
print(txt[1])

Ecrire()
print(txt)
txt.insert(1, "papa")
print(txt)
print(txt[-1])
print(len(txt))
txta = {"apple", "banana", "cherry"}
more_txt = ["orange", "mango", "grapes"]
txta.update(more_txt)
print(txta)
txta.remove("apple")
print(txta)
txta.add("apple")
print(txta)
txta.discard("apple")
print(txta)
txt.remove("papa")
print(txt)
print(car.get("model"))
car["color"] = "red"
print(car.get("color"))
car.pop("model")
print(car)
car.clear()
print(car)

x=float(5)
y=int(5)
print(x , y)

mdp = ["CKBTZS","EVMKPQ","PHAWAK","PCSCMN","UNHNXS","NHVDDE"]
print("Tous tes mdp ubisoft connect : ")
print(mdp)"""

# coding: utf-8
 
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()