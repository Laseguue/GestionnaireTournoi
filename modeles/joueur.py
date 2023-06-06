from controleurs.joueur_control import PlayerController
from controleurs.gestionnaire_donne_joueur import GestionnaireJoueurs

class Joueur:
    def __init__(self, identifiant_national, nom, prenom, date_naissance, score=0, matchs=[]):
        self.identifiant_national = identifiant_national
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = score
        self.matchs = matchs 
    
    @staticmethod
    def generate_joueur(identifiant_national, nom, prenom, date_naissance):
        return Joueur(identifiant_national, nom, prenom, date_naissance)
    
    @classmethod
    def creer_joueur(cls, verifier_identifiant_national, verifier_date_naissance):
        print("Entrez les informations du joueur :")
        identifiant_national = verifier_identifiant_national()
        
        if GestionnaireJoueurs.joueur_existe(identifiant_national):
            print("Un joueur avec cet identifiant national existe déjà.")
            return None

        nom = input("Nom : ")
        prenom = input("Prénom : ")
        date_naissance = verifier_date_naissance()

        nouveau_joueur = cls.generate_joueur(identifiant_national, nom, prenom, date_naissance)
        
        GestionnaireJoueurs.enregistrer(nouveau_joueur)

        print(f"Joueur {nouveau_joueur.nom} enregistré avec succès.")

        return nouveau_joueur