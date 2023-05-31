# controleurs/tournament_control.py
class TournamentController:
    def __init__(self, vue, modele):
        self.vue = vue
        self.modele = modele

    def add_tournament(self, nom, lieu, date_debut, date_fin, nombre_tours, description):
        tournament = self.modele(nom, lieu, date_debut, date_fin, nombre_tours, description)
        tournament.save()

    def show_tournaments(self):
        tournaments = self.modele.load_all()
        for tournament in tournaments:
            self.vue.afficher_tournoi(tournament)
