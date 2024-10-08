from flask import Flask, request, jsonify
from functools import wraps
import json
import os
import csv
from mysql.connector import connect, Error

app = Flask(__name__)

current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, 'config.json')
with open(config_path, 'r') as f:
    config= json.load(f)

def require_auth(f): #a decorater function that wraps other function to enforce authentication
    @wraps(f)
    def decorated_functions(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == config['auth']['username'] and auth.password == config['auth']['password']):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_functions

@app.route('/revoke_access', methods=['POST'])
@require_auth

def revoke_access():
    data= request.json

    return jsonify({"message": "User access revoked"})

@app.route('/generate_report', methods=['POST'])
@require_auth
def generate_report():
    data = request.json

    start_id = config["queries"]["start_ID"]
    end_id = config["queries"]["end_ID"]


    db_config = config["database"]

    query = config["queries"]["Query"].format(start_ID= start_id, end_ID=end_id)

    try:
        connection = connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        with connection.cursor() as cursor:
            cursor.execute(query)
            movies = cursor.fetchall()


            attachment_path = os.path.join(current_dir, config["email"]["attachment_path"])


            with open(attachment_path, 'w', newline='') as csvfile:
                csvwriter=csv.writer(csvfile)
                csvwriter.writerow([i[0] for i in cursor.description])
                csvwriter.writerows(movies)

    except Error as e:
        log_file_path = os.path.join(current_dir, config["logging"]["logging_file_path"])
        with open(log_file_path, "a") as f:
            f.write(f"An error occurred: {e}\n")
        return jsonify({"message": "an error occurred", "error": str(e)}). status_code

    finally:
        if connection:
            connection.close()

    return jsonify({"message": "report Generated successfully", "path": attachment_path})

if __name__=='__main__':
    app.run(debug=True)






