from controleurs.joueur_control import PlayerController

class VuesJoueur:
    @staticmethod
    def menu_joueur():
        print("1. Créer un nouveau joueur")
        print("2. Supprimer un joueur existant")
        print("3. Afficher tous les joueurs")
        print("4. Retourner au menu principal")

        choix = input("Choisissez une option : ")

        if choix == "1":
            PlayerController.creer_joueur()
        elif choix == "2":
            PlayerController.supprimer_joueur()
        elif choix == "3":
            PlayerController.afficher_joueurs()
        elif choix == "4":
            # retourner au menu principal
            pass
        else:
            print("Option invalide. Veuillez choisir une option valide.")
            VuesJoueur.menu_joueur()
