
"""
    Ejercicio 4 
Aprobado o reprobado
Pide una calificación del 0 al 100 y muestra "Aprobado" si es 60 o más,
o "Reprobado" en caso contrario.
"""
Calificacion = int(input("ingrese una nota del 0 al 100:"))
#if Calificacion >= 0 and Calificacion <= 100:
if 0 <= Calificacion <= 100:
   # print("okay")
    if Calificacion >= 60:
        print(f"la calficacion esta aprobada.")
    else:
        print(f"la calificacion esta reprobada.")
else:
    print("el numero esta fuera del rango")
