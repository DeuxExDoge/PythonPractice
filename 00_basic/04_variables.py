# 04 - Variables
# Las variables sirven para guardas datos en memorioa.
# Python es un lenguaj de tipado dinámico y de tipado fuerte

# Asignar una viarble
my_name = "Juan"  # Asigna el valor "Juan" a la variable my_name
print(my_name)  # Imprime el valor de la variable my_name

age = 28
print(age)  # Imprime el valor de la variable age

age = 27
print(age)  # Imprime el nuevo valor de la variable age, que ahora es 27

#se puede cambiar en tiempo de ejecución el valor de una variable
# Tipado dinámico : El tipo de dato se determian en tiempo de ejecución, no tienes que declarlo explícitamente.
# Tipado fuerte: No puede realizar conversiones automáticas entre tipos de datos, debes hacerlo explícitamente.

name = "pedo"
print(type(name))  # Imprime el tipo de dato de la variable name, que es una cadena (str)

name = 27
print(type(name))  # Imprime el tipo de dato de la variable name, que ahora es un entero (int)

# Tipado estatico: El tipo de dato se determina en tiempo de compilación, debes declararlo explícitamente.
# print("10" + 2)
# Tipado debil: El tipo de dato se determina en tiempo de ejecución, no tienes que declarlo explícitamente.

# formated strings literal
# f-string o (literal de cadena de formato)
# Desde la versión 3.6
print(f"Hola {my_name}, tengo {age + 5} años")  # Imprime un mensaje formateado con el nombre y la edad. formeado correctamente para poder mostrarlo

# Forma no recomendad de asignar variables

name, age, city = "Juan", 28, "Madrid"  # Asigna múltiples valores a múltiples variables en una sola línea

# Convenciones de nombres de viarables snake_case
mi_nombre_de_varible = "ok"  # Utiliza snake_case para nombres de variables
nombre = "ok"
MiNombreDeVAriable = "ko" # PascalCase, no recomendado para variables
minombredevariable = "ko" ## Utiliza minúsculas y guiones bajos para nombres de variables

mi_nombre_de_variable_123 = "ok"  # Puedes usar números en los nombres de variables, pero no al principio

MI_CONSTANTE = 3.14 #UPPER_CASE -> consantes, no se recomienda cambiar su valor. esto no existe pero se puede hacer algo parecido

#nombres no válidos de variables
# 123123_variable ="ko" 
# mi-variable = "ko"  # No se pueden usar guiones en los nombres de variables
# mi variable = "ko"  # No se pueden usar espacios en los nombres de variables
# Type = "ko"  # No se pueden usar palabras reservadas como nombres de variables


# python no hace checkeo de los tipso pero podemos pedirle anuestro editor que lo haga.