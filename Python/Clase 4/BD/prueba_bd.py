import psycopg2

conexion = psycopg2.connect(
    user= 'postgres',
    password='matiitas',
    host='127.0.0.1',
    port='5432',
    database='test_bd',
)

cursor= conexion.cursor()
sentencia='SELECT * FROM persona'
cursor.execute(sentencia)#de esta manera ejecutamos la sentencia
registros= cursor.fetchall()#recuperamos todos los registros
print(registros)

cursor.close()
conexion.close()