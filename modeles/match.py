class Match:
    def __init__(self, id, joueur1, joueur2, resultat=None):
        self.id = id
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat  # 0 pour joueur1 gagne, 1 pour joueur2 gagne, 0.5 pour match nul.
