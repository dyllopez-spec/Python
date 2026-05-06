while True:
    try:
        rondas = 0
        cant_rondas = 1

        multiplos_2_3 = 0
        pares = 0
        impares = 0

        mayor_50 = 0

        pequenos = 0
        medianos = 0
        grandes = 0 


        # Se solicita al usuario cuantas rondas quiere jugar
        rondas= int(input("ingresa cuantas rondas que desea jugar:"))
        if rondas >= 0 and rondas <= 5: 
            # Se valida que la cantidad de rondas sea mayor a cero (0)
            if rondas > 0:
                #Se repite con ciclo el proceso la cantiddad de veces segun las rondas
                while cant_rondas <= rondas:
                    cant_rondas += 1
                    #multiplos
                    if rondas % 2 == 0 or rondas % 3 == 0:
                        multiplos_2_3 += 1
                    elif rondas % 2 == 0:
                        pares += 1
                    elif rondas % 3 == 0:
                        impares += 1
                    # rondas mayores a 50
                    if rondas > 50:
                        mayor_50 += 1
                    #Tamano del numero de la ronda pequenpo, mediano, grande
                    if rondas > 1 and rondas < 20:
                        pequenos += 1
                    elif rondas > 21 and rondas < 50:
                        medianos += 1
                    elif rondas > 50:
                        grandes += 1
                    else:
                        #si no es multiplo de 2 0 3 es energia simple
                        print("energia simple.")

                    while True :
                        n_positivo= int(input("ingresa un rondas entero positivo:"))
                        if n_positivo == 0:
                            print(f'El rondas positivo debe ser mayor a cero (0)')
                        break

                print(f'la Cantidad de rondas son {rondas}')
            else:
                print(f'La cantidad de rondas debe ser mayor a cero (0)')
        else:
            print(f'El numero debe ser un numero entre el 0 y 5')
                

    except ValueError:
        print("debes ser un rondas, vuelve a intentarlo")

