import jsonpickle
from modeles.joueur import Joueur

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
