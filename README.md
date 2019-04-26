# DixHeures


## Présentation du projet
DixHeures est un moteur de recherche de musique classique
enregistrée dans notre base de donnée. Ce moteur de recherche
propose une gestion de sessions et donc de favoris, propre à
chaque utilisateur.


## Contributeur 

Arthur CANN, étudiant en première année de prépa à l'ISEP  
Constant CROCHET, étudiant en première année de prépa à l'ISEP  
Thibault CHANIER, étudiant en première année de prépa à l'ISEP  
Casimir BORGEAUD, étudian en première année de prépa à l'ISEP

## Pré-Requis

Le projet à été codé sur Python 3 et utilise nos base de données
qui sont de simples fichier CSV. Vous pouvez creer vos propre
CSV à condition que leurs structures respecte la notre.

## Utilisation

Lors du lancement du programme on vous demande de vous connecter,
si vous ne possedez pas de compte il vous suffit d'en creer un.
Une fois que vous êtes authentifié, vous avez le choix entre 
rechercher des partitions ou en éditer. Vous pouvez en effet
creer, modifier ou supprimer des partitions de la base de données.

Si vous décider par exemple de selectionner "Créer une partition"
on vous demandera de remplir un formulaire avec toutes les informations
nécessaire à la création d'une nouvelle partition. Idem pour la
modification. Pour supprimer vous aurez juste à taper le nom de 
la partition à supprimer.

## Fonctionnement et fonctionnalités

Le programme est basé sur l'utilisation de DataFrames qui sont des
objets de la bibliothèque Pandas. Nous créons nos DataFrames à
partir de fichier CSV qui contiennent les infos sur les partitions. 
 
Afin d'améliorer la rapidité de la recherche et de permettre la
manipulation de grande base de données, nous n'utilisons pas
qu'un seul CSV, nous avons un CSV par critère de recherche important.
Il y a une DataFrames principale qui liste toutes les oeuvres, et
qui par exemple pour les compositeurs, associe chaque compositeur
à un ID, cet ID se retrouve dans la DataFrame des compositeur.
Dans cette dernière chaque compositeur est associé à un ID ainsi qu'à
toute ses oeuvres, de ce fait lorsque l'utilisateur recherche les
oeuvres de Mozart, au lieu de parcourir toute la DataFrame principale
à la recherche de partitions de Mozart, le programme va chercher Mozart
dans la DataFrame compositeurs et va afficher toute les oeuvres qui
sont associé à Mozart.

Notre programme propose également une gestion sécurisée des mots 
de passe de session des utilisateurs. En effet chaque utilisateur
dispose d'un compte où il peut enregistrer ses partitions favorites
qu'il retrouvera à sa prochaine connexion. Afin de sécurisé nos
mot de passe nous utilisons des HASH salé, en l'occurence nous
salons des HASH de SHA256. Des HASH sont des chaines de caractères
données par des fonctions de Hachage, ces fonctions transforment
les mots de passe en HASH, chaque mot de passe a son HASH associé
et on ne peut pas inverser la procédure, c'est à dire qu'on ne 
peut pas retrouver un mot de passe à partir d'un HASH. Le salage
est en fait l'ajout d'une chaine de caractère aléatoire à chaque mot
de passe afin d'éviter que deux mots de passe aient les même HASH.
Une fois les HASH enregistré dans notre base de donnée, il suffit à
chaque tentative de connexion de HASH le mot de passe tapé par 
l'utilisateur et de vérifier qu'il correspond bien au HASH enregistré
pour cet utilisateur.

