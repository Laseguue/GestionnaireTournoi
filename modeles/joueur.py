from controleurs.joueur_control import PlayerController
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs
from vues.joueur_vues import VuesJoueur


class Joueur:
    def __init__(self, identifiant_national, nom, prenom, date_naissance, score=0, matchs=[]):
        """
        Initialise un nouveau joueur.
        """
        self.identifiant_national = identifiant_national
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = score
        self.matchs = matchs

    @staticmethod
    def generate_joueur(identifiant_national, nom, prenom, date_naissance):
        """
        Génère un nouveau joueur.
        """
        return Joueur(identifiant_national, nom, prenom, date_naissance)

    @classmethod
    def creer_joueur(cls, verifier_identifiant_national, verifier_date_naissance):
        """
        Crée un nouveau joueur après avoir validé les informations d'entrée.
        """
        VuesJoueur.info_joueur()
        identifiant_national = verifier_identifiant_national()
        if GestionnaireJoueurs.joueur_existe(identifiant_national):
            VuesJoueur.joueur_exist_deja()
            return None
        nom = PlayerController.verifier_nom()
        prenom = PlayerController.verifier_prenom()
        date_naissance = verifier_date_naissance()
        nouveau_joueur = cls.generate_joueur(identifiant_national, nom, prenom, date_naissance)
        GestionnaireJoueurs.enregistrer(nouveau_joueur)
        VuesJoueur.joueur_enregistre_avec_succes(nom)
        return nouveau_joueur
