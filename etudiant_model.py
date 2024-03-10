import connexion
import pymysql



class Etudiant:
    
    def __init__(self) -> None:
        pass


    def recuperer_tous_les_etudiants(self):
        try:
            conn = connexion.Connection()
            # Création d'un curseur pour exécuter des requêtes SQL
            curseur = conn.cursor()

            # Requête SQL pour récupérer tous les étudiants
            requete = "SELECT * FROM etudiant"

            # Exécution de la requête
            curseur.execute(requete)

            # Récupération de tous les résultats
            resultats = curseur.fetchall()

            # # Affichage des résultats (facultatif)
            # for resultat in resultats:
            #     print(resultat)

            # Fermeture du curseur et de la connexion
            curseur.close()
            conn.close()

            # Retourner les résultats
            return resultats

        except pymysql.Connection.Error as erreur:
            print("Erreur lors de la récupération des étudiants :", erreur)
            return None