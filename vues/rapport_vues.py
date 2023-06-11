class VuesRapport:

    @staticmethod
    def afficher_joueur(joueur):
        """
        Affiche le nom d'un joueur.
        """
        print(f"\n----- Joueur : {joueur.nom} -----\n")

    @staticmethod
    def afficher_tournoi(tournoi):
        """
        Affiche les informations d'un tournoi.
        """
        print("\n----- Tournoi : " + tournoi.nom + " -----\n"
              "Id : " + tournoi.id + "\n"
              "Dates: du " + tournoi.date_debut + " au " + tournoi.date_fin + "\n"
              "Description: " + tournoi.description + "\n"
              "Nombres de tours: " + str(tournoi.nb_tours) + "\n")

    @staticmethod
    def afficher_tour_et_match(tour, i, match, gagnant):
        """
        Affiche les informations d'un tour et d'un match.
        """
        if match.resultat == 0:
            gagnant = match.joueur1.nom
        elif match.resultat == 1:
            gagnant = match.joueur2.nom
        else:
            gagnant = 'égalité'
        print(f"\n----- Match {match.id} -----\n{match.joueur1.nom} vs {match.joueur2.nom}\nGagnant : {gagnant}\n")

    @staticmethod
    def afficher_nom_et_dates_tournoi(tournoi):
        """
        Affiche le nom et les dates d'un tournoi.
        """
        print(f"\n----- Tournoi : {tournoi.nom} -----\nDates: du {tournoi.date_debut} au {tournoi.date_fin}\n")

    @staticmethod
    def aucun_tournoi_trouve():
        """
        Informe qu'aucun tournoi avec un certain nom n'a été trouvé.
        """
        print("\n*** Aucun tournoi trouvé avec ce nom. ***\n")

    @staticmethod
    def rapport_genere():
        """
        Informe que le rapport a été généré avec succès.
        """
        print("\n*** Rapport généré avec succès. ***\n")

    @staticmethod
    def afficher_tour(i):
        """
        Affiche le numéro d'un tour.
        """
        print(f"\n----- Tour {i} : -----\n")
