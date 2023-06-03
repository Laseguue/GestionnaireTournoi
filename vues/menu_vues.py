class MenuVues:
    @staticmethod
    def afficher_menu_principal():
        print("\n*** Menu principal ***")
        print("1. Menu Tournoi")
        print("2. Menu Joueur")
        print("3. Menu Rapport")
        print("4. Quitter")
        choix = input("Choisissez une option : ")
        return choix
    
    @staticmethod
    def afficher_menu_rapport():
        print("1. Afficher la liste de tous les joueurs")
        print("2. Afficher la liste de tous les tournois")
        print("3. Rechercher un tournoi par son nom")
        print("4. Afficher la liste des joueurs d'un tournoi")
        print("5. Afficher la liste de tous les tours et matchs d'un tournoi")
        print("6. Génerer un rapport de tournois txt")
        print("7. Retourner au menu principal")
        option = input("Choisissez une option : ")
        return option

    @staticmethod
    def afficher_menu_joueur():
        print("1. Créer un nouveau joueur")
        print("2. Supprimer un joueur existant")
        print("3. Retourner au menu principal")
        choix = input("Choisissez une option : ")
        return choix
    
    @staticmethod
    def afficher_menu_tournoi():
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter un joueur à un tournoi existant")
        print("3. Lancer ou reprendre un tournoi existant")
        print("4. Supprimer un tournoi")
        print("5. Retourner au menu principal")
        choix = input("Choisissez une option : ")
        return choix