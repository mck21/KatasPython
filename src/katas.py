# NOTA: Este es un conjunto de ejercicios para mejorar la lógica de programación y masterizar el uso de Python. Se ha intentado usar lo máximo posible programación declarativa, lo pidiera o no el enunciado. Los ejercicios que requieren input del usuario se deben ejecutar en un terminal, ya que no funciona del todo bien en jupyter notebook.

from functools import reduce

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    diccionario = {}
    for letra in texto:
        if letra != " ":
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    return diccionario

print(frecuencia_letras("hola mundo"))  # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def lista_dobles(numeros):
    return list(map(lambda x: x * 2, numeros))

print(lista_dobles([1, 2, 3, 4, 5]))  # [2, 4, 6, 8, 10]

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def contiene(palabras, palabra_objetivo):
    return [p for p in palabras if palabra_objetivo in p]     

print(contiene(["hola", "mundo", "hola mundo", "mundo hola"], "hola"))  # ['hola', 'hola mundo', 'mundo hola']

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x-y, lista1, lista2))

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
    return list(map(lambda x: f"{x[0]}-{x[1]}", tuplas))

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
    return list(filter(lambda m: m not in prohibidas, mascotas))    

print(mascotas_legales(["Perro", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"])) # ['Perro', 'Gato']

#  10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def promedio(numeros):
    try:
        if len(numeros) == 0:
            raise Exception("La lista proporcionada está vacía") 
        return sum(numeros) / len(numeros)
    except Exception as e:
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

input_edad()  #Introduce un número: hola // Error: invalid literal for int() with base 10: 'hola'

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

frase = "tengo 369 cafes"

print(list(map(len, frase.split())))  # [5, 3, 5]

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

caracteres = "python"

print(list(map(lambda c: (c.upper(), c.lower()), set(caracteres))))  # [('Y', 'y'), ('O', 'o'), ('T', 't'), ('H', 'h'), ('N', 'n'), ('P', 'p')]

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

palabras = ["hola", "mundo", "python", "programacion"]

print(list(filter(lambda p: p.startswith("p"), palabras)))  # ['python', 'programacion']

# 15. Crea una función lambda que  sume 3 a cada número de una lista dada.

numeros = [2, 5, 7]

print(list(map(lambda x: x + 3, numeros)))  # [5, 8, 10]

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

frase = "hola soy Marcos Palomero y soy programador"

print(list(filter(lambda p: len(p) > 3, frase.split())))  # ['hola', 'Marcos', 'Palomero', 'programador']

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

numeros = [5, 7, 2]

print(int(reduce(lambda x, y: str(x) + str(y), numeros)))  # 572

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Marcos Palomero", "edad": 20, "calificacion": 99}, 
    {"nombre": "Ana García", "edad": 22, "calificacion": 95}, 
    {"nombre": "Luis Fernández", "edad": 19, "calificacion": 88}, 
    {"nombre": "Sofía López", "edad": 21, "calificacion": 70}, 
    {"nombre": "Carlos Martínez", "edad": 23, "calificacion": 85}, 
]

estudiantes_con_90_o_mas = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

print(estudiantes_con_90_o_mas)

# 19. Crea una función lambda que filtre los números impares de una lista dada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(lambda x: x % 2 != 0, numeros)))  # [1, 3, 5, 7, 9]

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista_mixta = [9, "hola", 21, "adios"]

print(list(filter(lambda x: type(x) == int, lista_mixta)))  # [9, 21]

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

print((lambda x: x ** 3)(9))  # 729

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() 

numeros = [4, 5, 1, 6]

print(reduce(lambda x, y: x + y, numeros))  # 16

# 23. Concatena una lista de palabras. Usa la función reduce() .

palabras = ["hola", "soy", "programador"]
print(reduce(lambda f, p: f"{f} {p}", palabras))  # hola soy programador

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() 

numeros = [82, 54, 21]

print(reduce(lambda x, y: x - y, numeros))  # 7

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

texto = "esternocleidomastoideo"

print(reduce(lambda cont, char: cont + len(char), texto.split(), 0))  # 22

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

print((lambda x, y: x % y)(22, 7))  # 1

# 27. Crea una función que calcule el promedio de una lista de números.

def promedio(numeros):
    if len(numeros) != 0:
        return sum(numeros) / len(numeros)
    else:
        return "La lista de números está vacía"

print(promedio([7, 8, 7])) # 7.333333333333333

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def buscar_primer_duplicado(lista):
    vistos = []
    return next((elemento for elemento in lista if elemento in vistos or vistos.append(elemento)), "No hay duplicados") # --> next(...) devuelve el PRIMER valor que genera el iterador, si no se genera nada, se devuelve el segundo argumento

print(buscar_primer_duplicado([1, 2, 3, 4])) # No hay duplicados
print(buscar_primer_duplicado(["berserk", "one piece", "kimetsu", "berserk"])) # berserk

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

def enmascarar(variable):
    texto = str(variable)
    resultado = '#' * max(len(texto) - 4, 0) + texto[-4:] 
    # --> 1) Pone tantos # como la longitud del texto -4 haya (asegurandose que no da valores negativos con max()), e.g si len(texto) es 6 -> ##
    # --> 2) Añade los ultimos 4 caracteres

    return resultado

print(enmascarar(7851658788)) # ######8788

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)   

print(anagramas("aloh", "hola")) # True
print(anagramas("hola", "adios")) # False

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def encontrar_nombre():
    try:
        lista_nombres = []

        while True:
            nombre = input("Introduce un nombre (o 'parar' para finalizar): ")
            if nombre.lower() == 'parar':
                break
            lista_nombres.append(nombre)

        encontrar = input("Nombre a buscar en la lista: ")

        if encontrar in lista_nombres:
            return f"'{encontrar}' ha sido encontrado"
        else:
            raise ValueError(f"'{encontrar}' no se encuentra en la lista.")
    except ValueError as e:
        return str(e)

print(encontrar_nombre())


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre_completo, empleados):
    if nombre_completo in empleados:
        return nombre_completo
    else:
        return "Esa persona no trabaja aquí"


