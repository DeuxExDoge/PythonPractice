# 00 - Print
# La función print() es una de las funciones más utilizadas en Python para mostrar mensajes en la consola.
# Permite imprimir texto, variables y resultados de operaciones de manera sencilla y personalizable.
# Cabecera de la función print:
#def print(
#    *values: object,
#    sep: str | None = " ",
#    end: str | None = "\n",
#    file: SupportsWrite[str] | None = None,
#    flush: Literal[False] = False
#) -> None

#print("Hola", 5, True)
#Nos muestra: Hola 5 True
# Imprime diferentes tipos de datos en una sola línea

#print("Hola", "mundo", sep=" - ", end="!!!\n", file=open("salida.txt", "w"))
# Escribe "Hola mundo!!!" en un archivo llamado "salida.txt" con un separador personalizado y un final específico
# Este "tooltip" te muestra exactamente cómo puedes personalizar la función print() sin necesidad de buscar documentación externa.

# 01 - Types
# Los tipos de datos son impresindibles para conocer que tipos de datos estamos trabajando, utilizando y en consecuencia saber su útilidad y posibilidades de uso.
#print("Entero:", type(10), "Flotante:", type(3.14), "Cadena:", type("Hola"), "Booleano:", type(True), "Lista:", type([1, 2, 3]), "Tupla:", type((1, 2)), "Diccionario:", type({"clave": "valor"}), "Conjunto:", type({1, 2, 3}), "Nulo:", type(None))

# CTRL + K + CTRL + C. esto comenta el código seleccionado
# CTRL + K + CTRL + U. esto descomenta el código seleccionado
# alt + shift + a. esto comenta el código seleccionado con comillas triples, es útil para comentar varias líneas de código a la vez.
# alr + shift + a. esto descomenta el código seleccionado con comillas triples
#Prueba quiero saber si 5/9 es mayor o menor que 5/10
# if 5 / 9 > 5 / 10:
#     print("5/9 es mayor que 5/10")
# else:
#     print("5/9 es menor o igual que 5/10")
# Comversión de celcius a fahrenheit

# list = [1,2,3,4,5,6,7,8,9]
# print(list[-5:]) # Prueba de funcionamiento de lista

# list =[1,2,3,5]
# print(list[-1::-1])

# lista = [1,2,3]
# var = lista[0] + lista[1]
# print(var)
# Prueba para ver si puedo sumar las partes de una lista a una variable, para por ejemplo sacar un promedio

# Lista usada como rango, que pasa si tiene un cambio dentro del for
# lista = [1,2,3]
# for i in lista:
#     lista[i] += lista
# print(lista)
# Error de memoria
# Cambiar el tamaño adentro afecta al rango del for y puede generar un loop infito.
# lista = [1,2,3]
# for i in lista:
#     lista.append(i+1)
#     print(i)
# print(lista)

# Generar una lista con un rango de 20. 1 al 20.
# lista = []
# for i in range(20):
#     lista.append(i+1)
#     print(i)
# print(lista)

string = "hola"
print(string[0])