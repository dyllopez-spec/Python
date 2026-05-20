acumulador_total = 0
acumulador_mayor = 0
acumulador_menor = 0
contador_mayor = 0
contador_menor = 0 


while True:
        print("===== MENU PRINCIPAL =====")
        print("Opcion[1] - Ingrese la ventas de productos.")
        print("Opcion[2]- Moatrar el reporte.")
        print("Opcion[3] - salir de este menu.")
        while True:
            try:
                opcion=int(input("ingrese  la opcion que deseas:"))
                if opcion != 1 and opcion != 2 and opcion != 3:
                    print("debe ingresar una de las opciones disponibles.")
            except:
                print("deben ser ingresados solo numeros.")
            if opcion == 1:
                while True:
                    try:
                        canidad_ventas=int(input("ingrese la cantidad de ventas:"))
                        if canidad_ventas < 0:
                            print("la cantidad de productos deben ser mayores a 0")
                    except:
                        print("debe ser un numero no una letra. ")
                    for ventas in range(0,canidad_ventas):
                            try:
                                monto=int(input("ingrese el monto del producto:"))
                                if monto < 0:
                                    print("el monto debe ser mayor a 0")
                            except:
                                print("porfavor ingrese el monto del producto.")
            
                            if monto > 10000:
                                acumulador_mayor += monto
                                contador_mayor += 1
                            elif monto <= 10000:
                                acumulador_menor += monto
                                contador_menor += 1 
                            
                                
                            



        