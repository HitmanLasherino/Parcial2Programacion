# Parcial 2 Programacion Mutantes
+ Nombre y Apellido: Franco Agustin Albornoz
+ Legajo: 51474
+ Email Escolar: francoa.albornoz@alumnos.frm.utn.edu.ar
+ Email: franquito45@live.com
## Proyecto Mutantes
El proyecto consiste en desarrollar un programa que pueda detectar si un humano es mutante basándose en su secuencia de ADN.
## Así fue resuelto
Se creó una función en Python llamada isMutant que toma como parámetro un array de Strings que representan cada fila de una tabla de (6x6) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representan cada base nitrogenada del ADN.

La función isMutant verifica si hay más de una secuencia de 4 letras iguales en horizontal, vertical o diagonal en el array de cadenas. Si encuentra más de una secuencia de 4 letras iguales, devuelve “El ADN es de un mutante”. De lo contrario, devuelve “El ADN es de una persona normal”.

Además, se creó un bucle que solicita al usuario que ingrese 6 secuencias de ADN. Si la secuencia ingresada es válida (es decir, contiene solo las letras A, T, G, C y tiene una longitud de 6), la secuencia se agrega a la lista dna. Si la secuencia no es válida, el programa solicita al usuario que ingrese una nueva secuencia.
## Como correrlo
Para correr el programa, simplemente necesitas tener Python instalado en tu computadora. Luego, puedes copiar y pegar el código en un archivo .py y ejecutarlo desde la línea de comandos. El programa te pedirá que ingreses las secuencias de ADN una por una. Después de ingresar las 6 secuencias, el programa te dirá si el ADN es de un mutante o de una persona normal.
```
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
    if count > 1:
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
```
