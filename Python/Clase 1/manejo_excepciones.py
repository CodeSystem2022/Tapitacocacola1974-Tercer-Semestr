from NumerosIgualesExeption import NumerosIgualesExeption

resultado = None

try:
    a = int(input("Digite el primer numero: "))
    b = int(input("Digite el segunto numero: "))
    if a == b:
        raise NumerosIgualesExeption("Son iguales")
    resultado = a / b #modificamos
except TypeError as e:
    print(f"Type Error - Ocurrió un error {type(e)}")
except ZeroDivisionError as e:
    print(f"Zero División - Ocurrió un error {type(e)}")
except Exception as e:
    print(f"Exeption - Ocurrió un error {type(e)}")
else:
    print("No encontró excepciones")
finally: #Siempre se va a ejecutar
    print(f"Ejecución de este bloque finally")
print(f"El resultado es: {resultado}")
print("seguimos...")
