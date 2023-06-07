class VuesRapport:

    @staticmethod
    def afficher_joueur(joueur):
        """
        Affiche le nom d'un joueur.
        """
        print(f"{joueur.nom}")

    @staticmethod
    def afficher_tournoi(tournoi):
        """
        Affiche les informations d'un tournoi.
        """
        print(f"Id : {tournoi.id} \n{tournoi.nom}, du {tournoi.date_debut} au {tournoi.date_fin}")

    @staticmethod
    def afficher_tour_et_match(tour, i, match):
        """
        Affiche les informations d'un tour et d'un match.
        """
        print(f"Tour {i}:")
        if match.resultat == 0:
            gagnant = match.joueur1.nom
        elif match.resultat == 1:
            gagnant = match.joueur2.nom
        else:
            gagnant = 'égalité'
        print(f"Match {match.id} : {match.joueur1.nom} vs {match.joueur2.nom} : gagnant : {gagnant}")

    @staticmethod
    def afficher_nom_et_dates_tournoi(tournoi):
        """
        Affiche le nom et les dates d'un tournoi.
        """
        print(f"Nom du tournoi: {tournoi.nom}, du {tournoi.date_debut} au {tournoi.date_fin}")

    @staticmethod
    def aucun_tournoi_trouve():
        """
        Informe qu'aucun tournoi avec un certain nom n'a été trouvé.
        """
        print("Aucun tournoi trouvé avec ce nom.")
    
    @staticmethod
    def rapport_genere():
        """
        Informe que le rapport a été généré avec succès.
        """
        print("Rapport généré avec succès.")
    
    @staticmethod
    def afficher_tour(i):
        """
        Affiche le numéro d'un tour.
        """
        print(f"Tour {i}:")