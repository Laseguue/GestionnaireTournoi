import re
from datetime import datetime
from modeles.joueur import Joueur
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs


class PlayerController:
    @staticmethod
    def creer_joueur():
        print("Entrez les informations du joueur :")
        identifiant_national = PlayerController._verifier_identifiant_national()
        
        if GestionnaireJoueurs.joueur_existe(identifiant_national):
            print("Un joueur avec cet identifiant national existe déjà.")
            return None

        nom = input("Nom : ")
        prenom = input("Prénom : ")
        date_naissance = PlayerController._verifier_date_naissance()

        nouveau_joueur = Joueur.generate_joueur(identifiant_national, nom, prenom, date_naissance)
        
        GestionnaireJoueurs.enregistrer(nouveau_joueur)

        print(f"Joueur {nouveau_joueur.nom} enregistré avec succès.")

        return nouveau_joueur
    
    @staticmethod
    def supprimer_joueur():
        identifiant_national = input("Entrez l'identifiant national du joueur à supprimer : ")

        if not GestionnaireJoueurs.joueur_existe(identifiant_national):
            print("Aucun joueur avec cet identifiant national n'existe.")
            return None

        GestionnaireJoueurs.supprimer_joueur(identifiant_national)

        print(f"Joueur avec l'identifiant national {identifiant_national} a été supprimé avec succès.")

        return None

    @staticmethod
    def _verifier_identifiant_national():
        while True:
            identifiant_national = input("Identifiant national (Deux lettres suivies de cinq chiffres, par exemple AB12345) : ")
            if re.match(r'^[a-zA-Z]{2}\d{5}$', identifiant_national):
                return identifiant_national
            else:
                print("Format de l'identifiant national incorrect, veuillez réessayer.")

    @staticmethod
    def _verifier_date_naissance():
        while True:
            date_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(date_naissance, '%d/%m/%Y')
                return date_naissance
            except ValueError:
                print("Format de la date de naissance incorrect, veuillez réessayer.")
