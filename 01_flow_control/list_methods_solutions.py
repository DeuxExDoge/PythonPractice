###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###
from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
numbers = [1,2,3,4,5]
# Añade el número 6 al final usando append().
numbers.append(6)
print(numbers)
# Inserta el número 10 en la posición 2 usando insert().
numbers.insert(2,10)
print(numbers)
# Modifica el primer elemento de la lista para que sea 0.
numbers.pop(0)
numbers.insert(0,0)
print(numbers) # Output: [0, 2, 10, 3, 4, 5, 6]

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
lista_a.extend(lista_b)
print("Extendemos la lista a con .extend de la b: ", lista_a)
# lista_a.extend(lista_b),lista_a.append(lista_b),lista_a.insert(0,lista_b) # Interesante como el insert agrega la lista, el append tambien, en cambio el extend solo los valores de la lista. # Resultado: [[4, 5, 6, 1, 2], 1, 2, 3, 4, 5, 6, 1, 2, [4, 5, 6, 1, 2]]
# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
print("Printeamos la lista a donde removimos la primera aparición del número 1:", lista_a)
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
elemento_eliminado = lista_a.pop(3)
print("Este es el elemento eliminado de la lista en la posición 3:", elemento_eliminado)
# Limpia completamente lista_b usando clear().
lista_b.clear() # Si no pones los parentesis al final () no borra nada xd.
print("La lista a:", lista_a ,"La lista b:", lista_b) # La lista a: [2, 3, 4, 6, 1, 2] La lista b: []

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
list = [1,2,3,4,5,6,7,8,9,10]
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
del list[2:5] # list[DESDE:HASTA:CUANTO]
# Imprime la lista resultante.
print(list) # [1, 2, 6, 7, 8, 9, 10]

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
numeros = [5, 2, 8, 1, 9, 4, 2]
# Ordena la lista de forma ascendente usando sort().
# numeros.sort(
#     reverse = True
# ) # Todo gracias a leer como funciona. La documentación de las funciones, metodos es muy útil.
numeros.sort()
print(numeros) # [1, 2, 2, 4, 5, 8, 9]
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
print(numeros.count(2))
# Comprueba si el número 7 está en la lista usando in.
print(7 in numeros)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
original = [1,2,3]
# Crea una copia de la lista original llamada copia_1 usando slicing.
copia_1 = original[:]
print(copia_1)
# Crea otra copia llamada copia_2 usando copy(). # No nos enseño copy el wuachin.
copia_2 = copia_1.copy()
print(copia_2)
# Crea una referencia a la lista original llamada referencia.
referencia = original
# Modifica el primer elemento de la lista referencia a 10.
original[0] = 10
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("Original:", original,"Copia 1:",copia_1,"Copia 2:",copia_2,"Referencia:",referencia)
# Por lo que entendi generan objetos nuevos, por ello no son una referencia del objeto original como referencia entonces por ello no comparten los cambios. Se supone que solo en listas plana, no en sublistas, diccionarios, entre otros. Para eso existe .deepcopy()


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
frutas = ["Manzana", "pera", "BANANA", "naranja"]
# Sin distinción de mayúsculas y minúsculas.
frutas.sort(key=str.lower)
print(frutas) # ['BANANA', 'Manzana', 'naranja', 'pera']

#frutas.sort # Cambia nuestra lista.
# frutas_sorted = sorted(frutas)
# print(frutas_sorted)
# prueba = ["ab","Aa","aA","Ab","aB","CCC","BBB","A","B","AA","aa","AB","a"] # Podemos entenderlo como que primero agrega un valor por orden del abecedario, ej. la a=1,5 y luego si nuestra letra esta en mayuscula eso le da una ponderación más baja, ej. A=1, cada letra va añadiendo más valor, mientras más valga más abajo en nuestra lista va a estar y por ultimo se fija en posicionamiento si son iguales, el que este antes en nuestra lista ira primero y el otro después o quizas aleatorio. Tambien se podria hacer por comparación siendo que las mayusculas son menor, si tenes menos terminos sos menor. Iria en un orden de Mayusculas < Abecedario < Tamaño < Posicionamiento. Por ejemplo : En el caso de AA vs B como ambos son mayusculas se encuentra iguales, pero en el momento que nuestra B esta después en el abecedario el resto de caracteristicas dejan de miportar ya es superior, no importa el tamaño, ni el posicionamiento. Este posicionamiento se repite con las minusculas, este proceso se debe hacer con cada elemento, por eso podemos decir que  a es menor que aA. Es como que todos empiezan en 0 y cada cosa va suamdno, una a minuscula suma 24, en cambio una a mayuscula suma 1 por eso si tenes una a y una aA es mayor aA. Me pregunto si cualquier cantidad mayuscula sera siempre considerado menor a una a.
# prueba.sort() # No te olvidez de los parentesis que sino no hace nada y estas conspirando contra la nada misma.
# print(prueba)