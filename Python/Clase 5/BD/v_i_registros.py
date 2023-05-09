import psycopg2

conexion = psycopg2.connect(
        user='postgres', password='matiitas', host='127.0.0.1', port='5432', database='test_bd',
    )
try:
        with conexion:
            with conexion.cursor() as cursor:
                    sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
                    valores=(
                        ('Carlos','Lara','Clara@mail.com'),
                        ('Marcos','Canto','mcanto@mail.com'),
                        ('Marcelo','Cuenca','cuencaM@mail.com')
                    )#tupla de tuplas
                    cursor.executemany(sentencia,valores)  # de esta manera ejecutamos la sentencia
                    #conexion.commit() guarda los cambios en la base de datos pero el with lo hace
                    registros_insertados = cursor.rowcount
                    print(f'Los registros insertados son: {registros_insertados}')


except Exception as e:
        print(f'Ocurrio un error:{e}')
finally:
        conexion.close()
