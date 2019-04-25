import secrets

import numpy as np
import pandas as pd
import hashlib

from modules.fonctions_menu import *

nomsColonnes = ["COMPOSITEUR","TYPE D'OEUVRE","NB DE MOUVEMENT"]

def authentification(dico,testSecu):
    print("Veuillez entrer votre Identifiant")
    ID = masqueDeSaisie()
    print("Veuillez entrer votre mot de passe")
    plainMDP = masqueDeSaisie()
    sel = dico[ID][1]
    contenu = plainMDP + sel
    hashMdptest = hashlib.new("SHA512")
    hashMdptest.update(contenu.encode("utf-8"))
    try:
        if hashMdptest.hexdigest() == dico[ID][0]:
            print("Vous êtes authentifié !")
            testSecu = True
        else:
            print("Mot de passe incorrect")

    except KeyError:
        print("Le nom d'utilisateur que vous avez entrer est inconnue")
    return testSecu

def creationCompte(dico):
    print("Veuillez entrer votre Identifiant")
    ID = masqueDeSaisie()
    print("Veuillez entrer votre mot de passe")
    plainMDP = masqueDeSaisie()
    sel = secrets.token_hex(16)
    contenu = plainMDP + sel
    hashMdpSale = hashlib.new("SHA512")
    hashMdpSale.update(contenu.encode("utf-8"))
    if ID not in dico.keys():
        dico[ID] = (hashMdpSale.hexdigest(),sel)
        fichier = open("data/passwords.csv", "a")
        fichier.write("{0},{1},{2},\n".format(ID, hashMdpSale.hexdigest(), sel))
        fichier.close()
        print("Votre compte à été correctement creer")
    else:
        print("Votre nom d'utilisateur est déjà pris")

def chargementMotDePasse():
    fichier = open("data/passwords.csv", "r")
    dico = {}
    for ligne in fichier:
        lignes = ligne.split(",")
        dico[lignes[0]] = (lignes[1], lignes[2])
    return dico

def masqueDeSaisie():
    boucle = True
    while boucle:
        try:
            masque = str(input("Entrez une chaîne de caractère : "))
            boucle = False
        except ValueError:
            print("Veuillez entrer une chaine de caractere valide")
    return masque

def lectureFichier(nomFichier):
    try:
        df = pd.read_csv("data/" + nomFichier + ".csv", index_col=0,sep=";")
        return df
    except IOError:
        "Aucune donnée n'est enregistrée"

def ecritureFichier(df):
    try:
        df.to_csv("data.csv", sep=",")
    except IOError:
        "Une erreur s'est produite lors de l'écriture"


def creerPartition(df):
    print("Vous allez avoir une liste d'information à rentrer : ")
    print("Quel est le nom de l'oeuvre ?")
    nomOeuvre = [masqueDeSaisie()]

    print("Quel est le compositeur de cet oeuvre ?")
    compositeur = str(input("Entrez une chaîne de caractère : "))
    print("Quelle est la forme de cette oeuvre (par ex: Symphonie, Sonate...) ?")
    forme = str(input("Entrez une chaîne de caractère : "))
    print("Combien de mouvement possède cette oeuvre ? Si elle n'en possède pas, tapez 0")
    nbMouvement = str(input("Entrez une chaîne de caractère : "))
    infoOeuvre = np.array([[compositeur,forme,nbMouvement]])

    df = pd.DataFrame(infoOeuvre,index=nomOeuvre,columns=nomsColonnes).append(df,sort=True)
    return df

def supprimerPartition(df):

    print("Quel est le nom de l'oeuvre que vous voulez supprimer")
    nomOeuvre = [masqueDeSaisie()]
    df.drop(nomOeuvre,axis = 0, inplace=True)
    print("Partition supprimée")

def modifierPartition(df):

    print("Quel est le nom de l'oeuvre que vous voulez modifier")
    nomOeuvre = masqueDeSaisie()
    print("Quelle information relative à cette oeuvre voulez vous modifier ?")
    colonne = masqueDeSaisie()
    print(df.loc[nomOeuvre,colonne])
    print("Veuillez entrer la nouvelle information :")
    infoModif = masqueDeSaisie()
    df.at[nomOeuvre,colonne] = infoModif

def afficherTouteData(df,ordre,critere):
    if ordre == 1:
        df = df.sort_values(by = critere,kind = "mergesort")
    elif ordre == 2:
        df = df.sort_values(by=critere, ascending=False, kind = "mergesort")
    return df

def afficherRechercheData(df,condition,dfRecherche,colonneRecherche):

    try:
        listeRecherche = dfRecherche.loc[condition,colonneRecherche].split(",")
        for nombre in listeRecherche:
            print(df.loc[int(nombre)])
            print("\n")






    except KeyError as error:
        print(error)
        return "\n" + " Votre recherche n'a pas aboutie, êtes vous sûr d'avoir entré les bonnes informations ? \n Si oui, alors " \
                   "votre recherche n'est pas dans notre base de données, \n vous pouvez la rajouter via " \
                   "le menu d'édition" + "\n"

"""
    try:
        if df[(df[colonne]==condition)].empty:
            raise KeyError
        return df[df[colonne] == condition]"""
