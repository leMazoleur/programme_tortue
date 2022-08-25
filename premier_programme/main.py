global age  = 0


def demander_age(nom):
    age_int = 0
    while age_int == 0:
        age_int = input("Quel est ton âge? ")
        try:
         age = int(age_int) + 1
        except:
            print("Tu dois rentrer un nombre pour l'âge !!!!")
    return age


def demander_nom():
    personne = ""
    while personne == "":
        personne = input("Quel est ton nom? ")
    return personne


def afficher(nom, age):
    print("Ton nom est " + nom + " tu as " + str(age) + " ans et tu auras " + str(age+1) + " ans l'an prochain.")
    if age >= 18:
        print("Tu es majeur")
    else:
        print("Tu es mineur")
nom1 = demander_nom()
age1 = demander_age(nom1)
nom2 = demander_nom()
age2 = demander_age(nom2)
afficher1 = afficher(nom1, age1)
afficher2 = afficher(nom2, age2)







