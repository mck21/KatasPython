# NOTA: Este es un conjunto de ejercicios para mejorar la lógica de programación y masterizar el uso de python. Se ha intentado usar lo máximo posible programación 
# declarativa, lo pidiera o no el enunciado.

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    diccionario = {}
    for letra in texto:
        if letra != " ":
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1

    return diccionario

print(frecuencia_letras("hola mundo")) # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def lista_dobles(numeros):
    return list(map(lambda x: x*2, numeros))


print(lista_dobles([1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10]

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def contiene(palabras, palabra_objetivo):
    lista = [p for p in palabras if palabra_objetivo in p]

    return lista

print(contiene(["hola", "mundo", "hola mundo", "mundo hola"], "hola")) # ['hola', 'hola mundo']

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    diferencia = list(map(lambda x, y: x-y, lista1, lista2))

    return diferencia

print(diferencia_listas([1, 4, 2], [1, 2, 3])) # [0, 2, -1]

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def media_y_estado(numeros, nota_aprobado = 5):
    media = sum(numeros) / len(numeros) if numeros else 0  #para evitar la división entre 0
    estado = 'aprobado' if media >= nota_aprobado else 'suspenso'
    resultado = (media, estado)

    return resultado

print(media_y_estado([5, 6, 7])) # (6.0, 'aprobado')

# 6. Escribe una función que calcule el factorial de un número de manera recursiva

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5)) # 120

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(tuplas):
    lista = list(map(lambda x: f"{x[0]}-{x[1]}", tuplas))

    return lista

print(tuplas_a_strings([(1, 2), (3, 4), (5, 6)])) # ['1-2', '3-4', '5-6']

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. 
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def division():
    try:
        num1 = float(input("Introduce un número: "))
        num2 = float(input("Introduce otro número: "))
        resultado = num1 / num2
        print(f"La división es: {resultado}")
    except ValueError:
        print("Debes introducir un número")
    except ZeroDivisionError:
        print("No puedes dividir entre 0")

division() # Introduce un número: 5 // Introduce otro número: 0 // No puedes dividir entre 0

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def mascotas_legales(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    list.filter(lambda m: m not in prohibidas, mascotas)

    return mascotas

print(mascotas_legales(["Perro", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"])) # ['Perro', 'Gato']

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class EmptyList(Exception):
    pass

def promedio(numeros):
    try:
        if len(numeros) == 0:
            raise EmptyList("La lista proporcionada está vacía") 
        return sum(numeros) / len(numeros)
    except EmptyList as e:
        return str(e)

print(promedio([])) # 'La lista proporcionada está vacía'

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado 
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def input_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        
        print(f"Tu edad es {edad}.")
    
    except ValueError as e:
        print(f"Error: {e}")

input_edad()  # Introduce un número: hola // Error: invalid literal for int() with base 10: 'hola'

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    return list(map(lambda x: len(x), frase.split()))

print(longitud_palabras("tengo 369 cafés")) # [5, 3, 5]


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas 
# .Usa la función map()

def lista_tuplas(caracteres):
    return list(map(lambda c: (c.upper(), c.lower()), set(caracteres)))

print(lista_tuplas("python")) # [('Y', 'y'), ('O', 'o'), ('T', 't'), ('H', 'h'), ('N', 'n'), ('P', 'p')]

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_que_empiezan_por_letra(palabras, inicial):
    return list(filter(lambda p: p.startswith(inicial), palabras))

print(palabras_que_empiezan_por_letra(["hola", "mundo", "python", "programacion"], "p")) # ['python', 'programacion']

# 15. Crea una función lambda que  sume 3 a cada número de una lista dada.

def sumar_3(numeros):
    return list(map(lambda x: x + 3, numeros))

print(sumar_3([2, 5, 7])) # [5, 8, 10]

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. 
# Usa la función filter()

def palabras_mas_largas_que_n(texto, n):
    return list(filter(lambda p: len(p) > n, texto.split()))

print(palabras_mas_largas_que_n("hola soy Marcos Palomero y soy programador", 3)) # ['hola', 'Marcos', 'Palomero', 'programador']

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). 
# Usa la función reduce()
from functools import reduce
def numero_desde_digitos(digitos):
     cadena = reduce(lambda x, y: str(x) + str(y), map(str, digitos)) # -> Concateno los digitos en un str para despues hacer el casting a int

     return int(cadena)

print(numero_desde_digitos([5, 7, 2])) # 572

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para 
# extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Marcos Palomero", "edad": 20, "calificacion": 99}, 
    {"nombre": "Ana García", "edad": 22, "calificacion": 95}, 
    {"nombre": "Luis Fernández", "edad": 19, "calificacion": 88}, 
    {"nombre": "Sofía López", "edad": 21, "calificacion": 70}, 
    {"nombre": "Carlos Martínez", "edad": 23, "calificacion": 85}, 
]

estudiantes_con_90_o_mas_nota = list(map(lambda estudiante: estudiante["nombre"], 
                                         filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)))

print(estudiantes_con_90_o_mas_nota) # ['Marcos Palomero', 'Ana Garc�a']

# 19. Crea una función lambda que filtre los números impares de una lista dada.

def impares(numeros):
    return list(filter(lambda x: x % 2 != 0, numeros))

print(impares([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [1, 3, 5, 7, 9]

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista):
    return list(filter(lambda x: type(x) == int, lista))

print(filtrar_enteros([9, "hola", 21, "adios"]))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo(numero):
    return (lambda x: x **3)(numero)

print(calcular_cubo(9)) # 729

