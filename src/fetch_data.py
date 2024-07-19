import mysql.connector

def fetch_data():
    connect_db = mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password= "admin",
        database = "online_movie_rating"
    )
    cursor = connect_db.cursor()

    cursor.execute("SHOW DATABASES")

    for x in cursor:
        print(x)