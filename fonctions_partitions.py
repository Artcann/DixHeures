import numpy as np
import pandas as pd


from fonctions_menu import *

nomsColonnes = ["COMPOSITEUR","TYPE D'OEUVRE","NB DE MOUVEMENT"]

def masqueDeSaisie():
    boucle = True
    while boucle:
        try:
            masque = str(input("Entrez une chaîne de caractère : "))
            boucle = False
        except ValueError:
            print("Veuillez entrer une chaine de caractere valide")
    return masque

def lectureFichier():
    try:
        df = pd.read_csv("data.csv", index_col=0,sep=";")
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

def afficherRechercheData(df,colonne,condition):
    try:
        if df[(df[colonne]==condition)].empty:
            raise KeyError
        return df[df[colonne] == condition]
    except KeyError as error:
        print(error)
        return "\n" + " Votre recherche n'a pas aboutie, êtes vous sûr d'avoir entré les bonnes informations ? \n Si oui, alors " \
                   "votre recherche n'est pas dans notre base de données, \n vous pouvez la rajouter via " \
                   "le menu d'édition" + "\n"

nouvelleInfo = np.array([["Chopin","Ballade",1],["Beethoven","Symphonie","3"],["Mozart","Requiem",1]])
nouvelleOeuvre =["Ballade No 1", "Symphonie No 9", "Requiem"]


