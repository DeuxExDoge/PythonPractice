# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
import os # Libreria de modulos de sistema operativo, nos permite limpiar la consola.

os.system("cls")  # Limpia la consola en sistemas Unix/Linux. En Windows, usar "cls".

# Creación de listas
print("\nCrear listas")
# Usamos llaves para crear las listas []
lista = [1,2,3,4,5] # lista de enteros
lista2 = ["manzanas","peras","bananas"] # lista de cadenas
lista3 = [1, "hola", True, 3.14] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1,2], [3,4]]
matrix = [[1,2], [2,3], [4,5]]

print(lista)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])# manzanas
print(lista2[1])# peras
print(lista2[-1]) # banana. Posición menos 1 significa la ultima
print(lista2[-2]) # peras

print(lista_de_listas[1][0]) # 3

# Slicing de listas
list = [1,2,3,4,5]
print(list[1:4]) # Es como un intervalo abierto # [2,3,4]
print(list[:3]) # [1,2,3] # Es desde la posición 3. Seria desde el número 4 en esta caso hacia atras.
print(list[3:]) # [4,5] # Seria desde la posición 3 hacia a delante. Es decir desde el 4 hacia adelante. Si no me equivoco la posición 3 esta entre el 4 y el tres y por ello es que surge esta sitación de que en uno elige al 4 y el otro no, es completamente lógico y cumple con su objetivo si tuvieramos 6 números almacenados en la lista la dsitribución seria par.
print(list[2:])
print(list[:]) # [1,2,3,4,5] # Toda la lista.
print(list[:-1]) # [1,2,3,4] # Seria desde la última posición hasta la primera.

# MORE MAGIC
list = [1,2,3,4,5,6,7,8]
#print(list[desde:hasta:paso]) # ????
print(list[::2])# list[desde el inicio: hasta el final: de dos en dos] # [1,3,5,7]. Recorre la lista de dos en dos. Selecciona las posiciones par de la lista [0],[2],[4],etc. Se puede ver el movimiento de izquierda a derecha o de derecha a izquierda. Yo recuerdo que me enseñaron de derecha a izquierda.
print(list[::3])# Devuelve 3 en 3.
print(list[::-1])# Pasos invertidos, lista al revés.

# Modificar una lsita
list[0] = 20
print(list)

# Añadir elementos a una lista
list = [1,2,3]

# forma larga y menos eficiente
list = list + [4,5,6] # Concatenación de listas
print(list)

# forma corta y más eficiente
list += [7,8,9]
print(list)


# Recuperar el largo de una lista
print("El largo de la lista es de ", len(list))

