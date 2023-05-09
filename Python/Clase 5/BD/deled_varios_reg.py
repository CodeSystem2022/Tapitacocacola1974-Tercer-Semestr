import psycopg2

conexion = psycopg2.connect(
        user='postgres', password='matiitas', host='127.0.0.1', port='5432', database='test_bd',
    )
try:
        with conexion:
            with conexion.cursor() as cursor:
                    sentencia='DELETE FROM persona WHERE id_persona in %s'
                    entrada=input('Digite los numeros de registros a eliminar separados por comas: ')
                    valores=(tuple(entrada.split(',')),)#tupla de valores de tuplas
                    cursor.execute(sentencia,valores)  # de esta manera ejecutamos la sentencia
                    registros_eliminados= cursor.rowcount
                    print(f'Los registros eliminados son: {registros_eliminados}')


except Exception as e:
        print(f'Ocurrio un error:{e}')
finally:
        conexion.close()
