from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs
from vues.rapport_vues import VuesRapport


class RapportController:
    @staticmethod
    def afficher_joueurs():
        """
        Affiche les informations sur tous les joueurs.
        """
        joueurs = GestionnaireJoueurs.charger()
        joueurs.sort(key=lambda j: j.nom)
        for joueur in joueurs:
            VuesRapport.afficher_joueur(joueur)

    @staticmethod
    def afficher_tournois():
        """
        Affiche les informations sur tous les tournois.
        """
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            VuesRapport.afficher_tournoi(tournoi)

    @staticmethod
    def afficher_joueurs_tournoi(nom_tournoi):
        """
        Affiche les joueurs participant à un tournoi spécifié.
        """
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                joueurs = tournoi.joueurs
                joueurs.sort(key=lambda j: j.nom)
                for joueur in joueurs:
                    VuesRapport.afficher_joueur(joueur)
                break

    @staticmethod
    def afficher_tours_et_matchs(nom_tournoi):
        """
        Affiche les tours et les matchs d'un tournoi spécifié.
        """
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                for i, tour in enumerate(tournoi.tours, 1):
                    VuesRapport.afficher_tour(i)
                    for match in tour.matchs:
                        if match.resultat == 0:
                            gagnant = match.joueur1.nom
                        elif match.resultat == 1:
                            gagnant = match.joueur2.nom
                        else:
                            gagnant = 'égalité'
                        VuesRapport.afficher_tour_et_match(tour, i, match, gagnant)
                break

    @staticmethod
    def afficher_nom_et_dates_tournoi(nom_tournoi):
        """
        Affiche le nom et les dates d'un tournoi spécifié.
        """
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                VuesRapport.afficher_nom_et_dates_tournoi(tournoi)
                break

    @staticmethod
    def rapport_de_tournoi(nom_tournoi):
        """
        Génère un rapport détaillé pour un tournoi spécifié.
        """
        nom = nom_tournoi
        tournoi = GestionnaireTournois.charger_tournoi_par_nom(nom)
        if tournoi is None:
            VuesRapport.aucun_tournoi_trouve()
            return
        with open(f"{nom}_rapport.txt", "w") as f:
            f.write(f"Tournoi: {tournoi.nom}\n")
            f.write(f"Lieu: {tournoi.lieu}\n")
            f.write(f"Date début: {tournoi.date_debut}\n")
            f.write(f"Date fin: {tournoi.date_fin}\n")
            f.write(f"Nombres de tours: {tournoi.nb_tours}\n")
            f.write(f"Description: {tournoi.description}\n\n")
            f.write("Joueurs:\n")
            for joueur in tournoi.joueurs:
                f.write(f"{joueur.identifiant_national} {joueur.prenom} {joueur.nom} {joueur.date_naissance}\n")
            f.write("\n")
            f.write("Tours:\n")
            for i, tour in enumerate(tournoi.tours, 1):
                f.write(f"Tour {i}:\n")
                for j, match in enumerate(tour.matchs, 1):
                    if match.resultat == 0:
                        gagnant = match.joueur1.prenom
                    elif match.resultat == 1:
                        gagnant = match.joueur2.prenom
                    else:
                        gagnant = 'égalité'
                    f.write(f"\tMatch {j}: {match.joueur1.prenom} vs {match.joueur2.prenom} : gagnant : {gagnant}\n")
            f.write("\n")
            f.write("Classement:\n")
            sorted_joueurs = sorted(tournoi.joueurs, key=lambda joueur: joueur.score, reverse=True)
            for i, joueur in enumerate(sorted_joueurs, 1):
                f.write(f"{i}. {joueur.nom} {joueur.score} \n")
        VuesRapport.rapport_genere()
