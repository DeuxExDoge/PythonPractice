# 02 - Booleanos
# Valores lógicos : True (verdadero) y False (falso).
# Fundamentos para el cotnrol de flujo y la lógica en programación.

# Los booleanos representan dos estados: verdadero (True) y falso (False).
import os # Libreria de modulos de sistema operativo, nos permite limpiar la consola.

os.system("cls")  # Limpia la consola en sistemas Unix/Linux. En Windows, usar "cls".

print("\nValores booleanos básicos:")
verdadero = True
falso = False

# Operadores de comparación: devuelven un valor booleano.
print("5 > 3:", 5 > 3)  # True
print("5 < 3:", 5 < 3)  # False
print("5 == 5:", 5 == 5)  # True (igualdad)
print("5 != 3:", 5 != 3)  # True (desigualdad)
print("5 >= 5:", 5 >= 5)  # True (mayor o igual)
print("5 <= 3:", 5 <= 3)  # False (menor o igual)


print("Comparación de cadenas:")
print("manzana < pera:", "manzana" < "pera")  # True (comparación lexicográfica)
print("manzana == Manzana:", "manzana" == "Manzana")  # False (diferencia de mayúsculas y minúsculas

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")

# NAND
print("\nnand:")
print("A     B     A nand B")
print("True  True  ", not (True and True))
print("True  False ", not (True and False))
print("False True  ", not (False and True))
print("False False ", not (False and False))

# AND
print("\nand:")
print("A     B     A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

# OR
print("\nor:")
print("A     B     A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

# NOT
print("\nnot:")
print("A      not A")
print("True   ", not True)
print("False  ", not False)

# Utilización de números como expresiones booleanas:
print("\nNúmeros como expresiones booleanas:")
numero = 5
if numero:
    print("El número es verdadero (no es cero).")

numero = 0
if not numero:
    print("El número es falso (es cero).")

# Utilización de strings como expresiones booleanas:
print("\nCadenas como expresiones booleanas:")
cadena = "Hola"
if cadena:
    print("La cadena es verdadera (no está vacía).")

cadena = ""
if not cadena:
    print("La cadena es falsa (está vacía).")

numero = 3 # Asignación de un número a la variable 'numero'
es_el_tres = numero == 3  # Comparación para verificar si 'numero' es igual a 3
if es_el_tres:
    print("El número es 3.")

print("\nLa condición ternaria:")
# Es una fomra concisa de un if-else.
# [Código si cumple la condición] if [condición] else [Código si no cumple la condición]
edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)