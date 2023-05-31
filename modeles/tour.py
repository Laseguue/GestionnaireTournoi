from datetime import datetime

class Tour:
    def __init__(self, id, matchs=[], nom='', debut=None, fin=None):
        self.id = id
        self.nom = nom
        self.matchs = matchs
        self.debut = debut if debut else datetime.now()
        self.fin = fin

    def terminer(self):
        self.fin = datetime.now()
