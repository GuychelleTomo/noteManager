
import connexion
import pymysql



class Classe:
    
    
    def __init__(self) -> None:
        pass
    
    def recuperer_toutes_les_classes(self):
        try:
            conn = connexion.Connection()
            # Création d'un curseur pour exécuter des requêtes SQL
            curseur = conn.cursor()

            # Requête SQL pour récupérer tous les étudiants
            requete = "SELECT * FROM classe"

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
            print("Erreur lors de la récupération des classes :", erreur)
            return None
    
    def ajouter_classe(self,*args):
        try:
            conn = connexion.Connection()
            # Création d'un curseur pour exécuter des requêtes SQL
            curseur = conn.cursor()

            # Requête SQL pour récupérer tous les étudiants
            requete = "INSERT INTO classe VALUES(NULL, %s)"

            # Exécution de la requête
            resultat = curseur.execute(requete,args)
            conn.commit()
            # Fermeture du curseur et de la connexion
            curseur.close()
            conn.close()

            # Retourner les résultats
            return resultat

        except pymysql.Connection.Error as erreur:
            print("Erreur lors de la récupération des classes :", erreur)
            return None
        
        
    def supprimer_classe(self,id):
        try:
            conn = connexion.Connection()
            # Création d'un curseur pour exécuter des requêtes SQL
            curseur = conn.cursor()

            # Requête SQL pour récupérer tous les étudiants
            requete = "DELETE FROM classe WHERE id_classe = %s"

            # Exécution de la requête
            resultat = curseur.execute(requete,id)
            conn.commit()
            # Fermeture du curseur et de la connexion
            curseur.close()
            conn.close()

            # Retourner les résultats
            return resultat

        except pymysql.Connection.Error as erreur:
            print("Erreur lors de la récupération des classes :", erreur)
            return None
        
        
    def modifier_classe(self,*args):
        try:
            conn = connexion.Connection()
            # Création d'un curseur pour exécuter des requêtes SQL
            curseur = conn.cursor()

            # Requête SQL pour récupérer tous les étudiants
            requete = "UPDATE classe  SET nom_classe = %s WHERE id_classe = %s"

            # Exécution de la requête
            resultat = curseur.execute(requete,args)
            conn.commit()
            # Fermeture du curseur et de la connexion
            curseur.close()
            conn.close()

            # Retourner les résultats
            return resultat

        except pymysql.Connection.Error as erreur:
            print("Erreur lors de la récupération des classes :", erreur)
            return None
    

    
if __name__ == "__main__":
    
    test = Classe()
    print(test.recuperer_toutes_les_classes())
    print(test.ajouter_classe("LPSIR"))
        