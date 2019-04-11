from fonctions_partitions import *

def choix(nb_choix):
    boucle = True
    while boucle:
        try:
            choix = int(input("--> "))
            assert choix in range(0,nb_choix)
            boucle = False
        except:
            print("\nVeuillez entrer un entier positif valide")
    return choix

def masqueDeSaisie():
    boucle = True
    while boucle:
        try:
            masque = str(input("Entrez une chaîne de caractère : "))
            boucle = False
        except ValueError:
            print("Veuillez entrer une chaine de caractere valide")
    return masque

def menuPrincipal():
    affichage = "\n" + 10*"*"+" MENU PRINCIPAL " + 10*"*"
    question = 2*"\n" + "Que voulez vous faire ?"
    choix = "\n" + "1- Creer, Modifier ou Supprimer des informations"
    choix += "\n" + "2- Rechercher et afficher des oeuvres"
    choix += 2*"\n" + "0- Quitter" + "\n"
    print(affichage,question,choix)

def menuEdition():
    affichage = 10*"*" + " MENU EDITION " + 10*"*"
    question = 2*"\n" + "Que voulez vous faire ?"
    choix = "\n" + "1- Creer une fiche"
    choix += "\n" + "2- Modifier une fiche"
    choix += "\n" + "3- Supprimer une fiche"
    choix += 2*"\n" + "0- Quitter" + "\n"
    print(affichage,question,choix)

def menuAffichage():
    affichage = 10*"*" + " MENU AFFICHAGE " + 10*"*"
    question = 2*"\n" + "Voulez vous afficher toutes les oeuvres, ou faire une recherche selon des critères ?"
    choix = "\n" + "1- Toutes les oeuvres triées"
    choix += "\n" + "2- Recherche fine"
    choix += 2*"\n" + "0- Quitter"
    print(affichage,question,choix)

def menuAffichage2():
    affichage = 10*"*" + " MENU AFFICHAGE 2 " + 10*"*"
    question = 2*"\n" + "Selon quels critères voulez vous trier les oeuvres ?"
    criteres = "Les critères disponibles sont : "
    for noms in nomsColonnes:
        criteres += noms.lower() + ";" + " "
    choix = "\n" + "1- Tri par ordre croissant/alphabétique"
    choix += "\n" + "2- Tri par ordre décroissant/alphabétique inverse"
    choix += 2*"\n" + "0- Quitter" + "\n"
    print(affichage,question,criteres,choix)

def menuAffichage2bis():
    affichage = 10*"*" + " MENU AFFICHAGE 2 " + 10*"*"
    question = 2*"\n" + "Selon quels critères voulez vous afficher les oeuvres ?"
    criteres = "Les critères disponibles sont : "
    for noms in nomsColonnes:
        criteres += noms.lower() + ";" + " "
    print(affichage,question,criteres)
