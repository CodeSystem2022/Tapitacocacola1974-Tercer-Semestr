from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
# comenzamos importando clases que utilizaremos en nuestro proyecto
load_dotenv()
# iniciamos proyecto
app = Flask(__name__)
key = Fernet.generate_key()
#definimos las variables de conexion
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')
dbname = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
# creamos la funcion get_conection que nos servira para nuestra conexion a la base de datos
def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn
#creamos el primer end point donde tendremos la funcion get users
@app.get('/api/users')
def get_users():
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute('SELECT * FROM users') #en esta funcion utilizamos dicho query 
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({'message': 'An error occurred while retrieving users: ' + str(e)}), 500

@app.post('/api/users')
def create_user(): #se crea la funcion create_user
    try:
        new_user = request.get_json()
        username = new_user['username']
        email = new_user['email']
        direccion = new_user['direccion']
        print(username, email, direccion)

        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute('INSERT INTO users (username, email, direccion) VALUES (%s, %s, %s) RETURNING *',
                    (username, email, direccion)) #en esta funcion utilizamos dicho query
        new_created_user = cur.fetchone()
        print(new_created_user)
        conn.commit()

        cur.close()
        conn.close()
        return jsonify(new_created_user)
    except Exception as e:
        return jsonify({'message': 'An error occurred while creating the user: ' + str(e)}), 500



@app.delete('/api/users/<id>')
def delete_users(id): #creamos la funcion delete users
    try:

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
    except Exception as e:
        return jsonify({'message': 'An error occurred while deleting the user: ' + str(e)}), 500


@app.put('/api/users/<id>')
def update_users(id): #funcion update users
    try:

        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        new_user = request.get_json()
        username = new_user['username']
        email = new_user['email']
        direccion = new_user['direccion']
        print(username, email, direccion)

        cur.execute(
            'UPDATE users SET username=%s, email=%s, direccion=%s WHERE id=%s RETURNING *',
            (username, email, direccion, id))
        updated_user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if updated_user is None:
            return jsonify({'message': 'User not found'}), 404

        return jsonify(updated_user)
    
    except Exception as e:
        return jsonify({'message': 'An error occurred while updating the user: ' + str(e)}), 500



@app.get('/api/users/<id>')
def get_user(id):
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute('SELECT * FROM users WHERE id = %s', (id,))
        user = cur.fetchone()

        if user is None:
            return jsonify({'message': 'User not found'}), 404

        return jsonify(user)
    except Exception as e:
        return jsonify({'message': 'An error occurred while retrieving the user: ' + str(e)}), 500

@app.route('/')
def home():
    return send_file('static/index.html')

if __name__ == '__main__':
    app.run(debug=True)
