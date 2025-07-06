# 03 - casting de types
# Transformar un tipo de dato a otro
# En Python, puedes convertir un tipo de dato a otro utilizando funciones de conversión como `int()`, `float()`, `str()`, etc.

print("Conversión de tipos en Python")
print("Entero a Flotante:", type(float(10)))  # Convierte un entero a flotante y te dice que tipo es.
print("Flotante a Entero:", type(int(3.14)))  # Convierte un flotante a entero y te dice que tipo es.
print("Suma de entero + int(string):", 2 + int("10") ) # Convierte una cadena a entero y suma 2.
print("Suma de string + str(int):", "2" + str(10))  # Convierte un entero a cadena y concatena con "2". Resultdo 210.
print("Cambio de float a int:", int(3.14))  # Convierte un flotante a entero, truncando la parte decimal.
# se pierde precisión al convertir de flotante a entero, por ejemplo, 3.14 se convierte en 3.
# Un caso que estoy pensando es imaginemos que tenemos unos parrafos donde queremos sacar información de números. Entonces podriamos utilizar la función find y lo que encuentre lo cambie a formato int o que ya lo genere de esa forma o algo así.
# Cadena de texto a float
print("Cambio de string a float:", type(float("3.14")))  # Convierte una cadena que representa un número decimal a flotante.
# Tansfoormación de booleano
print(bool(1), bool(-1), bool(0))  # Convierte enteros a booleano: 1 y -1 son True, 0 es False.

print(bool(""), bool(" "), bool("False"))  # Convierte cadenas a booleano: cadena vacía es False, cadena con espacio es True, cadena con texto es True.
#pirnt(int("hola mundo")) Da error porque "hola mundo" no se puede convertir a entero.

print(round(3.5), round(2.5))#  # Redondea números flotantes: 3.5 se redondea a 4, 2.5 se redondea a 2. Redondea al par más cercano.
