
"""
Ejercicio 1:

Mayor de dos números
Solicita dos números al usuario y muestra cuál es el mayor. Si son
iguales, indícalo
"""
num1 = int(input("ingrese su primer numero:"))
num2= int(input("ingrese su segundo numero:"))
if num1 > num2:
    print(f"el numero mayor es :{num1}")
elif num1 < num2:
    print(f"el numero maayor es :{num2}")
elif num1 == num2:
    print(f"los numeros son iguales")
