
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
 #   print(archivo.read)
#no hace falta try o finally
#se ejecuta de manera automatica los metodos:--enter--, __exit__
from manejo_archivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivos:
    print(archivos.read())
