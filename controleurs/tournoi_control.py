import random
from modeles.tour import Tour
from modeles.match import Match
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs
from vues.tournoi_vues import VuesTournoi


class TournoiController:
    @staticmethod
    def supprimer_tournoi(tournoi):
        """
        Supprime un tournoi.
        """
        GestionnaireTournois.supprimer_tournoi(tournoi.nom)

    @staticmethod
    def ajouter_joueur_tournoi(tournoi):
        """
        Ajoute un joueur à un tournoi.
        """
        identifiant_national = input("Entrez l'identifiant national du joueur à ajouter: ")
        joueur = GestionnaireJoueurs.charger_joueur_par_identifiant_national(identifiant_national)
        if joueur:
            tournoi.joueurs.append(joueur)
            GestionnaireTournois.enregistrer(tournoi)
            VuesTournoi.joueur_ajoute(joueur.nom, tournoi.nom)
        else:
            VuesTournoi.joueur_non_trouve(identifiant_national)

    @staticmethod
    def commencer_tournoi(tournoi):
        """
        Commence un tournoi.
        """
        random.shuffle(tournoi.joueurs)
        TournoiController.creer_tour(tournoi)
        TournoiController.saisir_resultat_tour(tournoi)
        GestionnaireTournois.enregistrer(tournoi)

    @staticmethod
    def continuer_tournoi(tournoi):
        """
        Continue un tournoi existant.
        """
        tournoi.joueurs.sort(key=lambda j: j.score, reverse=True)
        TournoiController.creer_tour(tournoi)
        TournoiController.saisir_resultat_tour(tournoi)
        GestionnaireTournois.enregistrer(tournoi)

    @staticmethod
    def creer_tour(tournoi):
        """
        Crée un nouveau tour dans un tournoi.
        """
        matchs = []
        joueurs = tournoi.joueurs.copy()

        while len(joueurs) > 1:
            joueur1 = joueurs.pop(0)
            joueur2 = joueurs.pop(0)
            match = Match(tournoi.num_tour_actuel * 100 + len(matchs) + 1, joueur1, joueur2)
            matchs.append(match)
        if joueurs:
            joueur_sans_paire = joueurs[0]
            for match in matchs:
                if match.joueur1.identifiant_national not in joueur_sans_paire.matchs and \
                   match.joueur2.identifiant_national not in joueur_sans_paire.matchs:
                    match_supplementaire = Match(
                        tournoi.num_tour_actuel * 100 + len(matchs) + 1,
                        joueur_sans_paire,
                        match.joueur1
                    )
                    matchs.append(match_supplementaire)
                    break

        tour = Tour(tournoi.num_tour_actuel, matchs, f"Tour {tournoi.num_tour_actuel}")
        tournoi.tours.append(tour)

        GestionnaireTournois.enregistrer(tournoi)
        tournoi.num_tour_actuel += 1
        num_tour = tournoi.num_tour_actuel
        VuesTournoi.debut_tour(num_tour)

    @staticmethod
    def enregistrer_resultat(tournoi, match_id, resultat):
        """
        Enregistre le résultat d'un match dans un tournoi.
        """
        for tour in tournoi.tours:
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
        GestionnaireTournois.enregistrer(tournoi)

    @staticmethod
    def lancer_tournoi(tournoi):
        """
        Lance ou continue un tournoi.
        """
        if tournoi.num_tour_actuel >= tournoi.nb_tours:
            VuesTournoi.max_tours()
            TournoiController.creer_classement(tournoi)

        elif tournoi.num_tour_actuel > 0:
            dernier_tour_termine = (
                all(match.resultat is not None for match in tournoi.tours[tournoi.num_tour_actuel - 1].matchs)
            )
            if not dernier_tour_termine:
                VuesTournoi.match_sans_resultat()
                TournoiController.saisir_resultat_tour(tournoi)
            else:
                TournoiController.continuer_tournoi(tournoi)
        elif tournoi.num_tour_actuel == 0:
            TournoiController.commencer_tournoi(tournoi)

    @staticmethod
    def creer_classement(tournoi):
        """
        Crée un classement pour un tournoi.
        """
        tournoi.joueurs.sort(key=lambda j: j.score, reverse=True)
        GestionnaireTournois.enregistrer(tournoi)

    @staticmethod
    def saisir_resultat_tour(tournoi):
        """
        Saisit le résultat d'un tour dans un tournoi.
        """
        tour_actuel = tournoi.tours[tournoi.num_tour_actuel - 1]
        for match in tour_actuel.matchs:
            VuesTournoi.info_match(match.id, match.joueur1.nom, match.joueur2.nom)
            while True:
                try:
                    resultat = float(input("""Entrez le résultat
                    (0 pour le joueur 1 gagnant, 1 pour le joueur 2 gagnant, 0.5 pour un match nul)
                    : """))
                    if resultat in [0, 0.5, 1]:
                        TournoiController.enregistrer_resultat(tournoi, match.id, resultat)
                        break
                    else:
                        VuesTournoi.resultat_invalide()
                except ValueError:
                    VuesTournoi.entree_invalide()

    @staticmethod
    def verifier_nb_joueurs(tournoi):
        """
        Vérifie le nombre de joueurs dans un tournoi.
        """
        return len(tournoi.joueurs)
