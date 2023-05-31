class MainController:

    def __init__(self):
        self.player_controller = PlayerController(VueJoueurs(), PlayerModel())
        self.tournament_controller = TournamentController(VueTournois(), TournamentModel())
        self.round_controller = RoundController(VueTours(), RoundModel())
        self.match_controller = MatchController(VueMatchs(), MatchModel())

    def run(self):
        while True:
            MenuView.display_main_menu()
            choice = int(input("Choisissez une option: "))
            if choice == 1:
                self.player_controller.handle_players()
            elif choice == 2:
                self.tournament_controller.handle_tournaments()
            elif choice == 3:
                self.round_controller.handle_rounds()
            elif choice == 4:
                self.match_controller.handle_matches()
            elif choice == 5:
                break
            else:
                print("Choix non valide, veuillez essayer à nouveau.")