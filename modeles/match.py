class Match:
    def __init__(self, id, joueur1, joueur2, resultat=None):
        """
        Initialise un nouveau match.
        """
        self.id = id
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat
