import re
from datetime import datetime
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs
from vues.joueur_vues import VuesJoueur



class PlayerController:
    
    @staticmethod
    def supprimer_joueur():
        """
        Demande à l'utilisateur d'entrer l'identifiant national du joueur à supprimer, puis supprime le joueur correspondant.
        """
        identifiant_national = input("Entrez l'identifiant national du joueur à supprimer : ")
        if not GestionnaireJoueurs.joueur_existe(identifiant_national):
            VuesJoueur.joueur_exist_pas()
            return None
        GestionnaireJoueurs.supprimer_joueur(identifiant_national)
        VuesJoueur.joueur_supprime_avec_succes(identifiant_national)
        return None

    @staticmethod
    def verifier_nom():
        """
        Demande à l'utilisateur d'entrer un nom et le vérifie.
        """
        while True:
            nom = input("Nom : ").strip()  
            if nom:  
                return nom
            else:
                VuesJoueur.champ_vide()

    @staticmethod
    def verifier_prenom():
        """
        Demande à l'utilisateur d'entrer un prénom et le vérifie.
        """
        while True:
            prenom = input("Prénom : ").strip()  
            if prenom:  
                return prenom
            else:
                VuesJoueur.champ_vide()