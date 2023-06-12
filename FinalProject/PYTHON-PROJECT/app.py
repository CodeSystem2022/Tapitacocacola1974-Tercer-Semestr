from flask import Flask, request, jsonify,send_file,json
from psycopg2 import connect, extras
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from os import environ

load_dotenv

app = Flask(__name__)
key = Fernet.generate_key()

host =environ.get('DB_HOST')
port = environ.get('DB_PORT')
dbname =environ.get('DB_NAME')
user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')
#host='localhost'
#port=5432
#dbname='usersdb'
#user='postgres'
#password="matiitas"
#host='containers-us-west-209.railway.app'
#port=7220
#dbname='usersdb'
#user='postgres'
#password="rZ1erL8rIiv8juGGtRFU"


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,
                   user=user, password=password)
    return conn


@app.get('/api/users')
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)


@app.post('/api/users')
def create_user():

    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
    print(username, email, password)

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO users (username,email,password)VALUES(%s,%s,%s)RETURNING *',
                (username, email, password))
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()

    cur.close()
    conn.close()
    return jsonify(new_created_user)


@app.delete('/api/users/<id>')
def delete_users(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('DELETE FROM users WHERE id = %s RETURNING *', (id, ))
    user = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    if user is None:
        return jsonify({'message': 'User not delete'}), 404

    return jsonify(user)


@app.put('/api/users/<id>')
def update_users(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
    print(username, email, password)

    cur.execute(
        'UPDATE users SET username=%s,email=%s,password=%s WHERE id=%s  RETURNING *', (username, email, password, id))
    updated_user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if updated_user is None:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(updated_user)


@app.get('/api/users/<id>')
def get_user(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cur.fetchone()

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(user)

@app.route('/')
def home():
    return send_file('static/index.html')

if __name__ == '__main__':
    app.run(debug=True)