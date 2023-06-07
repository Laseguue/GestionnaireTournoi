from datetime import datetime

class Tour:
    def __init__(self, id, matchs=[], nom='', debut=None, fin=None):
        """
        Initialise un nouveau tour.
        """
        self.id = id
        self.nom = nom
        self.matchs = matchs
        self.debut = debut if debut else datetime.now()
        self.fin = fin

    def terminer(self):
        """
        Termine le tour actuel en marquant l'heure de fin.
        """
        self.fin = datetime.now()