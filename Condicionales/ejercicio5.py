Edad=int(input("digite su edad: "))
peso=int(input("digite su peso: "))
latidos_corazon=int(input("digite sus latidos de corazon por minuto: "))
plaquetas=int(input("digite la cantidad normal de plaquetas: "))

if Edad>18 and Edad<65:
    peso>50 and peso<82
    latidos_corazon>60 and latidos_corazon<100
    plaquetas==150000
    print("¡Apto! para donar sangre")
else:
    print("¡No! es apto para donar sangre")