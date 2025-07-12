###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje = mensaje[-7:-2] + ["t","o"]# 
print(mensaje)

mensaje_dos = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_dos = mensaje_dos[7:12] + ["t","o"]
print(mensaje_dos)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros[0] = 50
numeros[-1] = 10
print(numeros)

numeros[0] 
# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
sandwich = pan, ingredientes, pan_abajo # Lista dentro de listas
print(sandwich)
sandwich = pan + ingredientes + pan_abajo # Una sola lista
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
lista += lista
print(lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
lista = [10, 20, 30, 40, 50] # -> El centro es 30
# lista[int(len(lista)/2)] = None # Duda que me surgio, se como sumar/concatenar, pero donde esta la sustracción o la resta en las listas siempre agrego nunca saco datos.Resultado : [10, 20, None, 40, 50]
lista = lista[:int(len(lista)/2)] + lista[int(-len(lista)/2):] # Encontramos en la lista impar el elemento del medio de la lista usando slicing y no lo incluimos en la última iteración de la lista.
print(lista)
#lista2 = lista[::-1]  and lista[:] Esto funciona raro me copia el segundo con el and y el primero con el or, no se igual que intento usando estos comparadores para booleanos con lsitas

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]