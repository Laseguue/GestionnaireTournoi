import json
from modeles.joueur import Joueur


class GestionnaireDonnees:
    @staticmethod
    def enregistrer_joueur(joueur):
        try:
            with open('Liste_de_joueurs.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(joueur.__dict__)

        with open('Liste_de_joueurs.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def charger_joueurs():
        try:
            with open('Liste_de_joueurs.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        joueurs = [Joueur(**joueur_data) for joueur_data in data]

        return joueurs

    @staticmethod
    def supprimer_joueur(identifiant_national):
        joueurs = GestionnaireDonnees.charger_joueurs()
        joueur_trouve = False

        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                joueurs.remove(joueur)
                joueur_trouve = True
                break

        if joueur_trouve:
            with open('Liste_de_joueurs.json', 'w') as file:
                json.dump([joueur.__dict__ for joueur in joueurs], file, indent=4, ensure_ascii=False)
            print("Joueur supprimé avec succès.")
        else:
            print("Le joueur n'a pas été trouvé.")
    
    @staticmethod
    def joueur_existe(identifiant_national):
        joueurs = GestionnaireDonnees.charger_joueurs()

        for joueur in joueurs:
            if joueur.identifiant_national == identifiant_national:
                return True

        return False