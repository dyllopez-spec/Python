"""
    Ejercicio 3 
Positivo, negativo o cero
Ingresa un número y determina si es positivo, negativo o cero.
"""
num1 = int(input("ingrese un numero:"))
if num1 > 0:
    print(f"El numero {num1} es mayor a 0")
elif num1 < 0:
    print(f"El numero {num1} es menor a 0")
elif num1 == 0:
    print(f"los numeros son iguales")
