import random

rejouer = "o"
while rejouer == "o":
    def demander_nombre(nb_min, nb_max):
        nbr_int = 0
        while nbr_int == 0:
            nbr_str = input("Quel est le nombre magique entre " + str(nb_min) + " et " + str(nb_max) + " ?")
            try:
                nbr_int = int(nbr_str)
            except ValueError:
                print("ERREUR: Vous devez entrer un nombre")
            else:
                if nbr_int < nb_min or nbr_int > nb_max:
                    print("ERREUR: choisissez un nombre entre 1 et 10 !!!!!!")
                    nbr_int = 0
        return nbr_int


    NOMBRE_MIN = 0
    NOMBRE_MAX = 20
    NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre = 0
    # boucle de test
    while not nombre == NOMBRE_MAGIQUE:
        nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
        if nombre > NOMBRE_MAGIQUE:
            print("Votre nombre est trop grand.")
        elif nombre < NOMBRE_MAGIQUE:
            print("Votre nombre est trop petit.")
        else:
            print("Bravo")

    rejouer = input("Voulez vous refaire une partie? o / n ?")
else:
    print("Au revoir ;)")