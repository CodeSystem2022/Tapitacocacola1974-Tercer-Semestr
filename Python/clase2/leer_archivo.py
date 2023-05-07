archivo = open('prueba.txt', 'r', encoding='utf8')#las letras son r read,w write,a append anexa,x exception,t para texto
print(archivo.read(5))

#iterando el archivo
#for linea in archivo:
    #print(linea)
    #print(archivo.readlines()) accedemos al archivo
#print(archivo.readlines()[int(input('ingrese el numero'))])
archivo2 = open('copia.txt', 'a',encoding='utf8')#abrimos archivo
archivo2.write(archivo.read())
archivo.close()#cerramos archivo
archivo2.close()#cerramos segundo archivo

print('se ha terminado el proceso de leer y copiar el archivo')