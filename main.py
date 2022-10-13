# Rayna Sillini
# TP2

from random import *


def jeu():
    jeu_commence = True
    print("Bienvenue au jeu de devinette! Commencer par écrire la limite des nombres puis commence a deviner!")

    while jeu_commence:
        limite_1 = int(input("Entrez la limite pour le plus petit nombre:"))
        limite_2 = int(input("Entrez la limite pour le plus gros nombre:"))
        nb_essais = 1
        nombre_mystere = randint(limite_1, limite_2)

        not_found = True
        while not_found:
            essai = int(input("Entrez votre essai:"))
            if essai < limite_1:
                print("Votre nombre dépasse la limite")
            elif essai > limite_2:
                print("Votre nombre dépasse la limite")
            elif essai > nombre_mystere:
                print("Le numero est plus petit")
                nb_essais += 1
            elif essai < nombre_mystere:
                print("Le numero est plus grand")
                nb_essais += 1
            else:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essais} essaies.")
                not_found = False
                restart = input("Si vous voulez rejouer, tapez (o). Sinon, tapez (n)")
                if restart == "o":
                    jeu_commence = True
                elif restart == "n":
                    print("A la prochaine!")
                    jeu_commence = False


jeu()
