
class VuesJoueur:
    @staticmethod
    def info_joueur():
        """
        Invite l'utilisateur à entrer les informations du joueur.
        """
        print("\n----- Entrez les informations du joueur : -----")

    @staticmethod
    def joueur_exist_deja():
        """
        Informe que le joueur avec cet identifiant national existe déjà.
        """
        print("\n*** Un joueur avec cet identifiant national existe déjà. ***")

    @staticmethod
    def joueur_exist_pas():
        """
        Informe que le joueur recherché n'existe pas ou n'a pas été trouvé.
        """
        print("\n*** Ce joueur n'existe pas ou n'as pas été trouvé. ***")

    @staticmethod
    def joueur_enregistre_avec_succes(nom):
        """
        Informe que le joueur a été enregistré avec succès.
        """
        print(f"\n*** Joueur {nom} enregistré avec succès. ***")

    @staticmethod
    def joueur_supprime_avec_succes(identifiant_national):
        """
        Informe que le joueur a été supprimé avec succès.
        """
        print(f"\n*** Joueur avec l'identifiant national {identifiant_national} a été supprimé avec succès. ***")

    @staticmethod
    def identifiant_invalide():
        """
        Informe que l'identifiant national entré est invalide.
        """
        print("\n*** Identifiant national invalide. Veuillez entrer deux lettres suivis de 5 chiffres. ***")

    @staticmethod
    def date_naissance_invalide():
        """
        Informe que la date de naissance entrée est invalide.
        """
        print("\n*** Date de naissance invalide. Veuillez entrer une date au format JJ/MM/AAAA. ***")

    @staticmethod
    def champ_vide():
        """
        Informe que le champ est vide et invite l'utilisateur à entrer une donnée valide.
        """
        print("\n*** Le champ est vide veuillez entrer une donnée valide. ***")
