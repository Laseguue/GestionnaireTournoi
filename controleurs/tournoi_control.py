from modeles.joueur import Joueur
from modeles.tournoi import Tournoi
from modeles.tour import Tour
from modeles.match import Match
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs


class TournoiController:
    @staticmethod
    def creer_tournoi():
        print("Entrez les informations du tournoi :")

        id = GestionnaireTournois.generer_id_unique() 
        nom = input("Nom : ")
        lieu = input("Lieu : ")
        date_debut = input("Date de début (JJ/MM/AAAA) : ")
        date_fin = input("Date de fin (JJ/MM/AAAA) : ")
        nb_tours = int(input("Nombre de tours : "))
        description = input("Description : ")

        tournoi = Tournoi(id, nom, lieu, date_debut, date_fin, nb_tours=4, description=description)

        return tournoi
    
    @staticmethod
    def supprimer_tournoi(tournoi):
        GestionnaireTournois.supprimer_tournoi(id)
        print("Le tournoi a été supprimé avec succès.")

    @staticmethod
    def ajouter_joueur_tournoi(tournoi):
        identifiant_national = input("Entrez l'identifiant national du joueur à ajouter: ")
        joueur = GestionnaireJoueurs.charger_joueur_par_identifiant_national(identifiant_national)
        if joueur:
            tournoi.joueurs.append(joueur)
            GestionnaireTournois.enregistrer(tournoi)
        else:
            print(f"Aucun joueur trouvé avec l'identifiant national {identifiant_national}")

    @staticmethod
    def commencer_tournoi(tournoi):
        random.shuffle(tournoi.joueurs)
        TournoiController.creer_tour(tournoi)
        tournoi.num_tour_actuel += 1

    @staticmethod
    def continuer_tournoi(tournoi):
        tournoi.joueurs.sort(key=lambda j: j.score, reverse=True)
        TournoiController.creer_tour(tournoi)
        tournoi.num_tour_actuel += 1

    @staticmethod
    def creer_tour(tournoi):
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
                    match_supplementaire = Match(tournoi.num_tour_actuel * 100 + len(matchs) + 1, joueur_sans_paire, match.joueur1)
                    matchs.append(match_supplementaire)
                    break
        
        tour = Tour(tournoi.num_tour_actuel, matchs, f"Tour {tournoi.num_tour_actuel}")
        tournoi.tours.append(tour)

        GestionnaireTournois.enregistrer(tournoi)

        print(f"Le tour {tournoi.num_tour_actuel} a commencé.")

    @staticmethod
    def enregistrer_resultat(tournoi, match_id, resultat):
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
        if tournoi.num_tour_actuel >= tournoi.nb_tours:
            print("Le tournoi a atteint le nombre maximum de tours ou est terminé.")
            TournoiController.creer_classement(tournoi)

        elif tournoi.num_tour_actuel > 0:
            for match in tournoi.tours[tournoi.num_tour_actuel - 1].matchs:
                if match.resultat is None:
                    print("Il y a encore des matchs sans résultats dans le tour actuel. Veuillez entrer tous les résultats avant de commencer un nouveau tour.")
                    TournoiController.saisir_resultat_tour(tournoi)
        elif tournoi.num_tour_actuel == 0:
            TournoiController.commencer_tournoi(tournoi)
    
    @staticmethod
    def creer_classement(tournoi):
        tournoi.joueurs.sort(key=lambda j: j.score, reverse=True)
        GestionnaireTournois.enregistrer(tournoi)
    
    @staticmethod
    def saisir_resultat_tour(tournoi):
        tour_actuel = tournoi.tours[tournoi.num_tour_actuel - 1]
        for match in tour_actuel.matchs:
            print(f"Match {match.id} : {match.joueur1.nom} vs {match.joueur2.nom}")
            while True:
                try:
                    resultat = float(input("Entrez le résultat (0 pour le joueur 1 gagnant, 1 pour le joueur 2 gagnant, 0.5 pour un match nul) : "))
                    if resultat in [0, 0.5, 1]:
                        TournoiController.enregistrer_resultat(tournoi, match.id, resultat)
                        break
                    else:
                        print("Résultat invalide. Veuillez entrer un nombre valide (0, 0.5, 1).")
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre valide.")