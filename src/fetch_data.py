import os.path
import json
import csv
import mysql.connector
import mysql
from mysql.connector import connect

def fetch_data(config, start_ID, end_ID):
    '''

    :param config: A dictionary containing the configuration settings
    :param start_ID: The starting ID for the query.
    :param end_ID: The ending ID for the query.

    '''


    connection = None
    db_config = config["database"]
    query = config["queries"]["query"].format(start_ID=start_ID, end_ID=end_ID)

    try:
        connection = connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        with connection.cursor() as cursor:
            cursor.execute(query)
            movies = cursor.fetchall()

            csv_output_path = config["output"]['csv_output_path']
            current_dir = os.path.dirname(__file__)
            csv_output_path = os.path.join(current_dir, '..', csv_output_path)
            csv_output_path = os.path.abspath(csv_output_path)


            #ensuring the directory exists
            output_dir = os.path.dirname(csv_output_path)
            os.makedirs(output_dir, exist_ok = True)


            with open(csv_output_path, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([i[0] for i in cursor.description])
                csvwriter.writerows(movies)

            return csv_output_path #return the path of the generated CSV file

    except Error as e:
        log_file_path = config["logging"]["log_file_path"]
        current_dir = os.path.dirname(__file__)
        log_file_path = os.path.join(current_dir, '..', log_file_path)
        log_file_path = os.path.abspath(log_file_path)


        with open(log_file_path, "a") as f:
            f.write(f"An error occured: {e}\n")

    finally:
        if connection:
            connection.close()

