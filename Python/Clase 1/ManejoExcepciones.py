from NumerosIgualesException import NumerosIgualesException
resultado = None

#a = 10 cambiamos por un string
#a = 7
#b = 0 #variables que estan fuera del try, tambien pueden ir dentro
try:
    a = int(input("Digite el primer numero:")) #las variables pueden ser pedidas al usuario
    b = int(input("Digite el segundo numero: "))
    if a == b:
        raise NumerosIgualesException("Son numeros iguales")
    resultado = a / b #modificamos
except TypeError as e:
    print(f"TyperError - Ocurrio un error¨{type(e)}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionErorr - Ocurrio un error¨{type(e)}")
except Exception as e: #se puede procesar con una excepcion de menor jerarquia
#except ZeroDivisionError as e: #cambiamos a excepcion nuevamente
    print(f"Excepcion - Ocurrio un error: ¨{type(e)}")
else:
    print("No se arrojo ninguna excepcion")
finally: #siempre se va a ejecutar
    print("Ejecucion de este bloque finally") #utilizar para poder liberar algun recurso
    # o avisarle al usuario como termino el manejo de escepciones.

print(f"El resultado es: {resultado}")
print(f'seguimos...')
