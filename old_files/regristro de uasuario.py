
def s (a,b):
        return a+b
def m (a,b):
        return a*b
def d (a,b):
        return a/b
def r (a,b):
        return a - b
while True:
 print ("--Menu principal--")
 print ("1. sumaar")
 print ("2. restar")
 print("3. multiplicar")
 print("4. dividir")
 opcion = input ("ingrese una opcion: ")
 n1= float(input())
 n2= float (input())
 if opcion=="1":
        print ("la suma es :",s(n1,n2))
 elif opcion =="2":
        print ("la resta es:",r,(n1,n2))
 elif opcion =="3":
        print("la multiplicacion es:",m(n1,n2))
 elif opcion=="4":
        print ("la division es:",d(n1,n2))