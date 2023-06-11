import jsonpickle
import datetime
from vues.tournoi_vues import VuesTournoi


class GestionnaireTournois:
    FILE_PATH = 'Liste_de_tournois.json'

    @staticmethod
    def enregistrer(tournoi):
        """
        Enregistre un tournoi dans un fichier JSON.
        """
        tournois = GestionnaireTournois.charger()
        tournoi_index = next((index for (index, t) in enumerate(tournois) if t.id == tournoi.id), None)

        if tournoi_index is not None:
            tournois[tournoi_index] = tournoi
        else:
            tournois.append(tournoi)

        with open(GestionnaireTournois.FILE_PATH, 'w') as file:
            file.write(jsonpickle.encode(tournois))

    @staticmethod
    def charger():
        """
        Charge la liste des tournois à partir d'un fichier JSON.
        """
        try:
            with open(GestionnaireTournois.FILE_PATH, 'r') as file:
                return jsonpickle.decode(file.read())
        except (FileNotFoundError, jsonpickle.UnpicklingError):
            return []

    @staticmethod
    def supprimer_tournoi(nom_tournoi):
        """
        Supprime un tournoi spécifique de la liste des tournois et met à jour le fichier JSON.
        """
        tournois = GestionnaireTournois.charger()
        tournoi_trouve = False

        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                tournois.remove(tournoi)
                tournoi_trouve = True
                break

        if tournoi_trouve:
            with open('Liste_de_tournois.json', 'w') as file:
                file.write(jsonpickle.encode(tournois))
            VuesTournoi.succes_suprimer()
        else:
            VuesTournoi.tournoi_introuvable()

    @staticmethod
    def charger_tournoi_par_nom(nom):
        """
        Charge un tournoi spécifique par son nom à partir de la liste des tournois.
        """
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom:
                return tournoi
        return None

    @staticmethod
    def valider_nom(nom):
        """
        Vérifie si le nom donné est valide.
        """
        return bool(nom)

    @staticmethod
    def valider_lieu(lieu):
        """
        Vérifie si le lieu donné est valide.
        """
        return bool(lieu)

    @staticmethod
    def valider_date(date_text, date_format="%d/%m/%Y"):
        """
        Vérifie si la date donnée est valide.
        """
        try:
            datetime.datetime.strptime(date_text, date_format)
            return True
        except ValueError:
            return False

    @staticmethod
    def valider_nb_tours(nb_tours):
        """
        Vérifie si le nombre de tours donné est valide.
        """
        return nb_tours.isdigit() and int(nb_tours) > 0
