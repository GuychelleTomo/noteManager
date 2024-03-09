import pymysql

def Connection():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="noteManager")
        return conn
    except pymysql.DatabaseError as err:
        print("Erreur lors de la connexion à la base de données:", err)
        return None
    

#SELECT * FROM etudiant;
#SELECT nom_etudiant, prenom_etudiant FROM etudiant;
    



def recuperer_tous_les_etudiants():
    try:
        conn = Connection()
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

# Appel de la fonction pour récupérer tous les étudiants
# etudiants = recuperer_tous_les_etudiants()

# # Utilisation des données récupérées (par exemple, les afficher)
# if etudiants:
#     for etudiant in etudiants:
#         print(etudiant)
# else:
#     print("Aucun étudiant trouvé.")

# if __name__ == "__main__":
#     recuperer_tous_les_etudiants()