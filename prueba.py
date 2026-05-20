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
                        cantidad_productos=int(input("ingrese la cantidad de productos:"))
                        if cantidad_productos < 0:
                            print("la cantidad de productos deben ser mayores a 0")
                    except ValueError:
                        print("debe ser un numero no letras. ")
            for i in range(cantidad_productos):
                while True:
                    try:
                        monto=int(input("ingrese el monto que desea:"))
                        if monto < 0:
                            print("el monto debe ser mayor a 0")
                    except:
                        print("solo debe ingresar numeros dentro del monto.")