empleados = ["Juan Pérez", "María Gómez", "Pedro Martínez"]

print(buscar_empleado("Ana López", empleados))   # Esa persona no trabaja aquí


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
print(list(map(lambda x, y: x + y, numeros1, numeros2)))  # [5, 7, 9]


# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    def __init__(self, tronco, ramas=None):
        if ramas is None:  # Asegurarse de que no se pase una lista mutable por defecto
            ramas = []
        self.tronco = tronco
        self.ramas = ramas
    
    def crecer_tronco(self, cantidad):
        self.tronco += cantidad
    
    def nueva_rama(self):
        self.ramas.append(1)  # Al agregar una nueva rama, su longitud inicial será 1
    
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]  # Aumenta la longitud de cada rama por 1
    
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            return "Posición inválida"
    
    def info_arbol(self):
        ramas_info = ", ".join(str(rama) for rama in self.ramas)
        return f"El árbol tiene un tronco de {self.tronco} metros y {len(self.ramas)} ramas de longitudes: {ramas_info}"

# Crear un árbol con un tronco de 1 metro
arbol = Arbol(1)

# Hacer crecer el tronco una unidad
arbol.crecer_tronco(1)

# Añadir una nueva rama
arbol.nueva_rama()

# Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# Quitar la rama de la posición 2
arbol.quitar_rama(2)

# Obtener la información sobre el árbol
print(arbol.info_arbol())  # El árbol tiene un tronco de 2 metros y 2 ramas de longitudes: 2, 1

# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            raise ValueError("No tienes suficiente saldo")
    
    def transferir_dinero(self, otro_usuario, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            otro_usuario.saldo += cantidad
        else:
            raise ValueError("No tienes suficiente saldo")
    
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Agregar 20 unidades de saldo a Bob
bob.agregar_dinero(20)

# Transferir 80 unidades de Bob a Alicia
bob.transferir_dinero(alicia, 80)

# Retirar 50 unidades de saldo a Alicia
alicia.retirar_dinero(50)

print(alicia.saldo) # 130
print(bob.saldo) # 20

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto . contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto

def contar_palabras(texto):
    diccionario = {}

    for palabra in texto.split():
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    if palabra in palabras:
        palabras.remove(palabra)
        return " ".join(palabras)
    else:
        return f"'{palabra}' no está en el texto"

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            return "Error: 'reemplazar' requiere 2 argumentos: la palabra original y la nueva palabra."
        original, nueva = args
        return reemplazar_palabras(texto, original, nueva)
    elif opcion == "eliminar":
        if len(args) != 1:
            return "Error: 'eliminar' requiere 1 argumento: la palabra a eliminar."
        palabra = args[0]
        return eliminar_palabra(texto, palabra)
    else:
        return "Error: Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'."
    
print(procesar_texto("hola hola hola me llamo Marcos", "contar")) # {'hola': 3, 'me': 1, 'llamo': 1, 'Marcos': 1}
print(procesar_texto("hola como estas?", "reemplazar", "hola", "adios")) # adios como estas?
print(procesar_texto("el barrio es tranquilo", "eliminar", "es")) # el barrio tranquilo
print(procesar_texto("hola como estas?", "opcion_invalida")) # Error: Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.
print(procesar_texto("hola como estas?", "reemplazar", "hola")) # Error: 'reemplazar' requiere 2 argumentos: la palabra original y la nueva palabra.
print(procesar_texto("hola como estas?", "eliminar", "hola", "adios")) # Error: 'eliminar' requiere 1 argumento: la palabra a eliminar.


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

from datetime import datetime

def momento_dia(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M").time()

        if 6 <= hora.hour <= 12:
            return "Es de día."
        elif 13 <= hora.hour <= 18:
            return "Es por la tarde."
        else:
            return "Es de noche."
    except ValueError:
        return "Formato inválido. Por favor, ingresa la hora en formato HH:MM."


hora_usuario = input("Por favor, ingresa la hora en formato HH:MM: ")
print(momento_dia(hora_usuario))  # Por favor, ingresa la hora en formato HH:MM: 15:00 // Es por la tarde.

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def calificacion_texto(calificacion):
    if 0 <= calificacion <= 69:
        return "Insuficiente"
    elif 70 <= calificacion <= 79:
        return "Bien"
    elif 80 <= calificacion <= 89:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "Calificación no válida"

calificacion = float(input("Introduce la calificación: "))
print(calificacion_texto(calificacion)) # Introduce la calificación: 96 -> Excelente

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return 3.1416 * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no válida"
    

print(calcular_area("rectangulo", (5, 3))) # 15
print(calcular_area("circulo", (4,))) # 50.2656
print(calcular_area("triangulo", (4, 3))) # 6.0

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.

precio = float(input("Introduce el precio del artículo: "))
cupon = input("¿Tienes un cupón de descuento? (sí/no): ")

if cupon == "sí" or cupon == "si":
    valor_cupon = float(input("Introduce el valor del cupón: "))
    if valor_cupon > 0:
        precio -= valor_cupon
        print(f"El precio final de la compra es: {precio}")
    else:
        print("El valor del cupón no es válido.")
elif cupon == "no":
    print(f"El precio final de la compra es: {precio}")
else:
    print("Respuesta no válida")

'''
Introduce el precio del artículo: 100
¿Tienes un cupón de descuento? (sí/no): sí
Introduce el valor del cupón: 20

--> El precio final de la compra es: 80.0
'''

