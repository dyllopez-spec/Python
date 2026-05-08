#librearia que genera numeros aleatorios 
import random 
#por cada iteracion aumentara en 1 
contador_par=0
contador_impar=0
count=0
#generara una iteracion de 100 veces
#for i in range(100):
#iteracion con ciclo while de entre 1 y 100
while (count < 100):
    count += 1
    #por cada iteracion generara un numero aleatorio entre el 1 y el 100
    num = (random.randint (1,100))
    #condicionamos si el numero es par o impar,identificando segun su residuo numerico
    if num % 2==0:
        #cuanta cada numero aleatorio par
        contador_par+=1  
    elif num % 2==1:
       #cunta cada numero aleatorio impar
        contador_impar+=1
#mensaje   
print (f"los numeros pares son: {contador_par}")  
print (f"los numeros impares son: {contador_impar}")