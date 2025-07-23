# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumple una condición
print("\n Bucle while:")

# Bucle con una simple condición
contador = 0
# while contador < 5:
#     print(contador)
#     contador +=1 # Importante para evitar bucles infinitos. Nos muestra los números del 0 al 4.

# while True:
#     print("Hola") # Bucle infinito

# Utilizamos la palabra break, para romper el bucle
print('\n Bucle while con break')
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # Sale del bucle

# continue, lo que hace es saltar esa iteración en concreto y continuar con el bucle
print('\n Bucle con continue')
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 ==0:
        continue # El continue va a la siguiente iteración, en esos casos ignorara el código de abajo.
    print(contador)
# Este codigo nos muestra números que no son divisibles por 2.
# Es una buena optimización de los bucles para saltear iteraciones inecesarias.

# else, esta condición cuando se ejecuta?
print('\n Bucle while con else')
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    break
else:
    print('Termino la cuenta wuachin') 
# Usa else si quieres ejecutar algo solo cuando el ciclo terminó de forma natural (sin break). No saldra el mensaje porque el break interrumpio todo el proceso, nuestro contador no hizo la la preposición sea false y por ello no printea.

print('\n Bucle while sin else')
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    break
print('Termino la cuenta wuachin') 
# Printea igual.

# Pedir al usuario un número positivo sino, no le dejamos en paz.
# numero = -1
# while numero < 0:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0 :
#         print(" El número debe ser positivo. Intata otra vez wuachin.")

# print(f"El número que has introducido es {numero}")

# Usando el try para manejar errores. Hay mejores formas aparantemente.
numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:    
            print(" El número debe ser positivo. Intata otra vez wuachin.")
    except:
        print("Introduzca solamente números. Por favor.")
    
print(f"El número que has introducido es {numero}")
