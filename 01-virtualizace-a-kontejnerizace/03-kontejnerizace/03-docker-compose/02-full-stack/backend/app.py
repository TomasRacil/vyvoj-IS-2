from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
import time

app = Flask(__name__)
# CORS povolí Frontendu (běžícímu na portu 3000) ptát se Backendu (na portu 5000)
CORS(app)

# Konfigurace DB z proměnných prostředí (z docker-compose.yml)
DB_HOST = "db" # Název služby v docker-compose
DB_NAME = os.getenv("POSTGRES_DB", "app_db")
DB_USER = os.getenv("POSTGRES_USER", "app_user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "app_password")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

def init_db():
    """Pokusí se připojit k DB a vytvořit tabulku. Pokud DB ještě neběží, zkusí to znovu."""
    retries = 5
    while retries > 0:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            # Přidali jsme sloupec 'done' pro stav úkolu
            cur.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id SERIAL PRIMARY KEY,
                    task VARCHAR(200) NOT NULL,
                    done BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("--- Databáze inicializována ---")
            return
        except psycopg2.OperationalError:
            print("--- Databáze není připravena, čekám... ---")
            time.sleep(2)
            retries -= 1

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Vrátí seznam všech úkolů."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, task, done FROM todos ORDER BY id DESC;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        todos = [{"id": row[0], "task": row[1], "done": row[2]} for row in rows]
        return jsonify(todos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/todos', methods=['POST'])
def add_todo():
    """Přidá nový úkol."""
    data = request.json
    task = data.get('task')
    if not task:
        return jsonify({"error": "Task is required"}), 400
        
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO todos (task) VALUES (%s) RETURNING id;", (task,))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": new_id, "task": task, "done": False, "status": "created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Smaže úkol podle ID."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM todos WHERE id = %s;", (todo_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "deleted", "id": todo_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Přepne stav hotovo (done)."""
    data = request.json
    done = data.get('done')
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE todos SET done = %s WHERE id = %s;", (done, todo_id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "updated", "id": todo_id, "done": done}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)