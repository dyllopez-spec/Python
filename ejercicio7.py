
"""
Descuento por compra
Ingresa el monto de una compra. Si supera $100, aplica un 10% de
descuento y muestra el total final. Si no, muestra el monto original.
"""
monto_compra = int(input("Ingrese el monto de una compra:"))
#if  0 < monto_compra:
if  monto_compra > 0:
    
   # if 100 < monto_compra:
    if  monto_compra > 100:
        dscto = monto_compra * 0.10
        compra_dscto = monto_compra - dscto
        print(f"su monto total es {compra_dscto}su compra tiene un descuento del 10%")
    else:
        print(f"su monto compra es {monto_compra}")

else:
    print(f"El monto debe ser mayor a 0.")