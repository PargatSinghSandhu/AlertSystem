import os.path
import json
import csv
import mysql.connector
import connect

def fetch_data(config, start_ID, end_ID):
    connection = None
    db_config = config["database"]
    query = config["queries"]["fetch_movies"].format(start_ID=start_ID, end_ID=end_ID)

    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        with connection.cursor() as cursor:
            cursor.execute(query)
            movies = cursor.fetchall()

            attachment_path = config["email"]["attachment_path"]

            current_dir = os.path.dirname(__file__)
            attachment_path = os.path.join(current_dir, '..', attachment_path)
            attachment_path = os.path.abspath(attachment_path)

            with open(attachment_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([i[0] for i in cursor.description])
                csvwriter.writerows(movies)

    except mysql.connector.Error as e:
        log_file_path = config["logging"]["log_file_path"]
        current_dir = os.path.dirname(__file__)
        log_file_path = os.path.join(current_dir, '..', log_file_path)
        log_file_path = os.path.abspath(log_file_path)

        with open(log_file_path, "a") as f:
            f.write(f"An error occurred {e}")

    finally:
        if connection:
            connection.close()



