def isMutant(dna):
    count = 0
    for i in range(6):
        for j in range(3):
            if dna[i][j] == dna[i][j+1] == dna[i][j+2] == dna[i][j+3]:
                count += 1
            if dna[j][i] == dna[j+1][i] == dna[j+2][i] == dna[j+3][i]:
                count += 1
    for i in range(3):
        for j in range(3):
            if dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                count += 1
            if dna[i][5-j] == dna[i+1][4-j] == dna[i+2][3-j] == dna[i+3][2-j]:
                count += 1
    if contadorDeCoincidencia > 1:
        return print("El adn es de un mutante")
    else:
        return print("El adn es de una persona normal")

dna = []
for i in range(6):
    while True:
        cadena = input("Ingrese la " + str(i+1) + " secuencia del ADN: ")
        cadena = cadena.upper()
        if set(cadena) <= set("ATGC") and len(cadena) == 6:
            dna.append(cadena)
            break
        else:
            print("Secuencia inválida. Por favor, ingrese una secuencia de 6 caracteres con las letras A, T, G, C.")
print(isMutant(dna))
