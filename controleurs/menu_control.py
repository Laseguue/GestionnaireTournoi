from controleurs.rapport_control import RapportController
from controleurs.tournoi_control import TournoiController
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois
from controleurs.rapport_control import RapportController
from controleurs.joueur_control import PlayerController
from vues.menu_vues import MenuVues

class MenuController:
    @staticmethod
    def afficher_menu_principal():
        while True:
            choix = MenuVues.afficher_menu_principal()

            if choix == "1":
                MenuController.menu_tournoi()
            elif choix == "2":
                MenuController.menu_joueur()
            elif choix == "3":
                MenuController.choisir_option()
            elif choix == "4":
                print("Au revoir !")
                break
            else:
                print("Choix non valide, veuillez réessayer.")
    
    @staticmethod
    def choisir_option():
        while True:
            option = MenuVues.afficher_menu_rapport()
            if option == "1":
                RapportController.afficher_joueurs()
            elif option == "2":
                RapportController.afficher_tournois()
            elif option == "3":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                RapportController.afficher_nom_et_dates_tournoi(nom_tournoi) 
            elif option == "4":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                RapportController.afficher_joueurs_tournoi(nom_tournoi)
            elif option == "5":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                RapportController.afficher_tours_et_matchs(nom_tournoi)
            elif option == "6":
                nom_tournoi = input("Entrez le nom du tournoi pour lequel vous souhaitez créer un rapport: ")
                RapportController.rapport_de_tournoi(nom_tournoi)
            elif option == "7":
                break
            else:
                print("Option invalide.")
    
    @staticmethod
    def menu_joueur():
        while True:  
            choix = MenuVues.afficher_menu_joueur()
            if choix == "1":
                PlayerController.creer_joueur()
            elif choix == "2":
                PlayerController.supprimer_joueur()
            elif choix == "3":
                break  
            else:
                print("Option invalide. Veuillez choisir une option valide.")
    
    @staticmethod
    def menu_tournoi():
        while True:
            choix = MenuVues.afficher_menu_tournoi()

            if choix == "1":
                tournoi = TournoiController.creer_tournoi()
                GestionnaireTournois.enregistrer(tournoi)
                print(f"Le tournois {tournoi.nom} à étais créer avec succes.\n")
            elif choix == "2":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                tournoi = GestionnaireTournois.charger_tournoi_par_nom(nom_tournoi)
                TournoiController.ajouter_joueur_tournoi(tournoi)
            elif choix == "3":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                tournoi = GestionnaireTournois.charger_tournoi_par_nom(nom_tournoi)
                TournoiController.lancer_tournoi(tournoi)
                GestionnaireTournois.enregistrer(tournoi)
            elif choix == "4":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                tournoi = GestionnaireTournois.charger_tournoi_par_nom(nom_tournoi)
                TournoiController.supprimer_tournoi(tournoi)
            elif choix == "5":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")