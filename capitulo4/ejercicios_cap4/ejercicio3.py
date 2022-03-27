Compras_superiores=float(input("Digite el precio de la compra: $"))
descuento=float(input("digite el decuento de la compra: "))
Balota=input("digite el color de la balota: ")

descuento=Compras_superiores*descuento
d=Compras_superiores-descuento

if Compras_superiores>=50.000 and Balota=='Roja':
    descuento==Compras_superiores*descuento and d==Compras_superiores-descuento
    print(f"Valor de la valota={Compras_superiores}\nValor del decuento={descuento}\nValor a pagar aplicado al decuento={d}")
elif Compras_superiores>=50.000 and Balota=='Verde':
    descuento==Compras_superiores*descuento and d==Compras_superiores-descuento
    print(f"Valor de la valota={Compras_superiores}\nValor del decuento={descuento}\nValor a pagar aplicado al decuento={d}")
elif Compras_superiores>=50.000 and Balota=='Blanca':
    descuento==Compras_superiores*descuento and d==Compras_superiores-descuento
    print(f"Valor de la valota={Compras_superiores}\nValor del decuento={descuento}\nValor a pagar aplicado al decuento={d}")
elif Compras_superiores>=50.000 and Balota=='Negra':
    descuento==Compras_superiores*descuento and d==Compras_superiores-descuento
    print(f"Valor de la valota={Compras_superiores}\nValor del decuento={descuento}\nValor a pagar aplicado al decuento={d}")
elif Compras_superiores>=50.000 and Balota=='Amarilla':
    descuento==Compras_superiores*descuento and d==Compras_superiores-descuento
    print(f"Valor de la valota={Compras_superiores}\nValor del decuento={descuento}\nValor a pagar aplicado al decuento={d}")
else:
    print("No aplica el decuento y el valor a pagar")