# 01 funcionalida de print()
# Print funciona como una función para mostrar mensajes en la consola
# Puedes usar comillas simples o dobles para definir cadenas de texto
print("Hello world")
print('Funciona con una comilla simple o doble')
print('''También funciona con comillas triples''')  # Comillas triples para cadenas multilínea
print("""Y también con comillas triples dobles""")  # Comillas triples dobles
print (3*"Hola mundo ")  # Multiplicación de cadenas, imprime "Hola mundo" 3 veces

print("Podemos", "usar", "comas", "para", "separar", "argumentos")
# Puedes usar el operador '+' para concatenar cadenas
print("Podemos"+"usar" + "+" + "para" + "concatenar" + "cadenas")  # Concatenación de cadenas
print("Podemos" + " usar " + "el operador + " + "para concatenar")  # Concatenación de cadenas con espacios

# Puedes cambiar el separador entre los argumentos con el parámetro 'sep'
print("El", "separador", "es", "un", "guión", sep="-")  # Cambia el separador a un guion
print("Sin", "separador",  sep="")  # Sin separador, los une directamente

# Puedes cambiar el final de la línea con el parámetro 'end'
print("Python", end=" ")  # No termina con un salto de línea
print("es", end=" ")  # Continúa en la misma línea
print("genial")  # Termina con un salto de línea por defecto

#1. Desafío: Mezcla de tipos. ¿Qué pasa si mezclás cadenas de texto y números en print()?
print("La suma de 2 + 3 es:", 2 + 3)  # Mezcla de cadena y operación aritmética
print("El número", 42, 43, "es el significado de la vida")  # Mezcla de cadena y número
#print("El número" + 42 + " es el significado de la vida") #Esto causará un error porque no se puede concatenar cadena y número directamente
#TypeError: can only concatenate str (not "int") to str. No  funciona porque solo puede concatenar strings con strings y no otro tipo de dato.
# Para evitar el error, puedes convertir el número a cadena usando str()
print("El número " + str(42) + " es el significado de la vida")

#2. Investiga el parámetro sep con diferentes tipos de datos
print("Python", "es", "genial", sep=" | ")
print("Python", "es", "genial", sep=' \ ')  
# print("Python", "es", "genial", sep='\') # Esto causará un error de sintaxis porque la barra invertida no se puede usar como separador directamente, siempre necesita estar espaciada.
# El no separa con esapcio al \ genera un error de sintaxis SyntaxError: unterminated string literal (detected at line 31), se refiere que la cadena no está cerrada correctamente.
print("Python", "es", "genial", sep='\\')  # Usa doble barra invertida para escapar la barra invertida
print("Python", "es", "genial", sep='\n')  # Usa salto de línea como separador
print("Python", "es", "genial", sep=' 😊 ') # Usa un emoji como separador, le agregue unos espacios porque el tamaño del emoji es raro y se toca con las letras si estan juntos.

#3. Explora el parámetro end con diferentes tipos de datos
print("Comienza", end=" -->") # Cambia el final de la línea a una flecha
print("Termina aquí")
#print("Comienza", end=" | " "Termina", end=" --> " "Vuelve", end="<--")  # Esto genera un error de sintaxis porque utlizamos el end varias veces y no se puede repetir este argumento en la función.
# print("Python", "es", "genial", sep=' \ ') File"c:\Users\Usuario\Desktop\PythonPractice\hello_world.py", line 39 print("Comienza", end=" | " "Termina", end=" --> " "Vuelve", end="<--") SyntaxError: keyword argument repeated: end
print("Comienza", end=3*" --> ")  # Genera 3 flechas.
#print("Comienza", 3*end=" | ") # No funciona no es una sitexis válida. Forma correcta print("Comienza", end=3*" --> ") 
print("\nComienza", end=" \n" "Termina")  # Cambia el final de la línea a un salto de línea, seria lo mismo que usar print("Comienza") y print("Termina") en líneas separadas
print("\nComienza", "Termina" + " Vuelve", end=" <--\n")  #Prueba uso de la coma más el operador '+' para concatenar cadenas

# 4. Creatividad: Arma un separador visual
nombre = input("Bienvenido a la GRIETA DEL INVOCADOR. \nIngresa tu nombre: ")  # Solicita al usuario que ingrese su nombre, usamos variables e input para guardar la información y podemos ver como print funciona con variables.
print("", nombre, sep=" ~ ", end=" ~ ")  # Usa un separador visual con ~. Me gusta el uso de "" porque es una forma de usar un separador visual.
# end="" cancela el salto de línea al final del print, por lo que el siguiente print continuará en la misma línea. y eso ees molesto, para evitarlo se puede usar end="\n" o simplemente no usar el parámetro end.

# 5. Desafío interactivo: Tu propio menú
print("\n--- Menú Interactivo ---"), print("1. Matar", "2. Casarse", "3. C#$er", sep=" | ")  # Muestra un menú interactivo con opciones separadas por |

# 6. Escribe una línea de código que muestre "Hola", "Python", "Mundo", separados por un asterisco y termine con tres signos de exclamación en la misma línea.
print("Hola", "Python" + " * " " Mundo", sep=" * ", end=3*("!"))

#Escribe un mensaje en un archivo de texto llamado "salida.txt" usando print()
# Esto creará un archivo llamado "salida.txt" en el mismo directorio donde se ejecuta el script y escribirá el mensaje en él. Increible todas las maneras que podemos usar print.
print("Texto usando print", file=open("salida.txt", "w", encoding="utf-8"))
