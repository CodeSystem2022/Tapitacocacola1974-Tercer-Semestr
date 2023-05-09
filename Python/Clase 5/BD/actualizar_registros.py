import psycopg2

conexion = psycopg2.connect(
        user='postgres', password='matiitas', host='127.0.0.1', port='5432', database='test_bd',
    )
try:
        with conexion:
            with conexion.cursor() as cursor:
                    sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
                    valores=('Juan Carlos','Roldan','rcarlos@mail.com',2)#tupla
                    cursor.execute(sentencia,valores)  # de esta manera ejecutamos la sentencia
                    registros_actualizados= cursor.rowcount
                    print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
        print(f'Ocurrio un error:{e}')
finally:
        conexion.close()
