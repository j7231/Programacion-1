import random

def SumaCartas(cartas):
    total = 0
    ases = 0
    
    for carta in cartas:
        valor = carta[0] 
        if valor == "AS":
            ases += 1
            total += 11
        elif valor in ["J", "Q", "K"]:
            total += 10
        elif valor in ["2","3","4","5","6","7","8","9","10"]:
            total += int(valor)
            
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
        
    return total
#-----------------------------------

jugar = "SI"
saldo = int(input("Cuanto dinero tienes para apostar? (mínimo 100): "))
    
while saldo < 100:
    print("\nSaldo insuficiente, ocupas minimo 100 para apostar")
    saldo = int(input("\nCuanto dinero tienes para apostar? (mínimo 100): "))

while jugar == "SI" and saldo >= 50:
    valores = ["AS", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]
    palos = ["♥", "♦", "♣", "♠"]
    baraja = []
    cartas = [] 
    cartasRival = []

    for palo in palos:
        for valor in valores:
            baraja.append([valor, palo])

    apuesta = int(input(f"\ncuanto apuestas? Tu saldo es de {saldo} (la apuesta minima es de 50): "))

    while apuesta > saldo:
        print("\nno puedes apostar mas dinero del que tienes")
        apuesta = int(input(f"\n¿Cuánto apuestas? Tu saldo es de {saldo}: "))
    
    while apuesta < 50:
        print("\nla apuesta minima es de 50")
        apuesta = int(input(f"\nCuanto apuestas? Tu saldo es de {saldo}: "))
        
    random.shuffle(baraja)
    print("\ntus dos cartas son:")
    
    cartas.append(baraja.pop())
    cartas.append(baraja.pop())

    print(f"{cartas[0]}\n{cartas[1]}")
    print(f"Total actual: {SumaCartas(cartas)}")

    
    cartasRival.append(baraja.pop())
    print(f"El rival pide carta y recibe: {cartasRival[-1]}")

    while True:
        unaMas = input("\nQuieres una carta mas [SI/NO]: ").strip().upper()
        
        if unaMas == "SI":
            cartas.append(baraja.pop())
            print(f"Nueva carta: {cartas[-1]}")  
            print(f"Total actual: {SumaCartas(cartas)}")
            
            if SumaCartas(cartas) > 21:
                print("Tienes más de 21, perdiste.")
                saldo -= apuesta
                jugar = input("¿Quieres volver a jugar? [SI/NO]: ").upper().strip()
                print("\033[2J\033[H", end="")
                break
        else:
            break

    print("\n--- Cartas de tu rival ---")
    cartasRival.append(baraja.pop())
    cartasRival.append(baraja.pop())

    print(f"{cartasRival[0]}\n{cartasRival[1]}")

    while True:
        if SumaCartas(cartasRival) < 17:
            cartasRival.append(baraja.pop())
            print(f"El rival pide carta y recibe: {cartasRival[-1]}")
        else:
            print(f"El rival tiene con: {SumaCartas(cartasRival)}")
            break

    totalJugador = SumaCartas(cartas)
    totalRival = SumaCartas(cartasRival)
    print(f"\nTu total: {totalJugador} | Total del rival: {totalRival}")

    if totalJugador > totalRival or totalRival > 21:
        print("Ganaste")
        saldo += apuesta
    elif totalJugador == totalRival:
        print("Empate")
    elif totalJugador < totalRival or totalJugador > 21:
        print("Perdiste")
        saldo -= apuesta
        
    if saldo >= 50:
        jugar = input("\n¿Quieres volver a jugar? [SI/NO]: ").upper().strip()
        print("\033[2J\033[H", end="")
    else:
        break

if jugar == "NO":
    print("saliendo...")
    exit()
    
print("\nYa no puedes jugar, no tienes saldo suficiente.")