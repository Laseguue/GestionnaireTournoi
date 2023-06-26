Tournoi d'échecs Ce programme est conçu pour gérer des tournois d'échecs. Il permet d'enregistrer les détails du tournoi, les joueurs, les matchs et de générer des rapports en fin de tournoi.

Installation Clonez ce dépôt sur votre machine locale en utilisant git clone https://github.com/utilisateur/nom-du-depot.git

Naviguez jusqu'au répertoire du projet avec cd tournoi-echecs

Installez les dépendances avec pip install -r requirements.txt

Exécution du programme Pour exécuter le programme, naviguez jusqu'au répertoire du projet et exécutez le fichier Start.py avec la commande "python -m Start.py".

Suivez les instructions à l'écran pour naviguer dans le menu et utiliser les différentes fonctionnalités du programme.

Utilisation du programme Joueur.py : Permet de créer un joueur avec son nom, prénom, date de naissance, sexe et classement.

Tour.py : Permet de créer un tour de matchs.

Tournoi.py : Permet de créer un tournoi, d'ajouter des joueurs et des tours, et d'enregistrer les résultats.

Menu.py : C'est le point d'entrée du programme. Il permet de naviguer dans les différentes options et fonctionnalités.

Une fois lancé, le programme affichera un menu avec les options suivantes :

Le menu principal est une partie essentielle du programme. Il propose les fonctionnalités suivantes :

Menu Tournoi
Menu Joueur
Menu Rapport
Quitter
Le menu Tournoi propose les options suivantes :

Créer un nouveau tournoi
Ajouter un joueur à un tournoi existant
Lancer ou reprendre un tournoi existant
Supprimer un tournoi
Retourner au menu principal
Le menu Joueur propose les options suivantes :

Créer un nouveau joueur
Supprimer un joueur existant
Retourner au menu principal
Le menu Rapport propose les options suivantes :

Afficher la liste de tous les joueurs
Afficher la liste de tous les tournois
Rechercher un tournoi par son nom
Afficher la liste des joueurs d'un tournoi
Afficher la liste de tous les tours et matchs d'un tournoi
Générer un rapport de tournois txt
Retourner au menu principal
Utilisez les options des menus pour interagir avec le programme et bénéficier de ses fonctionnalités.

Génération d'un rapport Flake8 HTML Flake8 est un outil qui nous aide à maintenir la qualité de notre code. Pour générer un rapport HTML Flake8, suivez ces étapes :

Installez flake8 et flake8-html avec la commande pip install flake8 flake8-html

Exécutez Flake8 avec le format de rapport html en utilisant la commande flake8 --format=html --htmldir=flake8_report

Un nouveau répertoire appelé flake8_report sera créé. Ouvrez index.html dans ce répertoire pour afficher le rapport.

