from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",          # ganti jika user MySQL kamu berbeda
    password="pwbiasa",          # isi sesuai password MySQL kamu
    database="tugas_19_sintesa"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')     

    cursor = db.cursor()
    query = "SELECT * FROM login WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        return f"Login berhasil! Selamat datang, {username}."
    else:
        return "Login gagal! Username atau password salah."

if __name__ == '__main__':
    app.run(debug=True)
