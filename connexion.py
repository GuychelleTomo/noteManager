import pymysql

def Connection():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="noteManager")
        return conn
    except pymysql.DatabaseError as err:
        print("Erreur lors de la connexion à la base de données:", err)
        return None
