while True:
    mensaje = input("que mensaje deseas cifrar: ")
    abecedario = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM "
    key = 2
    copia = ""
    desbloqueo = ""

    for i in range(len(mensaje)):

        if mensaje[i] not in abecedario:
            copia += mensaje[i]

        for j in range(len(abecedario)):
            
            if mensaje[i] == abecedario[j]:
                copia += abecedario[(j + key) %len(abecedario)]
            
    print(copia)
    print()

    for i in range(len(copia)):

        if copia[i] not in abecedario:
            desbloqueo += copia[i]
            
        for j in range(len(abecedario)):
            
            if copia[i] == abecedario[j]:
                desbloqueo += abecedario[(j - key) %len(abecedario)]
                    
    print(desbloqueo)

    pregunta = input("quieres volver a cifrar [si/no]: ").strip().lower()

    if pregunta == "si":
        print("\033[2J\033[H", end="")
    else:
        break