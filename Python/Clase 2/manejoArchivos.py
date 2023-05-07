#declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('programamos con diferentes tipos de archivos,ahora en txt.\n')
    archivo.write('la palabra acción lleva acento.\n')
    archivo.write('las letras son r read,w write,a append,x exception\n')
    archivo.write('saludos a todos los alumnos de la tecnicatura')
except Exception as e:
    print(f'{e}')
finally:#siempre se ejecuta
    archivo.close()
