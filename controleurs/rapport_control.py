from modeles.joueur import Joueur
from modeles.tournoi import Tournoi
from modeles.tour import Tour
from modeles.match import Match
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs

class RapportController:
    @staticmethod
    def afficher_joueurs():
        joueurs = GestionnaireJoueurs.charger()
        joueurs.sort(key=lambda j: j.nom)
        for joueur in joueurs:
            print(f"{joueur.nom}")

    @staticmethod
    def afficher_tournois():
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            print(f"Id : {tournoi.id} \n{tournoi.nom}, du {tournoi.date_debut} au {tournoi.date_fin}")

    @staticmethod
    def afficher_joueurs_tournoi(nom_tournoi):
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                joueurs = tournoi.joueurs
                joueurs.sort(key=lambda j: j.nom) 
                for joueur in joueurs:
                    print(f"{joueur.nom}")
                break

    @staticmethod
    def afficher_tours_et_matchs(nom_tournoi):
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                for tour in tournoi.tours:
                    print(f"Tour {tour.id}:")
                    for match in tour.matchs:
                        print(f"Match {match.id} : {match.joueur1.nom} vs {match.joueur2.nom} : {match.joueur1.nom} {match.joueur1.score} points, {match.joueur2.nom} {match.joueur2.score} points")
                break
    
    @staticmethod
    def afficher_nom_et_dates_tournoi(nom_tournoi):
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom_tournoi:
                print(f"Nom du tournoi: {tournoi.nom}, du {tournoi.date_debut} au {tournoi.date_fin}")

                break
    @staticmethod
    def rapport_de_tournoi(nom_tournoi):
        nom = nom_tournoi
        tournoi = GestionnaireTournois.charger_tournoi_par_nom(nom)
        if tournoi is None:
            print("Aucun tournoi trouvé avec ce nom.")
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
                    f.write(f"\tMatch {j}: {match.joueur1.prenom} vs {match.joueur2.prenom} : {match.joueur1.prenom} {match.joueur1.score} points {match.joueur2.prenom} {match.joueur2.score} points\n")
            f.write("\n")
            f.write("Classement:\n")
            sorted_joueurs = sorted(tournoi.joueurs, key=lambda joueur: joueur.score, reverse=True)
            for i, joueur in enumerate(sorted_joueurs, 1):
                f.write(f"{i}. {joueur.nom} {joueur.score} \n")
        print("Rapport généré avec succès.")