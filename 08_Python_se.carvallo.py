total_vendido = 0
cant_may_10 = 0
cant_men_10 = 0
total_may_10 = 0
total_men_10 = 0
cant_ventas = 0
avg_general =  0
avg_ventas_may_10 = 0
avg_ventas_men_10 = 0

while(True):
    opcion = int(input("""Seleccione una opción del Menu:
    1. Ingrese ventas de productos.
    2. Mostrar reporte.
    3. Salir
    > """))
    # La primera opcion debe decir Ingresar ventas de producto
    if opcion == 1:
        cant_ventas = int(input('Cuantas ventas quisiera registrar: '))

        for venta in range(0, cant_ventas):
            try:
                monto_vta = int(input('Ingrese el monto de cada venta : '))
                # Acumular el total vendido
                total_vendido += monto_vta
                # Cantidad de ventas mayores a 10000
                if monto_vta > 10000:
                    cant_may_10 += 1
                    # Total de ventas mayores a 10000
                    total_may_10 += monto_vta
                #Cantidad de ventas menores o iguales a 10000
                if monto_vta <= 10000:
                    cant_men_10 += 1
                    # Total de ventas menores e iguales a 10000
                    total_men_10 += monto_vta
                
            except ValueError:
                print('Error')

    elif opcion == 2:
        try:

            if total_vendido > 0 and cant_ventas > 0:
                avg_general =  total_vendido / cant_ventas  
            else:
                avg_general = 0

            if total_may_10 > 0 and cant_may_10 > 0:
                avg_ventas_may_10 = total_may_10 / cant_may_10
            else:
                avg_ventas_may_10 = 0 

            if total_men_10 > 0 and cant_men_10 > 0:
                avg_ventas_men_10 = total_men_10 / cant_men_10
            else:
                avg_ventas_men_10 = 0

        except ZeroDivisionError:
            print('EL numero no debe ser divisble por cero')

        print(f'Total de ventas mayores a $10.000.- CLP es de {total_may_10}')
        print(f'Total de ventas menores o iguales a $10.000.- CLP es de {total_men_10}')
        print(f'Cantidad de ventas mayores a $10.000.- CLP es de {cant_may_10}')
        print(f'Cantidad de ventas menores o iguales a $10.000.- CLP es de {cant_men_10}')
        print(f'Total de ventas {total_vendido}')
        print(f'Promedio general de ventas {avg_general}')
        print(f'Promedio de ventas mayores a $10.000.- {avg_ventas_may_10}')
        print(f'Promedio de ventas menores o iguales a $10.000.- {avg_ventas_men_10}')

    elif opcion == 3:
        print('Exit')
        break