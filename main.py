from fonctions_menu import *
from fonctions_partitions import *

continuer = True
sousMenu1 = False

dataFrame = lectureFichier()

while continuer:
    menuPrincipal()
    choixVariable1 = choix(3)
    if choixVariable1 == 0:
        continuer = 0
        ecritureFichier(dataFrame)
    else:
        sousMenu1 = True
    while sousMenu1:
        if choixVariable1 == 1:
            menuEdition()
            choixVariable2 = choix(4)
            if choixVariable2 == 0:
                sousMenu1 = False
            elif choixVariable2 == 1:
                dataFrame = creerPartition(dataFrame)
            elif choixVariable2 == 2:
                modifierPartition(dataFrame)
            elif choixVariable2 == 3:
                supprimerPartition(dataFrame)


        elif choixVariable1 == 2:
            menuAffichage()
            choixVariable2 = choix(3)

            if choixVariable2 == 0:
                sousMenu1 = False

            elif choixVariable2 == 1:
                menuAffichage2()
                choixOrdre = choix(3)
                choixCritere = masqueDeSaisie().upper()
                print(afficherTouteData(dataFrame,choixOrdre,choixCritere).to_string())

            elif choixVariable2 == 2:
                menuAffichage2bis()
                choixColonne = masqueDeSaisie().upper()
                print("Veuillez ensuite entrer le mot clé de votre recherche")
                motCle = masqueDeSaisie()
                print(afficherRechercheData(dataFrame,choixColonne,motCle))


            sousMenu1 = False


