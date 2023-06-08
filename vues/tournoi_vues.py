
class VuesTournoi:
    @staticmethod
    def saisi_info_tournoi():
        """
        Invite l'utilisateur à entrer les informations du tournoi.
        """
        print("\nEntrez les informations du tournoi :\n")
    
    @staticmethod
    def succes_suprimer():
        """
        Informe que le tournoi a été supprimé avec succès
        """
        print("\nTournoi supprimé avec succès.\n")
    
    @staticmethod
    def tournoi_introuvable():
        """
        Informe que le tournoi recherché n'a pas été trouvé
        """
        print("\nLe tournoi n'a pas été trouvé.\n")
    
    @staticmethod
    def joueur_ajoute(nom_joueur, nom_tournoi):
        """
        Informe qu'un joueur a été ajouté à un tournoi avec succès
        """
        print(f"\nLe joueur {nom_joueur} à étais ajouté au tournoi {nom_tournoi} avec succes.\n")

    @staticmethod
    def joueur_non_trouve(identifiant_national):
        """
        Informe qu'aucun joueur avec un certain identifiant national n'a été trouvé
        """
        print(f"\nAucun joueur trouvé avec l'identifiant national {identifiant_national}\n")
        
    @staticmethod
    def debut_tour(num_tour):
        """
        Informe qu'un nouveau tour a commencé
        """
        print(f"\nLe tour {num_tour} a commencé.\n")
    
    @staticmethod
    def max_tours():
        """
        Informe que le tournoi a atteint le nombre maximum de tours ou est terminé.
        """
        print("\nLe tournoi a atteint le nombre maximum de tours ou est terminé.\n")
    
    @staticmethod
    def match_sans_resultat():
        """
        Informe qu'il y a encore des matchs sans résultats dans le tour actuel
        """
        print("\nIl y a encore des matchs sans résultats dans le tour actuel. Veuillez entrer tous les résultats avant de commencer un nouveau tour.\n")
    
    @staticmethod
    def info_match(id_match, nom_joueur1, nom_joueur2):
        """
        Affiche les informations d'un match
        """
        print(f"\nMatch {id_match} : {nom_joueur1} vs {nom_joueur2}\n")

    @staticmethod
    def resultat_invalide():
        """
        Informe que le résultat entré est invalide
        """
        print("\nRésultat invalide. Veuillez entrer un nombre valide (0, 0.5, 1).\n")

    @staticmethod
    def entree_invalide():
        """
        Informe que l'entrée est invalide
        """
        print("\nEntrée invalide. Veuillez entrer un nombre valide.\n")
    
    @staticmethod
    def choix_vide():
        """
        Informe que le choix ne peut pas être vide.
        """
        print("\nLe choix ne peut pas être vide.\n")
    
    @staticmethod
    def date_invalide():
        """
        Informe que la date de début doit être au format JJ/MM/AAAA.
        """
        print("\nLa date de début doit être au format JJ/MM/AAAA.\n")
    
    @staticmethod
    def nombre_invalide():
        """
        Informe que le nombre de tours doit être un entier positif.
        """
        print("\nLe nombre de tours doit être un entier positif.\n")
    
