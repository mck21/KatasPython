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

frecuencia_letras("hola mundo") # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def lista_dobles(numeros):
    doble = list(map(lambda x: x*2, numeros))

    return doble

lista_dobles([1, 2, 3, 4, 5]) # [2, 4, 6, 8, 10]

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def contiene(palabras, palabra_objetivo):
    lista = [p for p in palabras if palabra_objetivo in p]

    return lista

contiene(["hola", "mundo", "hola mundo", "mundo hola"], "hola") # ['hola', 'hola mundo']

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    diferencia = list(map(lambda x, y: x-y, lista1, lista2))

    return diferencia

diferencia_listas([1, 4, 2], [1, 2, 3]) # [0, 2, -1]

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def media_y_estado(numeros, nota_aprobado = 5):
    media = sum(numeros) / len(numeros) if numeros else 0  #para evitar la división entre 0
    estado = 'aprobado' if media >= nota_aprobado else 'suspenso'
    resultado: (media, estado)

    return resultado

media_y_estado([5, 6, 7]) # (6.0, 'aprobado')

# 6. Escribe una función que calcule el factorial de un número de manera recursiva

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(5) # 120

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(tuplas):
    lista = list(map(lambda x: f"{x[0]}-{x[1]}", tuplas))

    return lista

tuplas_a_strings([(1, 2), (3, 4), (5, 6)]) # ['1-2', '3-4', '5-6']

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

