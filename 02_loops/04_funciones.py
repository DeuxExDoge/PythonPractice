# 04 - Funciones
# Bloques de código reutilizqables y parametrizables para hacer tareas especficias.

'''
def nombree_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la función
    return valor_de_retorno # opcional

'''

# # Ejemplo de una función para imprimir algo en consola.
# def saludar():
#     print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#     print(f"¡Hola, {nombre}!")
# # Es parametrizable, podemos pasarle un nombre y nos saluda a esa persona.
# saludar_a("Juan")
# saludar_a("María")
# saludar_a("Pedro")
# # El parametro es lo que acepta la función.
# # El argumento es lo que le pasamos a la función cuando la llamamos.

# # Funciones con más parámetros
# def sumar(a, b,):
#     suma = a + b
#     return suma

# result = sumar (2,3)
# print(result)

# # Documentar las funcioens con docstring
# def restar(a,b):
#     """Reta dos números y devuelve el resutlado"""
#     return a - b

# print(restar.__doc__)
# help(restar)

# Parámetros por defecto
def multiplicar (a, b=2):
    return a * b

print(multiplicar(2,6))

#