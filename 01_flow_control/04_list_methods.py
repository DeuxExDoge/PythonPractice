# 04 - Listas métodos
# Los métodos más importantespara trabajar con listas.

from os import system
if system("clear") != 0: system("cls")

# Añadir o insertar elementos a la lista

lista1 = ['a','b','c','d']
lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posición que le indquemos como primer argumento.
print(lista1)

lista1.extend(['f','g','@']) # Agrega elementos al final de la lista.
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Elimina la primera aparación de la cadena de texto @. Amigo aquí estaba el borrador. Le pasamos el elemento que queremos borrar.
print(lista1)

ultimo = lista1.pop() # Elimina el último elemento de la lista y te lo devuelve.
print("La lista: ", lista1 , "último elemento de la lista: ", ultimo)

lista1.pop(1) # Eliminar el segundo elemetno de la lista (es el índice 1)
print(lista1)

del lista1[-1] # Elimina el último elemento. Sintaxis y no metodo.
print(lista1)

lista1.clear() # Eliminar todos los elemetnos de la lista
print("Eliminamos todos los elementos de la lista:", lista1)

# Eliminar un rango de elementos
lista1 = ['Cha','Che','Chi','Cho','Chu']
del lista1[1:]
print(lista1)

# Ordenar lista sort
print('Ordenar listas modificando la original')
numeros = [3,10,2,8,100,23423]
numeros.sort() # Esto modifica la lista.
print(numeros)

print('Ordenar listas creando una nueva lista')
number = [3,1,2,8,100,23423]
numeros_sorted = sorted(numeros)
print(numeros_sorted)

print("Ordenar cadenas de texto")
frutas = ['manzana', 'pera','limón','manzana','pera','limon']
frutas_sorted = sorted(frutas)
print(frutas_sorted)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['Manzana', 'Pera','limón','manzana','Pera','limon']
frutas_sorted = sorted(frutas)
print(frutas_sorted)
frutas.sort(key=str.lower) # Le aclaramos que cuando ordene la lista de frutas se fije que nuestros strings esten en lower case para ordenar y asi ignora mayusculas y no las pone primero por su distinto ponderación.
print("Las frutas:",frutas)

# Más cosas útilies
animals = ['Panda', 'Koala', 'Perro', 'Perro']
print(len(animals)) # Tamaño de la lista
print(animals.count('Perro')) # Cuenta si encontro un Perro.
print('Perro' in animals) # Comprueba si hay un 'Perro' en la lista -> True
print('NoEsta' in animals) # -> False 