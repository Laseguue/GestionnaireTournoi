class MenuVues:
    @staticmethod
    def afficher_menu_principal():
        """
        Affiche le menu principal et invite l'utilisateur à choisir une option.
        """
        print("\n*** Menu principal ***")
        print("1. Menu Tournoi")
        print("2. Menu Joueur")
        print("3. Menu Rapport")
        print("4. Quitter")
        choix = input("Choisissez une option : ")
        return choix
    
    @staticmethod
    def afficher_menu_rapport():
        """
        Affiche le menu de rapport et invite l'utilisateur à choisir une option.
        """
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
        """
        Affiche le menu du joueur et invite l'utilisateur à choisir une option.
        """
        print("1. Créer un nouveau joueur")
        print("2. Supprimer un joueur existant")
        print("3. Retourner au menu principal")
        choix = input("Choisissez une option : ")
        return choix
    
    @staticmethod
    def afficher_menu_tournoi():
        """
        Affiche le menu du tournoi et invite l'utilisateur à choisir une option.
        """
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter un joueur à un tournoi existant")
        print("3. Lancer ou reprendre un tournoi existant")
        print("4. Supprimer un tournoi")
        print("5. Retourner au menu principal")
        choix = input("Choisissez une option : ")
        return choix
    
    @staticmethod
    def choix_invalid():
        """
        Informe que l'option choisie est invalide.
        """
        print("Option invalide. Veuillez choisir une option valide.")
    
    @staticmethod
    def nombre_tour_invalide():
        """
        Informe que le tournoi doit avoir au moins deux joueurs pour être lancé.
        """
        print("Le tournoi doit avoir au moins deux joueurs pour être lancé.")
    
    @staticmethod
    def afficher_succes_creation_tournoi(nom_tournoi):
        """
        Informe que le tournoi a été créé avec succès.
        """
        print(f"Le tournoi {nom_tournoi} a été créé avec succès.\n")
    
    @staticmethod
    def quitter_programme():
        """
        Informe que le programme se termine.
        """
        print("Au revoir !")