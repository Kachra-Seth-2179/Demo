from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': os.getenv('AZURE_MYSQL_HOST'),
    'user': os.getenv('AZURE_MYSQL_USER'),
    'password': os.getenv('AZURE_MYSQL_PASSWORD'),
    'database': os.getenv('AZURE_MYSQL_NAME')
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        return f"Connected to database: {db_name[0]}"
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
