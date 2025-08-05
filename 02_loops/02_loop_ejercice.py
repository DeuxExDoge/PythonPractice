###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
pares = []
for i in range(2,21,1): # Aquí aprendi la clase range que transforma nuestros números en un rango, esto no existia en c ahí solo colocabas un contador numero y eso lo ibas sumando. Podrias poner que vaya de 2 en 2 que seria lo mismo porque esos son los pares.
    if i % 2 == 0:
        pares.append(i) # Me parece muy buena y lógica la utilización del append. Yo estaba pensando en cosas como guardar en cada celda una por una la variable. entonces esto deberia guardar en otra variable para hacer los pasos y un quilombo.
print(f"Estos son los números pares")
print(pares)

print("\nEjercicio 2:")
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
media = 0
for i in range(len(numeros)):
    media += numeros[i]
    print(i)
print(f"La media es {media/len(numeros)}, media es : {type(media)}")
print(f"El rango de una lista es: {range(len(numeros))}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
mayor = numeros[0]
for i in range(len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]
print(mayor)
# Otra forma
mayor = max(numeros) # Usando la función max.
print(f"El número máximo de la lista es: {mayor}")
# Otra forma
mayor = sorted(numeros)[-1] # Usando la función sorted y accediendo al último elemento.
print(f"El número mayor es el: {mayor}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
cinco_letras =[]
for i in range(len(palabras)):
    if len(palabras[i]) >= 5:
        cinco_letras.append(palabras[i])
print(f"Las palabras con 5 caracteres son: {cinco_letras}")
# Otra forma
cinco_letras = [x for x in palabras if len(x) >= 5] # Es una forma ingeniosa, compacta de resolver el ejercicio. List comprehension.
print(f"Las palabras con 5 caracteres son: {cinco_letras}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
letra = input("Escribi una letra ").lower()
var = 0
palabras.sort(key=str.lower)
# for i in range(len(palabras)):
#     for x in palabras[i]: 
#         if x == letra:
#             print(i,x,letra,palabras[i])
#             var += 1
# print(var,palabras,letra) No se si funcaria pero no podemos dar cuenta que no es ni la más optima ni la mejor manera.
for i in range(len(palabras)):
    if letra == (palabras[i])[0]:
        var += 1
print(f"La letra '{letra}' aparece como primera letra en {var} palabra(s) de nuestra lista.")

