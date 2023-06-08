class MenuVues:
    @staticmethod
    def afficher_menu(options):
        """
        Affiche le menu à partir d'une liste d'options et invite l'utilisateur à choisir une option.
        """
        for option in options:
            print(option)
        choix = input("Choisissez une option : ")
        return choix

    @staticmethod
    def afficher_menu_principal():
        """
        Affiche le menu principal et invite l'utilisateur à choisir une option.
        """
        options = [
            "\n*** Menu principal ***",
            "1. Menu Tournoi",
            "2. Menu Joueur",
            "3. Menu Rapport",
            "4. Quitter",
        ]
        return MenuVues.afficher_menu(options)
    
    @staticmethod
    def afficher_menu_rapport():
        """
        Affiche le menu de rapport et invite l'utilisateur à choisir une option.
        """
        options = [
            "1. Afficher la liste de tous les joueurs",
            "2. Afficher la liste de tous les tournois",
            "3. Rechercher un tournoi par son nom",
            "4. Afficher la liste des joueurs d'un tournoi",
            "5. Afficher la liste de tous les tours et matchs d'un tournoi",
            "6. Génerer un rapport de tournois txt",
            "7. Retourner au menu principal",
        ]
        return MenuVues.afficher_menu(options)

    @staticmethod
    def afficher_menu_joueur():
        """
        Affiche le menu du joueur et invite l'utilisateur à choisir une option.
        """
        options = [
            "1. Créer un nouveau joueur",
            "2. Supprimer un joueur existant",
            "3. Retourner au menu principal",
        ]
        return MenuVues.afficher_menu(options)
    
    @staticmethod
    def afficher_menu_tournoi():
        """
        Affiche le menu du tournoi et invite l'utilisateur à choisir une option.
        """
        options = [
            "1. Créer un nouveau tournoi",
            "2. Ajouter un joueur à un tournoi existant",
            "3. Lancer ou reprendre un tournoi existant",
            "4. Supprimer un tournoi",
            "5. Retourner au menu principal",
        ]
        return MenuVues.afficher_menu(options)
    
    @staticmethod
    def choix_invalid():
        """
        Informe que l'option choisie est invalide.
        """
        print("\nOption invalide. Veuillez choisir une option valide.\n")
    
    @staticmethod
    def nombre_tour_invalide():
        """
        Informe que le tournoi doit avoir au moins deux joueurs pour être lancé.
        """
        print("\nLe tournoi doit avoir au moins deux joueurs pour être lancé.\n")
    
    @staticmethod
    def afficher_succes_creation_tournoi(nom_tournoi):
        """
        Informe que le tournoi a été créé avec succès.
        """
        print(f"\nLe tournoi {nom_tournoi} a été créé avec succès.\n")
    
    @staticmethod
    def quitter_programme():
        """
        Informe que le programme se termine.
        """
        print("\nAu revoir !\n")