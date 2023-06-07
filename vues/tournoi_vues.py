
class VuesTournoi:
    @staticmethod
    def saisi_info_tournoi():
        """
        Invite l'utilisateur à entrer les informations du tournoi.
        """
        print("Entrez les informations du tournoi :")
    
    @staticmethod
    def succes_suprimer():
        """
        Informe que le tournoi a été supprimé avec succès
        """
        print("Tournoi supprimé avec succès.")
    
    @staticmethod
    def tournoi_introuvable():
        """
        Informe que le tournoi recherché n'a pas été trouvé
        """
        print("Le tournoi n'a pas été trouvé.")
    
    @staticmethod
    def joueur_ajoute(nom_joueur, nom_tournoi):
        """
        Informe qu'un joueur a été ajouté à un tournoi avec succès
        """
        print(f"Le joueur {nom_joueur} à étais ajouté au tournoi {nom_tournoi} avec succes.\n")

    @staticmethod
    def joueur_non_trouve(identifiant_national):
        """
        Informe qu'aucun joueur avec un certain identifiant national n'a été trouvé
        """
        print(f"Aucun joueur trouvé avec l'identifiant national {identifiant_national}")
        
    @staticmethod
    def debut_tour(num_tour):
        """
        Informe qu'un nouveau tour a commencé
        """
        print(f"Le tour {num_tour} a commencé.")
    
    @staticmethod
    def max_tours():
        """
        Informe que le tournoi a atteint le nombre maximum de tours ou est terminé.
        """
        print("Le tournoi a atteint le nombre maximum de tours ou est terminé.")
    
    @staticmethod
    def match_sans_resultat():
        """
        Informe qu'il y a encore des matchs sans résultats dans le tour actuel
        """
        print("Il y a encore des matchs sans résultats dans le tour actuel. Veuillez entrer tous les résultats avant de commencer un nouveau tour.")
    
    @staticmethod
    def info_match(id_match, nom_joueur1, nom_joueur2):
        """
        Affiche les informations d'un match
        """
        print(f"Match {id_match} : {nom_joueur1} vs {nom_joueur2}")

    @staticmethod
    def resultat_invalide():
        """
        Informe que le résultat entré est invalide
        """
        print("Résultat invalide. Veuillez entrer un nombre valide (0, 0.5, 1).")

    @staticmethod
    def entree_invalide():
        """
        Informe que l'entrée est invalide
        """
        print("Entrée invalide. Veuillez entrer un nombre valide.")
    
    @staticmethod
    def choix_vide():
        """
        Informe que le choix ne peut pas être vide.
        """
        print("Le choix ne peut pas être vide.")
    
    @staticmethod
    def date_invalide():
        """
        Informe que la date de début doit être au format JJ/MM/AAAA.
        """
        print("La date de début doit être au format JJ/MM/AAAA.")
    
    @staticmethod
    def nombre_invalide():
        """
        Informe que le nombre de tours doit être un entier positif.
        """
        print("Le nombre de tours doit être un entier positif.")
    
