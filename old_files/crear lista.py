
import random 
contador_zero=0
acumulador_temp25=0
total=0
for i in range (30):
    temperatura= (random.randint(-5,35))
    print(temperatura)
    total+=temperatura %2
    if temperatura < 0:
        contador_zero+=1
    elif temperatura > 25:
        acumulador_temp25+=1
print(f"los grados menores a 0 son: {contador_zero}")
print(f"los grados mayores a 25 son: {acumulador_temp25}")
print(total)