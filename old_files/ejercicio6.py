
"""
    Ejerciocio 6 
Número dentro de un rango
Pide un número e indica si está entre 1 y 100 (inclusive).
"""
numero= int(input("ingrese un numero:"))
if 1 <= numero <= 100:
    print(f"el numero esta dentro del rango.")
else:
    print(f"el numero esta fuera del rango.")