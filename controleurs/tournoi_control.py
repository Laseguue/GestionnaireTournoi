from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs
from vues.tournoi_vues import VuesTournoi
from controleurs.gestionnaire_donne_tournoi import GestionnaireTournois


class TournoiController:

    @staticmethod
    def ajouter_joueur_tournoi(tournoi):
        """
        Ajoute un joueur à un tournoi.
        """
        identifiant_national = input("Entrez l'identifiant national du joueur à ajouter: ")
        joueur = GestionnaireJoueurs.charger_joueur_par_identifiant_national(identifiant_national)
        if joueur:
            GestionnaireTournois.ajouter_joueur(tournoi, joueur)
            VuesTournoi.joueur_ajoute(joueur.nom, tournoi.nom)
        else:
            VuesTournoi.joueur_non_trouve(identifiant_national)

    @staticmethod
    def supprimer_tournoi(tournoi):
        """
        Supprime le tournoi
        """
        GestionnaireTournois.supprimer_tournoi(tournoi.nom)

    @staticmethod
    def lancer_tournoi(tournoi):
        """
        Supprime le tournoi
        """
        tournoi.lancer()

    @staticmethod
    def commencer_tournoi(tournoi):
        """
        Supprime le tournoi
        """
        tournoi.commencer()

    @staticmethod
    def continuer_tournoi(tournoi):
        """
        Supprime le tournoi
        """
        tournoi.continuer()

    @staticmethod
    def saisir_resultat_tour(tournoi):
        """
        Supprime le tournoi
        """
        tournoi.saisir_resultat_tour()

    @staticmethod
    def enregistrer_resultat(tournoi, match_id, resultat):
        """
        Supprime le tournoi
        """
        tournoi.enregistrer_resultat(match_id, resultat)

    @staticmethod
    def creer_classement(tournoi):
        """
        Supprime le tournoi
        """
        tournoi.creer_classement()

    @staticmethod
    def verifier_nb_joueurs(tournoi):
        """
        Supprime le tournoi
        """
        return tournoi.verifier_nb_joueurs()
