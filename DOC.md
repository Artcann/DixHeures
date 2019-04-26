# DOCUMENTATION DixHeures

## Présentation

Vous êtes ici dans la documentation des modules de ce programme,
ceci est un document technique, pour plus d'informations sur le 
fonctionnement du programme sans les détails techniques, veuillez
lire le README qui se trouve à la racine du projet.

## Les Modules

Le programme comporte deux modules, le premier, fonctions_menu, 
permet de gérer l'affichage des informations, tandis que 
fonctions_partitions est un module qui gère la manipulation
des DataFrames à partir des données receuillies dans main.py.

## fonctions_menu

#### choix(nb_choix)

Cette première fonction a en paramètre le nombre de choix attendu, puis demande à
l'utilisateur de rentrer un chiffre compris entre 0 et le nombre de choix possibles,
La fonction teste si l'utilisateur a bien rentré un nombre, et s'il est bien compris entre
0 et le nombre de choix attendu alors la fonction retourne le nombre rentré par l'utilisateur.

#### menuXXX()

Cette fonction ne possède pas de paramètre et se contente d'afficher le menu XXX

XXX étant à remplacer par le menu afficher, la liste des menu étant pour l'instant:  
Authentification  
Principal  
Edition  
Affichage  
Affichage2  
Affichage2bis


## fonctions_partitions

####authentification(dico,testSecu)

Cette fonction prend en paramètre le dico avec les HASH de Mot de Passe et les Sels qui
vont avec.  
La fonction demande à l'utilisateur d'entrer son Identifiant et son Mot de Passe.  
Elle récupère ensuite le sel associé à l'utilisateur puis concatène le Sel récupéré et le
Mot de Passe entré par l'utilisateur, elle HASH ensuite la chaîne obtenu grâce à la fonction
de Hachage SHA512. Elle n'a plus qu'a vérifié si le HASH obtenu correspond au HASH enregistré
dans le dico, si c'est le cas l'utilisateur est authentifié, sinon un message d'erreur est envoyé
et il doit retenter de se connecter.

#### creationCompte(dico)

Cette fonction prend en paramètre le dico avec les HASH de Mot de Passe et les Sels qui vont
avec.  
La fonction demande à l'utilisateur d'entrer son Identifiant et son Mot de Passe.
Elle génère ensuite une chaine aléatoire de 16 caractères Hexadécimaux, c'est le Sel de cet
utilisateur. Elle concatène le Sel et le Mot de Passe puis les passe dans la fonction de Hachage
SHA512. Elle écrit la combinaison ID, Mot de Passe et Sel sur le Disque puis l'ajoute dans 
le Dico, le compte utilisateur est crée.