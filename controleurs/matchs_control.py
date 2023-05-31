# controleurs/match_control.py
class MatchController:
    def __init__(self, vue, modele):
        self.vue = vue
        self.modele = modele

    def add_match(self, round, player1, player2):
        match = self.modele(round, player1, player2)
        match.save()

    def show_matches(self, round):
        matches = self.modele.load_all(round)
        for match in matches:
            self.vue.afficher_match(match)
