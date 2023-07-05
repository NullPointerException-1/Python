"""
A dieferencia de otros lenguajes, Python es un lenguaje de programación dinámicamente tipado, lo que significa que no es necesario declarar el tipo de una
variable explícitamente, ya que el intérprete de Python puede inferirlo automáticamente según el valor asignado a la variable. 

Tipos de datos en Python:

Enteros (int): Representan números enteros positivos o negativos, como 5, -10, 0, etc.

Reales (float): Representan números decimales, como 3.14, -2.5, 0.0, etc.

Cadenas de texto (str): Representan secuencias de caracteres, encerradas entre comillas simples ('') o dobles (""). Por ejemplo, "Hola mundo".

Booleanos (bool): Representan los valores de verdad True (verdadero) o False (falso), utilizados para realizar operaciones lógicas.

Listas (list): Son colecciones ordenadas y modificables de elementos, separados por comas y encerrados entre corchetes ([]). Por ejemplo, [1, 2, 3].

Tuplas (tuple): Son colecciones ordenadas e inmutables de elementos, separados por comas y encerrados entre paréntesis (()). Por ejemplo, (1, 2, 3).

Diccionarios (dict): Son colecciones de pares clave-valor, donde cada clave se asocia a un valor específico. Se definen utilizando llaves ({}) y separando cada par clave-valor con dos puntos (:). Por ejemplo, {"nombre": "Juan", "edad": 25}.

Conjuntos (set): Son colecciones no ordenadas y sin elementos duplicados. Se definen utilizando llaves ({}) o la función set(). Por ejemplo, {1, 2, 3}.

"""

# COMENTAR CÓDIGO EN PYTHON
# Esto es un comentario de una línea

"""
Esto es un comentario
de varias líneas, también sirve con comillas simples
"""


# Mostrar texto por consola
print("Hola mundo")

# Nombrar variables.
'''La estructura que tiene es la siguiente: 
nombre_variable = valor
'''
edad= 18

# OPERACIONES CON STRINGS

    # Concatenación de strings
cadena1 = "Hola"
cadena2 = "mundo"
concatenada = cadena1 + " " + cadena2  # Resultado: "Hola mundo"

    # Acceso a caracteres individuales
cadena = "Hola"
primer_caracter = cadena[0]  # Resultado: "H"

    # Longitud de una cadena
cadena = "Hola"
longitud = len(cadena)  # Resultado: 4

    # Búsqueda de subcadenas
cadena = "Hola mundo"
posicion = cadena.find("mundo")  # Resultado: 5

    # Reemplazo de subcadenas
cadena = "Hola mundo"
reemplazada = cadena.replace("mundo", "amigo")  # Resultado: "Hola amigo"

    # Conversión a mayúsculas o minúsculas
cadena = "Hola"
mayusculas = cadena.upper()  # Resultado: "HOLA"
minusculas = cadena.lower()  # Resultado: "hola"

    # Separación en base a un delimitador
cadena = "Hola,amigo"
separada = cadena.split(",")  # Resultado: ["Hola", "amigo"]

    # Eliminación de espacios en blanco
cadena = "   Hola   "
sin_espacios = cadena.strip()  # Resultado: "Hola"


# OPERACIONES CON NÚMEROS

num1 = 10
num2 = 5

suma = num1 + num2       # Resultado: 15
resta = num1 - num2      # Resultado: 5
multiplicacion = num1 * num2   # Resultado: 50
division = num1 / num2   # Resultado: 2.0 (resultado como float)
division_entera = num1 // num2   # Resultado: 2 (resultado como entero)
modulo = num1 % num2    # Resultado: 0 (resto de la división)
exponente = num1 ** num2    # Resultado: 100000 (10 elevado a la 5)

    # Comparaciones
num3 = 8
num4 = 12

igual = num1 == num2    # Resultado: False
diferente = num1 != num2   # Resultado: True
mayor = num3 > num4     # Resultado: False
menor_igual = num3 <= num4    # Resultado: True

    # Conversión de entero a string
num5 = 123
cadena = str(num5)      # Resultado: "123"

    # Obtener valor absoluto
num6 = -7
absoluto = abs(num6)    # Resultado: 7

    # Redondeo
