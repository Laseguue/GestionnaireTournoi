
class VuesJoueur:
    @staticmethod
    def info_joueur():
        """
        Invite l'utilisateur à entrer les informations du joueur.
        """
        print("Entrez les informations du joueur :")

    @staticmethod
    def joueur_exist_deja():
        """
        Informe que le joueur avec cet identifiant national existe déjà.
        """
        print("Un joueur avec cet identifiant national existe déjà.")
    
    @staticmethod
    def joueur_exist_pas():
        """
        Informe que le joueur recherché n'existe pas ou n'a pas été trouvé.
        """
        print("Ce joueur n'existe pas ou n'as pas était trouvé.")

    @staticmethod
    def joueur_enregistre_avec_succes(nom):
        """
        Informe que le joueur a été enregistré avec succès.
        """
        print(f"Joueur {nom} enregistré avec succès.")
    
    @staticmethod
    def joueur_supprime_avec_succes(identifiant_national):
        """
        Informe que le joueur a été supprimé avec succès.
        """
        print(f"Joueur avec l'identifiant national {identifiant_national} a été supprimé avec succès.")
    
    @staticmethod
    def identifiant_invalide():
        """
        Informe que l'identifiant national entré est invalide.
        """
        print("Identifiant national invalide. Veuillez entrer deux lettres suivis de 5 chiffres.")

    @staticmethod
    def date_naissance_invalide():
        """
        Informe que la date de naissance entrée est invalide.
        """
        print("Date de naissance invalide. Veuillez entrer une date au format JJ/MM/AAAA.")
    
    @staticmethod
    def champ_vide():
        """
        Informe que le champ est vide et invite l'utilisateur à entrer une donnée valide.
        """
        print("Le champ est vide veuillez entrer une donnée valide.")