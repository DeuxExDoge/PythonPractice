###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Hola, me llamo Pepe")
print("Vivo en Argentina")
# Otra forma
print("Mi nombre es : Pepe\nVivo en Argentina")
# Otra forma
print("Mi nombre es : Pepe", "Vivo en Argentina", sep="\n")
# Otra forma
print("Mi nombre es : Pepe", end="\n")
print("Vivo en Argentina", end="\n")
# Otra forma
nombre = "Pepe"
ciudad = "Argentina"
print(f"Mi nombre es: {nombre}\nVivo en: {ciudad}")  # Usando f-strings para formatear la salida


print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159 # '1e3' esto seria un float.
c = "Hola mundo" # Un input seria un string.
d = True
e = None # Podria ser un print o un input que no tenga valor asignado.



### Completa aquí

print("La variable 'a' es de tipo:", type(a))# La primera es un enetero (int)
print("La variable 'b' es de tipo:", type(b))# La segunda es un floante (float)
print("La variable 'c' es de tipo:", type(c))# La tercera es una cadena de texto (str)
print("La variable 'd' es de tipo:", type(d))# La cuarta es un booleano (bool)
print("La variable 'e' es de tipo:", type(e))# La quinta es un nulo (NoneType)

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
entero = int("12345")  # Convierte la cadena a entero
type(entero)  # Verifica el tipo de dato
flotante = float(entero)  # Convierte el entero a flotante
print(f"El entero es: {entero}, y su tipo es: {type(entero)}, el flotante es: {flotante}, y su tipo es: {type(flotante)}")
print("3.99 al convertirlo a un entero pierde su apartado decimal dejandonos 3, aunque este apartado lo deje más cerca del 4 que del 3:", int(3.99), type(int(3.99)))  # Convierte el flotante a entero, truncando la parte decimal

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")


### Completa aquí
nombre = "Pepe"
edad = 21
altura = 1.70
print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura} metros.")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# 1. Como creo una viaralbe sin asignar una variable?
# pi = 3.14159  # Asignamos el valor de PI a una variable
pi = input("Escribe el número Pi primeros 5 decimales:") # Tecnicamente podriamos decir que el usuario es el que esta asignando la variable.
round(float(pi))// 2  # Redondeamos el número y hacemos la división entera entre el número y 2
print("El número", pi, "redondeado usando round() es:", round(float(pi)), "y la división entera entre el número y 2 es:", round(float(pi)) // 2)
# Otra forma
# Redondeamos directamente el valor de pi sin almacenarlo en una variable
resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)
# "Hacer la división entera se puede interpretar como la divison entera // o la division entera que es int(/)., ahora que lo pienso otra forma de printear el resultado sin usar una variable, auqnue ahí te pides qeu si crees una seria solo mostrarlo con un print