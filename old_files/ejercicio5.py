
"""
    Ejercicio 5
Verificar mayoría de edad
Solicita la edad e indica si es mayor de edad (18 o más) o menor.
"""
edad =  int(input("ingrese su edad:"))
if 0 <= edad <= 120:
    print(" ")
    if edad >= 18:
        print(f"la edad {edad} es mayor de edad.")
    else:
        print("es menor de edad.")
else:
    print (f"estas fuera del rango etario.")