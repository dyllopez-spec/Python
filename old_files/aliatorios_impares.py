
import random 
contador_par=0
contador_impar=0
for i in range(100):
    num = (random.randint (1,100))
    print(f"{i}:{num}")
    if num % 2==0:
        contador_par+=1  
    elif num % 2==1:
       contador_impar+=1

print (f"los numeros pares son: {contador_par}")   
print (f"los numeros impares son: {contador_impar}")
