import random

Lista = ["Piedra", "Papel", "Tijeras"]

contrario = random.choice(Lista)

print("[P]iedras, [Pa]pel, [Tijeras]: ")

while True:
    
    eleccion = str(input("elige una de las opciones: "))   
    
    if eleccion not in ["P", "Pa", "T"]:
        print("Elige solo las opciones mostradas por pantalla")
        continue
    else:
        break

if eleccion == "P" and contrario == "Tijeras":
    print("Ganaste")

elif eleccion == "Pa" and contrario == "Tijeras":
    print("Perdiste")
    
elif eleccion == "T" and contrario == "Tijeras":
    iprint("Empate")

elif eleccion == "P" and contrario == "Piedra":
    print("Empate")
    
elif eleccion == "Pa" and contrario == "Piedra":
    print("Ganaste")
    
elif eleccion == "T" and contrario == "Piedra":
    print("Perdiste")

elif eleccion == "P" and contrario == "Papel":
    print("Ganaste")
    
elif eleccion == "Pa" and contrario == "Papel":
    print("Empate")
    
elif eleccion == "T" and contrario == "Papel":
    print("Perdiste")
    
else:
    print("hola")
    
