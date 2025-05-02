from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route('/log-ip', methods=['POST'])
def log_ip():
    source_ip = request.remote_addr
    conn = None
    cursor = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS request_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ip_address VARCHAR(45),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("INSERT INTO request_log (ip_address) VALUES (%s)", (source_ip,))
        conn.commit()
        return {"status": "success", "ip_logged": source_ip}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