num7 = 3.8
redondeo = round(num7)  # Resultado: 4


# OPERACIONES CON  TUPLAS

    # Creación de una tupla
tupla1 = (1, 2, 3)

    # Acceso a elementos individuales
elemento1 = tupla1[0]  # Resultado: 1
elemento2 = tupla1[1]  # Resultado: 2

    # Concatenación de tuplas
tupla2 = (4, 5)
tupla_concatenada = tupla1 + tupla2  # Resultado: (1, 2, 3, 4, 5)

    # Longitud de una tupla
longitud = len(tupla1)  # Resultado: 3

    # Verificación de existencia de un elemento en la tupla
existe = 2 in tupla1  # Resultado: True

    # Iteración sobre los elementos de la tupla
for elemento in tupla1:
    print(elemento)  # Imprime: 1, 2, 3

    # Desempaquetado de una tupla
a, b, c = tupla1
print(a, b, c)  # Imprime: 1, 2, 3

    # Conversión de una tupla a lista
lista = list(tupla1)  # Resultado: [1, 2, 3]

    # Conteo de elementos en una tupla
conteo = tupla1.count(2)  # Resultado: 1 (el elemento 2 aparece una vez en la tupla)

# OPERACIONES CON  LISTAS

    # Creación de una lista
lista1 = [1, 2, 3]

    # Acceso a elementos individuales
elemento1 = lista1[0]  # Resultado: 1
elemento2 = lista1[1]  # Resultado: 2

    # Modificación de elementos individuales
lista1[2] = 4
print(lista1)  # Imprime: [1, 2, 4]

    # Añadir elementos al final de la lista
lista1.append(5)
print(lista1)  # Imprime: [1, 2, 4, 5]

    # Eliminar elementos de la lista
lista1.remove(2)
print(lista1)  # Imprime: [1, 4, 5]

    # Longitud de una lista
longitud = len(lista1)  # Resultado: 3

    # Verificación de existencia de un elemento en la lista
existe = 4 in lista1  # Resultado: True

    # Iteración sobre los elementos de la lista
for elemento in lista1:
    print(elemento)  # Imprime: 1, 4, 5

    # Ordenar la lista de forma ascendente
lista1.sort()
print(lista1)  # Imprime: [1, 4, 5]

    # Reversión de la lista
lista1.reverse()
print(lista1)  # Imprime: [5, 4, 1]

    # Conversión de una lista a tupla
tupla = tuple(lista1)  # Resultado: (5, 4, 1)

    # Eliminar todos los elementos de la lista
lista1.clear()
print(lista1)  # Imprime: []


# OPERACIONES CON  DICCIONARIOS

    # Creación de un diccionario
diccionario1 = {"nombre": "Juan", "edad": 30, "ciudad": "Antananaribo"}

    # Acceso a elementos individuales por clave
nombre = diccionario1["nombre"]    # Resultado: "Juan"
edad = diccionario1["edad"]    # Resultado: 30

    # Modificación de un valor existente
diccionario1["edad"] = 31

    # Agregar un nuevo par clave-valor
diccionario1["ocupacion"] = "Ingeniero"

    # Eliminar un par clave-valor
del diccionario1["ciudad"]

    # Verificación de existencia de una clave en el diccionario
existe_nombre = "nombre" in diccionario1    # Resultado: True

    # Obtener todas las claves del diccionario
claves = diccionario1.keys()

    # Obtener todos los valores del diccionario
valores = diccionario1.values()

    # Iteración sobre las claves del diccionario
for clave in diccionario1:
    valor = diccionario1[clave]
    print(clave, valor)



# ESTRUCTURAS DE CONTROL

# Estructura if-else:
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Estructura if-elif-else:
num = 10
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Bucle for:
lista = [1, 2, 3, 4, 5]
for num in lista:
    print(num)

# Bucle while:
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Estructura break y continue:
for num in range(10):
    if num == 5:
        break  # Termina el bucle cuando num es igual a 5
    if num % 2 == 0:
        continue  # Salta a la siguiente iteración si num es par
    print(num)

# Estructura try-except:
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except:
    print("Ocurrió un error")
else:
    print("La operación se realizó correctamente")
finally:
    print("Finalizando programa")




