import jsonpickle
import uuid
import hashlib

class GestionnaireTournois:
    FILE_PATH = 'Liste_de_tournois.json'

    @staticmethod
    def enregistrer(tournoi):
        tournois = GestionnaireTournois.charger()
        tournoi_index = next((index for (index, t) in enumerate(tournois) if t.id == tournoi.id), None)

        if tournoi_index is not None:
            tournois[tournoi_index] = tournoi
        else:
            tournois.append(tournoi)

        with open(GestionnaireTournois.FILE_PATH, 'w') as file:
            file.write(jsonpickle.encode(tournois))

    @staticmethod
    def charger():
        try:
            with open(GestionnaireTournois.FILE_PATH, 'r') as file:
                return jsonpickle.decode(file.read())
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def charger_tournoi_par_id(id):
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.id == id:
                return tournoi
        return None
        
    @staticmethod
    def supprimer_tournoi(id):
        tournois = GestionnaireTournois.charger()
        tournoi_trouve = False

        for tournoi in tournois:
            if tournoi.id == id:
                tournois.remove(tournoi)
                tournoi_trouve = True
                break

        if tournoi_trouve:
            with open('Liste_de_tournois.json', 'w') as file:
                file.write(jsonpickle.encode(tournois))
            print("Tournoi supprimé avec succès.")
        else:
            print("Le tournoi n'a pas été trouvé.")

    @staticmethod
    def charger_tournoi_par_nom(nom):
        tournois = GestionnaireTournois.charger()
        for tournoi in tournois:
            if tournoi.nom == nom:
                return tournoi
        return None
    
    def generer_id_unique():
        data = 'votre_data_unique'.encode('utf-8')
        hashed = hashlib.sha256(data).hexdigest()
        return hashed[:8]