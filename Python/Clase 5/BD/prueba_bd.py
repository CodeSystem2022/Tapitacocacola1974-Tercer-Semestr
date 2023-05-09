import psycopg2

conexion = psycopg2.connect(
    user='postgres', password='matiitas', host='127.0.0.1', port='5432', database='test_bd',
)
try:
    with conexion:
        with conexion.cursor() as cursor:
              # sentencia = 'SELECT id_persona,nombre FROM persona'
                sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
                id_persona=input('Digite un numero: ')
                cursor.execute(sentencia,(id_persona,))  # de esta manera ejecutamos la sentencia
                registros = cursor.fetchone()  # recuperamos todos los registros
                print(registros)
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()
# https://www.psycopg.org/docs/usage.html



