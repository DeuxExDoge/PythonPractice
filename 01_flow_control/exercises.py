###
# EJERCICIOS
###
import os # Libreria de modulos de sistema operativo, nos permite limpiar la consola.

os.system("cls")  # Limpia la consola en sistemas Unix/Linux. En Windows, usar "cls".
# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("Comparación de dos números")
var1=int(input("Ingrese un número "))
#var2=input #me sorprende que esto no funcione como otra instancia de input, me da un error de que no declare o no asigne un valor a la var2. TypeError: '>' not supported between instances of 'str' and 'builtin_function_or_method'
var2=int(input("Ingrese otro número "))
#print(type(var1), type(var2))  # Verifica el tipo de dato ingresado
if var1 > var2:
    print(f"El número {var1} es mayor que {var2}.")
elif var1 < var2:
    print(f"El número {var2} es mayor que {var1}.")
else:
    print(f"Los números {var1} y {var2} son iguales.")  


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\nCalculadora simple")
num1 = float(input("Ingrese el primer número: "))
operador = input(("Seleccione una operación: +, -, *, / "))
num2 = float(input("Ingrese el segundo número: "))


if operador == "+":
    print("Esto es igual a: ", num1 + num2)
elif operador == "-":
    print("Esto es igual a: ", num1 - num2)
elif operador == "*":
    print("Esto es igual a: ", num1 * num2)
elif operador == "/" and not num2  ==  0:
    print("Esto es igual a: ", num1 / num2)
else:
    print("Error en el ingreso de datos.")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("Analizador de año bisiesto")
año = int(input("Introduzca un año "))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0: # Creo que mientras sea divisible por 400 cuenta como un año bisiesto.
    print("Es un año bisiesto")
else:
    print("NO es un año bisiesto")
    
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
edad = int(input("Escriba su edad para la clasificación "))
if edad <= 2:
    print("Bebe")
elif edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolecente")
elif edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no valida.")