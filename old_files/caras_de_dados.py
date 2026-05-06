import random
lanzamientos= [random.randint (1,6)for i in range (50)]
for cara in range (1,7):
    cantidad= lanzamientos.count (cara)
    print(f"cara{cara}: salio {cantidad} veces")