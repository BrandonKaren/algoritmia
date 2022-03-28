n1=int(input("digite el numero n1: "))
n2=int(input("digite el numero n2: "))
n3=int(input("digite el numero n3: "))

if n1<n2<n3 or n1<n2>n3:
    print(f"el numero menor es: {n1}")
elif n2<n1<n3 or n2<n3>n1:
    print(f"El numero menor es: {n2}")
elif n3<n2<n1 or n3<n1>n2:
    print(f"El numero menor es: {n3}")
elif n1==n2:
    print(f"Se digitaron 2 numeros iguales:\nn1={n1}\nn2={n2}")
elif n1==n3:
    print(f"Se digitaron 2 numeros iguales:\nn1={n1}\nn3={n3}")
elif n2==n3:
    print(f"Se digitaron 2 numeros iguales:\nn2={n2}\nn3={n3}")
else:
    print("Los 3 numeros digitados son iguales")