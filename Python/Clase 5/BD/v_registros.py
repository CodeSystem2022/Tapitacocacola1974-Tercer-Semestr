import psycopg2

conexion = psycopg2.connect(
    user='postgres', password='matiitas', host='127.0.0.1', port='5432', database='test_bd',
)
try:
    with conexion:
        with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
                entrada= input('Digite los id_personas a buscar seperados por coma: ')
                llaves_primarias=(tuple(entrada.split(',')),)
                cursor.execute(sentencia,llaves_primarias)  # de esta manera ejecutamos la sentencia
                registros = cursor.fetchall()  # recuperamos todos los registros
                for registro in registros:
                   print(registros)

except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()
# https://www.psycopg.org/docs/usage.html
