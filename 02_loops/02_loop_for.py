# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERa un iterable o una lista

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "pedro"
for caracter in cadena:
    print(caracter)

# enumarate()
frutas = ["manzana", "pera", "mandarina"]
for i, value in enumerate(frutas):
    print(f"El ínidice es {i} y la fruta es {value}")

# Bucles anidados
letras = ["A","B","C"]
numeros = [1,2,3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


# break
print("\nbreak")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for animal in animales:
    print(animal)
    if animal == "loro":
        print(f"El loro está escondido en el índice {i}")
        break
# Como solo queriamos que busque el loro, evitamos más trabajo usando break.
# Lo mismo se podria hacer usando continue.
# Continue. Salteamos loro porque no necesitamos usarlo.
print("\ncontinue")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for animal in animales:
    print(animal)
    if animal == "loro":
        print(f"El loro está escondido en el índice {i}")
        continue

# Comprensión de listas (list comprehension).
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números paraes de una lista
pares = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
print(pares)
# Hay mejores formas. Hicimos la lista a mano.