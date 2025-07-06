# 05 - Entrada de usuario (input()) - versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.

# print("Hola, ¿Cómo te llamas?")
# nombre = input()
# print(f"Hola {nombre}, ¿Cómo estás?")
# print("Hola,", nombre, "¿Cómo estás?")  # Otra forma de imprimir el mensaje

nombre = input("¿Cómo te llamas?\n")  # Solicita el nombre del usuario directamente en el prompt
print(f"Hola {nombre}, ¿Cómo estás?")  # Imprime un saludo personalizado

age = input("¿Cuántos años tienes?\n")  # Solicita la edad del usuario
print(type(age))  # Imprime el tipo de dato de la variable age, que será str (cadena de texto)
print(f"DEntro de 5 años tendrás {int(age) + 5} años")  # Calcula la edad dentro de 5 años y la imprime
# Toda la información que meta un input nuestro usuario es una cadena de texto, por eso es necesario la conversión.

print("Obtener múltiples vaolres a la vez")
country, city = input("¿En qué país y ciudad vives? (separados por coma)\n").split(",") # Por default split utiliza el espacio como separador, pero aquí especificamos la coma como separador
print(f"Vives en {city.strip()} {country.strip()}")