import uuid
import random
from controleurs.tournoi_control import TournoiController
from vues.tournoi_vues import VuesTournoi
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from modeles.tour import Tour
from modeles.match import Match


class Tournoi:
    def __init__(self, id, nom, lieu, date_debut, date_fin, nb_tours=4,
                 tours=[], joueurs=[], num_tour_actuel=0, description=''):
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
            VuesTournoi.date_invalide()
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

    def commencer(self):
        """
        Commence le tournoi.
        """
        random.shuffle(self.joueurs)
        self.creer_tour()
        self.saisir_resultat_tour()
        GestionnaireTournois.enregistrer(self)

    def continuer(self):
        """
        Continue le tournoi.
        """
        self.joueurs.sort(key=lambda j: j.score, reverse=True)
        self.creer_tour()
        self.saisir_resultat_tour()
        GestionnaireTournois.enregistrer(self)

    def creer_tour(self):
        """
        Crée un nouveau tour dans un tournoi.
        """
        matchs = []
        joueurs = self.joueurs.copy()

        while len(joueurs) > 1:
            joueur1 = joueurs.pop(0)
            joueur2 = joueurs.pop(0)
            match = Match(self.num_tour_actuel * 100 + len(matchs) + 1, joueur1, joueur2)
            matchs.append(match)
        if joueurs:
            joueur_sans_paire = joueurs[0]
            for match in matchs:
                if match.joueur1.identifiant_national not in joueur_sans_paire.matchs and \
                   match.joueur2.identifiant_national not in joueur_sans_paire.matchs:
                    match_supplementaire = Match(
                        self.num_tour_actuel * 100 + len(matchs) + 1,
                        joueur_sans_paire,
                        match.joueur1
                    )
                    matchs.append(match_supplementaire)
                    break

        tour = Tour(self.num_tour_actuel, matchs, f"Tour {self.num_tour_actuel}")
        self.tours.append(tour)
        GestionnaireTournois.enregistrer(self)
        self.num_tour_actuel += 1
        num_tour = self.num_tour_actuel
        VuesTournoi.debut_tour(num_tour)

    def enregistrer_resultat(self, match_id, resultat):
        """
        Enregistre le résultat d'un match dans un tournoi.
        """
        for tour in self.tours:
            for match in tour.matchs:
                if match.id == match_id:
                    match.resultat = resultat

                    if resultat == 0:
                        match.joueur1.score += 1
                    elif resultat == 1:
                        match.joueur2.score += 1
                    elif resultat == 0.5:
                        match.joueur1.score += 0.5
                        match.joueur2.score += 0.5
                    break
        GestionnaireTournois.enregistrer(self)

    def lancer(self):
        """
        Lance ou continue un tournoi.
        """
        if self.num_tour_actuel >= self.nb_tours:
            VuesTournoi.max_tours()
            TournoiController.creer_classement(self)

        elif self.num_tour_actuel > 0:
            dernier_tour_termine = (
                all(match.resultat is not None for match in self.tours[self.num_tour_actuel - 1].matchs)
            )
            if not dernier_tour_termine:
                VuesTournoi.match_sans_resultat()
                TournoiController.saisir_resultat_tour(self)
            else:
                TournoiController.continuer_tournoi(self)
        elif self.num_tour_actuel == 0:
            TournoiController.commencer_tournoi(self)

    def creer_classement(self):
        self.joueurs.sort(key=lambda j: j.score, reverse=True)
        GestionnaireTournois.enregistrer(self)

    def saisir_resultat_tour(self):
        """
        Saisit le résultat d'un tour dans un tournoi.
        """
        tour_actuel = self.tours[self.num_tour_actuel - 1]
        for match in tour_actuel.matchs:
            VuesTournoi.info_match(match.id, match.joueur1.nom, match.joueur2.nom)
            while True:
                try:
                    resultat = float(input("""Entrez le résultat
                    (0 pour le joueur 1 gagnant, 1 pour le joueur 2 gagnant, 0.5 pour un match nul)
                    : """))
                    if resultat in [0, 0.5, 1]:
                        self.enregistrer_resultat(match.id, resultat)
                        break
                    else:
                        VuesTournoi.resultat_invalide()
                except ValueError:
                    VuesTournoi.entree_invalide()

    def verifier_nb_joueurs(self):
        """
        Verifie le nombre de joueurs d'un tournoi.
        """
        return len(self.joueurs)
