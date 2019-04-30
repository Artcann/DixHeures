from modules.fonctions_menu import *
from modules.fonctions_partitions import *

# Définition des variables de boucle
continuer = True
sousMenu1 = False
acces = False


# Création des dataframes à partir des différents CSV
dataframePartition = lectureFichier("data")
dataframeCompositeurs = lectureFichier("compositeurs")
dataframeInstruments = lectureFichier("instruments")
dataframeTonalites = lectureFichier("tonalites")

print(dataframeTonalites, "\n", dataframePartition.to_string(), "\n", dataframeInstruments, "\n", dataframeCompositeurs)


# Création du dictionnaire des utilisateur à partir du CSV passwords
dicoIdentifiant = chargementMotDePasse()


# Début de la boucle principale
while continuer:

    # Appel de la fonction d'authentification et premier menu
    # Plus d'infos sur les fonctions dans le dossier modules
    menuAuthentification()
    choixAuthentification = choix(3)
    if choixAuthentification == 1:
        acces = authentification(dicoIdentifiant, acces)
    elif choixAuthentification == 2:
        creationCompte(dicoIdentifiant)
    elif choixAuthentification == 0:
        continuer = 0
        ecritureFichier(dataframePartition)

    # Début de la boucle de menu principal
    while acces:

        menuPrincipal()
        choixVariable1 = choix(4)

        if choixVariable1 == 0:
            acces = False
            continuer = False

        elif choixVariable1 == 3:
            acces = False

        else:
            sousMenu1 = True

        # Début de la boucle de choix entre éditer et afficher
        while sousMenu1:

            if choixVariable1 == 1:
                menuEdition()
                choixVariable2 = choix(4)

                if choixVariable2 == 0:
                    sousMenu1 = False

                elif choixVariable2 == 1:
                    dataframePartition = creerPartition(dataframePartition)

                elif choixVariable2 == 2:
                    modifierPartition(dataframePartition)

                elif choixVariable2 == 3:
                    supprimerPartition(dataframePartition)

            elif choixVariable1 == 2:
                menuAffichage()
                choixVariable2 = choix(3)

                if choixVariable2 == 0:
                    sousMenu1 = False

                elif choixVariable2 == 1:
                    menuAffichage2()
                    choixOrdre = choix(3)
                    choixCritere = masqueDeSaisie().upper()
                    print(afficherTouteData(dataframePartition, choixOrdre, choixCritere).to_string())

                elif choixVariable2 == 2:
                    menuAffichage2bis()
                    choixColonne = masqueDeSaisie().upper()
                    print("Veuillez ensuite entrer le mot clé de votre recherche")
                    motCle = masqueDeSaisie()
                    if choixColonne == "COMPOSITEUR":
                        afficherRechercheData(dataframePartition, motCle, dataframeCompositeurs, "COMPOSITIONS")
                    elif choixColonne == "INSTRUMENT":
                        afficherRechercheData(dataframePartition, motCle, dataframeInstruments, "OEUVRES")
                    elif choixColonne == "TONALITÉ":
                        afficherRechercheData(dataframePartition, motCle, dataframeTonalites, "OEUVRES")
                sousMenu1 = False
