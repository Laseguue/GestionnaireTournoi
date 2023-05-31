# controleurs/round_control.py
class RoundController:
    def __init__(self, vue, modele):
        self.vue = vue
        self.modele = modele

    def add_round(self, tournament, round_name):
        round = self.modele(tournament, round_name)
        round.save()

    def show_rounds(self, tournament):
        rounds = self.modele.load_all(tournament)
        for round in rounds:
            self.vue.afficher_tour(round)
