from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    try:
        # Všimněte si: host="db" odkazuje na název služby v docker-compose.yml
        conn = psycopg2.connect(
            host="db",
            database="dev_db",
            user="dev_user",
            password="dev_password"
        )
        return "Connected to DB successfully!"
    except Exception as e:
        return f"DB Connection Failed: {str(e)}"

@app.route('/')
def home():
    db_status = get_db_connection()
    return jsonify({
        "service": "Backend API",
        "status": "Running in Docker Compose",
        "db_check": db_status
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)