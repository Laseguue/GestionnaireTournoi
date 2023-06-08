from controleurs.rapport_control import RapportController
from controleurs.tournoi_control import TournoiController
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs
from controleurs.joueur_control import PlayerController
from vues.menu_vues import MenuVues
from modeles.tournoi import Tournoi
from modeles.joueur import Joueur
from vues.tournoi_vues import VuesTournoi

class MenuController:
    @staticmethod
    def afficher_menu_principal():
        """
        Affiche le menu principal et gère l'interaction utilisateur.
        """
        while True:
            choix = MenuVues.afficher_menu_principal()

            if choix == "1":
                MenuController.menu_tournoi()
            elif choix == "2":
                MenuController.menu_joueur()
            elif choix == "3":
                MenuController.choisir_option()
            elif choix == "4":
                MenuVues.quitter_programme()
                break
            else:
                MenuVues.choix_invalid()
    
    @staticmethod
    def choisir_option():
        """
        Affiche le menu des rapports et gère l'interaction utilisateur.
        """
        while True:
            option = MenuVues.afficher_menu_rapport()
            if option == "1":
                RapportController.afficher_joueurs()
            elif option == "2":
                RapportController.afficher_tournois()
            elif option == "3":
                nom_tournoi = MenuController.input_nom_tournoi()
                RapportController.afficher_nom_et_dates_tournoi(nom_tournoi) 
            elif option == "4":
                nom_tournoi = MenuController.input_nom_tournoi()
                RapportController.afficher_joueurs_tournoi(nom_tournoi)
            elif option == "5":
                nom_tournoi = MenuController.input_nom_tournoi()
                RapportController.afficher_tours_et_matchs(nom_tournoi)
            elif option == "6":
                nom_tournoi = MenuController.input_nom_tournoi()
                RapportController.rapport_de_tournoi(nom_tournoi)
            elif option == "7":
                break
            else:
                MenuVues.choix_invalid()
    
    @staticmethod
    def menu_joueur():
        """
        Affiche le menu des joueurs et gère l'interaction utilisateur.
        """
        while True:  
            choix = MenuVues.afficher_menu_joueur()
            if choix == "1":
                Joueur.creer_joueur(GestionnaireJoueurs.verifier_identifiant_national, GestionnaireJoueurs.verifier_date_naissance)
            elif choix == "2":
                PlayerController.supprimer_joueur()
            elif choix == "3":
                break  
            else:
                MenuVues.choix_invalid()
    
    @staticmethod
    def menu_tournoi():
        """
        Affiche le menu des tournois et gère l'interaction utilisateur.
        """
        while True:
            choix = MenuVues.afficher_menu_tournoi()

            if choix == "1":
                tournoi = Tournoi.creer_tournoi()
                GestionnaireTournois.enregistrer(tournoi)
                MenuVues.afficher_succes_creation_tournoi(tournoi.nom)
            elif choix == "2":
                tournoi = MenuController.entrer_tournoi_pour_charger()
                TournoiController.ajouter_joueur_tournoi(tournoi)
            elif choix == "3":
                tournoi = MenuController.entrer_tournoi_pour_charger()
                if TournoiController.verifier_nb_joueurs(tournoi) >= 2:
                    TournoiController.lancer_tournoi(tournoi)
                    GestionnaireTournois.enregistrer(tournoi)
                else:
                    MenuVues.nombre_tour_invalide()
            elif choix == "4":
                tournoi = MenuController.entrer_tournoi_pour_charger()
                TournoiController.supprimer_tournoi(tournoi)
            elif choix == "5":
                break
            else:
                MenuVues.choix_invalid()
                
    @staticmethod
    def entrer_tournoi_pour_charger():
        """
        Demande à l'utilisateur d'entrer le nom d'un tournoi pour le charger.
        """
        while True:
            nom_tournoi = MenuController.input_nom_tournoi()
            tournoi = GestionnaireTournois.charger_tournoi_par_nom(nom_tournoi)
            if tournoi is not None:
                return tournoi
            else:
                VuesTournoi.tournoi_introuvable()
    
    @staticmethod
    def input_nom_tournoi():
        """
        Demande à l'utilisateur d'entrer le nom d'un tournoi.
        """
        nom_tournoi = input("Entrez le nom du tournoi : ")
        return nom_tournoi