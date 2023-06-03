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
