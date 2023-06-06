import jsonpickle
import re
from datetime import datetime

class GestionnaireJoueurs:
    FILE_PATH = 'Liste_de_joueurs.json'

    @staticmethod
    def enregistrer(joueur):
        joueurs = GestionnaireJoueurs.charger()
        joueurs.append(joueur)
        with open(GestionnaireJoueurs.FILE_PATH, 'w') as file:
            file.write(jsonpickle.encode(joueurs))

    @staticmethod
    def charger():
        try:
            with open(GestionnaireJoueurs.FILE_PATH, 'r') as file:
                return jsonpickle.decode(file.read())
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def supprimer_joueur(identifiant_national):
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
            print("Le joueur n'a pas été trouvé.")
        
    @staticmethod
    def charger_joueur_par_identifiant_national(identifiant_national):
        joueurs = GestionnaireJoueurs.charger()
        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                return joueur
        return None

    @staticmethod
    def joueur_existe(identifiant_national):
        joueurs = GestionnaireJoueurs.charger()
        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                return True
        return False

    @staticmethod
    def verifier_identifiant_national():
        while True:
            identifiant_national = input("Identifiant National : ")
            if re.match(r"^[A-Z]{2}\d{5}$", identifiant_national):
                return identifiant_national
            else:
                print("Identifiant national invalide. Veuillez entrer un nombre de 15 chiffres.")
    
    @staticmethod
    def verifier_date_naissance():
        while True:
            date_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(date_naissance, "%d/%m/%Y")
                return date_naissance
            except ValueError:
                print("Date de naissance invalide. Veuillez entrer une date au format JJ/MM/AAAA.")