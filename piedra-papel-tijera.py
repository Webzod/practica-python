jugador1 = input ("Seleccion de jugador 1: ")
jugador2 = input ("Seleccion de jugador 2: ")

#Escenarioas donde gana el jugador 1
if jugador1 == "piedra" and jugador2 == "tijera":
    print ("Gana jugador 1")

elif jugador1 == "tijera" and jugador2 == "papel":
    print ("Gana jugador 1")

elif jugador1 == "papel" and jugador2 == "piedra":
    print ("Gana jugador 1")

#Escenarios donde gana el jugador 2
elif jugador1 == "tijera" and jugador2 == "piedra":
    print ("Gana jugador 2")

elif jugador1 == "papel" and jugador2 == "tijera":
    print ("Gana jugador 2")

elif jugador1 == "piedra" and jugador2 == "papel":
    print ("Gana jugador 2")

else:
    print ("Empate")
    
    

