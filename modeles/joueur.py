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