# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso.

print("\nrange():")
# nums = range(5) # Range sino especificamos empeiza desde 0 y va a al número indicado. Lo crea bajo demanda.
# # range(empeiza, hasta, paso)
# print(type(nums)) # <class 'range'>
# print(nums) # range(0, 5)

# # for num in range(5):
# #     print(num) # Imprime del 0 al 4

# for num in range(5,10):
#     print(num) # Imprime del 5 al 9

# for num in range(0, 10, 2):
#     print(num) # Imprime del 0 al 8 de a dos. Es decir, los pares.

# # Sirve para números nega
# # Cuentas atras tambien

# for num in range(10, 0, 1):
#     print(num) # Imprime del 10 al 1 de a uno. Es decir, los números en orden descendente.

# for num in range(-5,0):
#     print(num)

# Crear una lista con range()
lista_de_numeros = list(range(1, 11))  # Crea una lista del 1 al 10
print("Lista de números del 1 al 10:", lista_de_numeros)
# La funcion list acepta un iterable, por lo que range() puede ser convertido a una lista.

# Si quiero hace algo 5 veces
for _ in range(5): # El guión bajo indica que no vamos a usar la varibale. Es una convención.
    print("Hola")
