jugador_1=input("digite la opcion del jugador_1: ")
jugador_2=input("digite la opcion del jugador_2: ")

if jugador_1==jugador_2:
    print(f"los jugadores han empatado")
    
elif jugador_1=="papel" and jugador_2=="piedra":
    print("¡Gana! jugador_1: el papel envuelve la piedra")
elif jugador_1=="papel" and jugador_2=="tijera":
    print("¡Gana¡ jugador_2: la tijera corta papel")
elif jugador_1=="piedra" and jugador_2=="tijera":
    print("¡Gana! jugador_1: la piedra rompe tijera")
    
elif jugador_2=="tijera" and jugador_1=="papel":
    print("!Gana¡ jugador_1: la tijera corta papel")
elif jugador_2=="papel" and jugador_1=="piedra":
    print("¡Gana! jugador_2: el papel envuelve la piedra")
elif jugador_2=="piedra" and jugador_1=="tijera":
    print("¡Gana! jugador_2: la piedra rompe tijera")
    