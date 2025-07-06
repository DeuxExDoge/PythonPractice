# 0.2 Tipos de datos en Python
# Entero
entero = 17
print('entero:', entero, '->', type(entero))
print('entero:', '10 es', type(10), '->','0 es', type(0), '->', '-5 es', type(-5), '->', '324987518394057348917513480957 es', type(324987518394057348917513480957))  

# Flotante
flotante = 3.1415
print('flotante:', flotante, '->', type(flotante))
print('flotante:', '3.14 es', type(3.14), '->', '0.0 es', type(0.0), '->', '-2.71828 es', type(-2.71828), '->', '1e3', type(1e3))  # Aunque sea 1.e3 = 1000 se entiende como 1000.0 lo que es flotante. La utilización del punto decimal o la notación científica (e) indica que es un número flotante.

# Complejos
print('complex:', '3+4j es', type(3+4j), '->', '0j es', type(0j), '->', '-2.5+3.5j es', type(-2.5+3.5j))  # Números complejos, con parte real e imaginaria
#, '->', 'i es', type(j) no cuenta como número complejo, "j" no esta definido, tendriamos que adjuntarle un valor para que sea un número complejo, por ejemplo: 1j o 0j.

# Cadena de texto (string)
cadena = "Hola, mundo"
print('cadena:', cadena, '->', type(cadena))
print('string o cadena:', 'Hola es', type("Hola"), '->', '"" es', type(""), '->', "'Python' es", type('Python'), '->',""" Multilinea es: """ ,type(""" Multilinea """))


# Booleano
booleano = False
print('booleano:', booleano, '->', type(booleano))
print('booleano:', 'True es', type(True), '->', 'False es', type(False), '->', 'bool(1) es', type(bool(1)), '->', 'bool(0) es', type(bool(0)), '->', '1<2 es', type(1 < 2), '->', '1>2 es', type(1 > 2), '->', '1==1 es', type(1 == 1), '->', '1!=2 es', type(1 != 2))
# True y False son valores booleanos, 1 se interpreta como True y 0 como False.
# Esto da error type(bool = -1) TypeError: type() takes 1 or 3 arguments

# Lista
lista = [1, 2, 3, 4]
print('lista:', lista, '->', type(lista))

# Tupla
tupla = (1, 2, 3, 4)
print('tupla:', tupla, '->', type(tupla))

# Diccionario
diccionario = {"nombre": "Ana", "edad": 25}
print('diccionario:', diccionario, '->', type(diccionario))

# Conjunto (set)
conjunto = {1, 2, 3, 4}
conjunto0 = {'A','B'}
print('conjunto:', conjunto, '->', type(conjunto))
print('conjunto:', conjunto0, '->', type(conjunto0))

# Valor nulo (NoneType)
nulo = None
print('nulo:', nulo, '->', type(nulo))
# Otra forma de valor nulo
x = print("Hello world")
print (type(x))
