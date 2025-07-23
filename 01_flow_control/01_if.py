# 01 - sentencias condicionales (if, else, elif)
# Permite ejecutar bloques de código solo si se cumnplen ciertas condiciones.

from os import system
if system("clear") != 0: system("cls")


print("Sentencia simple condicional (if) y (else):")
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")

print("\nSentencia condicional con else:")
# Si la condición no se cumple, se ejecuta el bloque de código dentro del else.
edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("\nSentencia condicional con elif:")
nota = 7.9
if nota >= 7.51:
    print("Promociona")
elif nota >= 5.51:
    print("Regulariza")
elif nota < 5.50:
    print("Final")
else:
    print("No esta calificado")

print("\n Condiciones múltiples:")
edad = 20
carnet_de_conducir = True
# JavaScript
# && -> and
# || -> or


if edad >= 18 and carnet_de_conducir:
    print("Puedes conducir.")
else:
    print("Policia")

# Un pueblo de Cuba
if edad >= 18 or carnet_de_conducir:
    print("Puedes conducir.")
else:
    print("Paga a la policía y te deja conducir")

es_fin_de_semana = True
# JavaScript -> !
if  not es_fin_de_semana:
    print("Es un día de semana, a trabajar.")
else:
    print("Es fin de semana, a descansar.")

