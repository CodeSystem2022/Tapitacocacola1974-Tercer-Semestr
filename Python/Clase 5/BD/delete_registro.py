import psycopg2

conexion = psycopg2.connect(
        user='postgres', password='matiitas', host='127.0.0.1', port='5432', database='test_bd',
    )
try:
        with conexion:
            with conexion.cursor() as cursor:
                    sentencia='DELETE FROM persona WHERE id_persona=%s'
                    entrada=input('Digite el numero del registro a eliminar: ')
                    valores=(entrada,)#tupla de valores
                    cursor.execute(sentencia,valores)  # de esta manera ejecutamos la sentencia
                    registros_eliminados= cursor.rowcount
                    print(f'Los registros eliminados son: {registros_eliminados}')


except Exception as e:
        print(f'Ocurrio un error:{e}')
finally:
        conexion.close()
