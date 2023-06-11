import jsonpickle
import re
from datetime import datetime
from vues.joueur_vues import VuesJoueur


class GestionnaireJoueurs:
    FILE_PATH = 'Liste_de_joueurs.json'

    @staticmethod
    def enregistrer(joueur):
        """
        Enregistre un joueur dans un fichier JSON.
        """
        joueurs = GestionnaireJoueurs.charger()
        joueurs.append(joueur)
        with open(GestionnaireJoueurs.FILE_PATH, 'w') as file:
            file.write(jsonpickle.encode(joueurs))

    @staticmethod
    def charger():
        """
        Charge la liste des joueurs à partir d'un fichier JSON.
        """
        try:
            with open(GestionnaireJoueurs.FILE_PATH, 'r') as file:
                return jsonpickle.decode(file.read())
        except (FileNotFoundError, jsonpickle.UnpicklingError):
            return []

    @staticmethod
    def supprimer_joueur(identifiant_national):
        """
        Supprime un joueur spécifique de la liste des joueurs et met à jour le fichier JSON.
        """
        joueurs = GestionnaireJoueurs.charger()
        joueur_trouve = False

        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                joueurs.remove(joueur)
                joueur_trouve = True
                break

        if joueur_trouve:
            with open('Liste_de_joueurs.json', 'w') as file:
                file.write(jsonpickle.encode(joueurs))
        else:
            VuesJoueur.joueur_exist_pas()

    @staticmethod
    def charger_joueur_par_identifiant_national(identifiant_national):
        """
        Charge un joueur spécifique par son identifiant national à partir de la liste des joueurs.
        """
        joueurs = GestionnaireJoueurs.charger()
        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                return joueur
        return None

    @staticmethod
    def joueur_existe(identifiant_national):
        """
        Vérifie si un joueur existe dans la liste des joueurs en utilisant son identifiant national.
        """
        joueurs = GestionnaireJoueurs.charger()
        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                return True
        return False

    @staticmethod
    def verifier_identifiant_national():
        """
        Vérifie si l'identifiant national entré est valide.
        """
        while True:
            identifiant_national = input("Identifiant National : ")
            if re.match(r"^[A-Z]{2}\d{5}$", identifiant_national):
                return identifiant_national
            else:
                VuesJoueur.identifiant_invalide()

    @staticmethod
    def verifier_date_naissance():
        """
        Vérifie si la date de naissance entrée est valide.
        """
        while True:
            date_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(date_naissance, "%d/%m/%Y")
                return date_naissance
            except ValueError:
                VuesJoueur.date_naissance_invalide()
