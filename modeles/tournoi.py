import uuid
import hashlib

class Tournoi:
    def __init__(self, id, nom, lieu, date_debut, date_fin, nb_tours, tours=[], joueurs=[], num_tour_actuel=0, description=''):
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
        print("Entrez les informations du tournoi :")

        id = Tournoi.generer_id_unique() 
        nom = input("Nom : ")
        lieu = input("Lieu : ")
        date_debut = input("Date de début (JJ/MM/AAAA) : ")
        date_fin = input("Date de fin (JJ/MM/AAAA) : ")
        nb_tours = int(input("Nombre de tours : "))
        description = input("Description : ")

        tournoi = cls(id, nom, lieu, date_debut, date_fin, nb_tours=4, description=description)

        return tournoi

    @staticmethod
    def generer_id_unique():
        return str(uuid.uuid4())
