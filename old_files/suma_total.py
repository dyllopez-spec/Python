import random
suma_total=0
while suma_total <= 500:
    num=(random.randint (10,50))
    suma_total+= num
    print (num)
print(f"su suma total es: {suma_total}")