import uuid
import hashlib
from vues.tournoi_vues import VuesTournoi
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois

class Tournoi:
    def __init__(self, id, nom, lieu, date_debut, date_fin, nb_tours=4, tours=[], joueurs=[], num_tour_actuel=0, description=''):
        """
        Initialise un nouveau tournoi.
        """
        self.id = id
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.tours = tours
        self.joueurs = joueurs
        self.num_tour_actuel = num_tour_actuel
        self.description = description

    @classmethod
    def creer_tournoi(cls):
        """
        Crée un nouveau tournoi à partir des informations fournies par l'utilisateur.
        """
        VuesTournoi.saisi_info_tournoi
        id = Tournoi.generer_id_unique()
        nom = input("Nom : ")
        while not GestionnaireTournois.valider_nom(nom):
            VuesTournoi.choix_vide()
            nom = input("Nom : ")
        lieu = input("Lieu : ")
        while not GestionnaireTournois.valider_lieu(lieu):
            VuesTournoi.choix_vide()
            lieu = input("Lieu : ")
        date_debut = input("Date de début (JJ/MM/AAAA) : ")
        while not GestionnaireTournois.valider_date(date_debut):
            VuesTournoi.date_invalide()
            date_debut = input("Date de début (JJ/MM/AAAA) : ")
        date_fin = input("Date de fin (JJ/MM/AAAA) : ")
        while not GestionnaireTournois.valider_date(date_fin):
            date_invalide()
            date_fin = input("Date de fin (JJ/MM/AAAA) : ")
        nb_tours = input("Nombre de tours : ")
        while nb_tours and not GestionnaireTournois.valider_nb_tours(nb_tours):
            VuesTournoi.nombre_invalide()
            nb_tours = input("Nombre de tours : ")
        nb_tours = int(nb_tours) if nb_tours else 4
        description = input("Description : ")
        tournoi = cls(id, nom, lieu, date_debut, date_fin, nb_tours, description=description)
        return tournoi

    @staticmethod
    def generer_id_unique():
        """
        Génère un identifiant unique pour le tournoi.
        """
        return str(uuid.uuid4())
