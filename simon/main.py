import os
import random
import time
#import beepy
score = 0
ok = True


def clear_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def sequence(nbr_chiffres_debut):
    suite = ""
    for i in range (nbr_chiffres_debut):
        suite += str(random.randint(0, 9))
    return suite

nbr_chiffres_debut = 4
jeu = sequence(nbr_chiffres_debut)


while ok == True:
    clear_screen()
    print("Retenez la séquence")
    time.sleep(1)
    print(jeu)
    time.sleep(3)
    clear_screen()
    rep = input("Votre réponse :")
    ok = (rep == jeu)
    if ok:
        score += 1
        print("Bonne réponse, votre score est :" + str(score))
        jeu = jeu + str(random.randint(0, 9))
    else:
        print("Mauvaise réponse, la séquence était : " + str(jeu))
        if score <= 1:
            print("Vous avez " + str(score) + " bonne réponse.")
        else:
            print("Vous avez " + str(score) + " bonnes réponses.")

    time.sleep(1)
    clear_screen()


print("Jeu terminé")

