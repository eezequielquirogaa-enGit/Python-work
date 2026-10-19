Métodos para cadenas:

# print()
- mostrar por pantalla

# .title()
- cambia cada palabra a formato de título

# .upper() 
- cambia cada palabra a mayúsculas

# .lower() 
- cambia cada palabra a minúsculas

# \t 
- tabulación 

# \n
- añadir nueva linea en una cadena 

# .rstrip()
- eliminar espacios en blancos a la derecha

# .lstrip()  
- eliminar espacios en blancos a la izquierda

# .strip() 
- eliminar espacios en blancos ambos lados

# .removeprefix()
- eliminar prefijos, entre paréntesis prefijo a eliminar

# .removesuffix()
- eliminar extensión, entre paréntesis parámetro a eliminar

# type()
- descubrir tipo de dato

# import this
- El Zen de Python, por Tim Peters. (Breve compendio de principios para escribir un buen código en Python)

# listas[-1]
# listas[-2]
- acceder al último elemento de una lista con el indice -1
- acceder al penúltimo elemento de una lista con el indice -2

# listas[0] = nuevo_elemento
- modificar un elemento de lista indicando el indice

# .append()
- listas.append( nuevo_elemento )
- añadir un elemento al final de una lista

# .insert()
- listas.insert( indice , elemento )
- añadir un elemento nuevo a una lista en cualquier posición
- especificar el índice y su valor

# del
- del listas[0]
- eliminar un elemento de la lista conociendo la posición
- ya no se puede acceder al valor que se ha eliminado
- del diccionario['clave']
- eliminar un par de clave-valor del diccionario

# .pop()
- elimina el último elemento de la lista
- reutilizar elemento eliminado, almacenandolo previamente en una variable
- elemento_eliminado = listas.pop()

# .pop(0)
- sacar elementos de cualquier posición de una lista

# .remove()
- listas.remove('valor')
- eliminar un elemento por valor, si desconocemos su posición
- reutilizar elemento eliminado, almacenandolo previamente en una variable
- solo borra la primera aparición del valor especificado

# .sort()
- ordenar alfabéticamente una lista de manera permanente
- no se puede volver al orden original

# .sort(reverse=True)
- orden alfabético inverso una lista de manera permanente
- no se puede volver al orden original

# sorted(listas)
- ordenar alfabeticamente una lista temporalmente
- permite mostrar la lista en un orden concreto pero no afecta el orden real de la misma
- ejemplo: print(sorted(listas))

# sorted(listas, reverse=True)
- ordenar alfabeticamente inverso una lista temporalmente
- permite mostrar la lista en un orden inverso pero no afecta el orden real de la misma
- ejemplo: print(sorted(listas, reverse=True))

# .reverse()
- invertir el orden original de una lista
- el método cambia el orden de forma permanente
- se puede volver al orden original, aplicándolo de nuevo a la misma lista

# len()
- descubrir la longitud de una lista

# range()
- for value in range(1, 5)
- en bucle for, empieza a contar en el primer valor
- se detiene cuando llega al segundo valor proporcionado
- usando un solo argumento, la secuencia arranca en 0
- en listas, sirve para crear una lista de numeros en ese rango: list(range(1,5)). Salida: [1,2,3,4,5]
- range(2, 11, 2) el tercer argumento sirve como tamaño de pasos al generar números. Salida: [2,4,6,8,10]

# list()
- convertir a la salida una lista

# min()
- hallar el mínimo

# max()
- hallar el maximo

# sum()
- calcular la suma, de una lista por ejemplo.

# listas[:]
- copiar una lista. 
- lista_nueva = listas[:]

# La PEP (Python Enhancement Proposal, Propuesta de mejora en Python), recomienda:
- Sangrado: 4 espacios por nivel de sangrado
- Longitud de línea: estándar de 79 caracteres por línea
- Lineas en blanco: para agregar partes de su programa visualmente
- un espacio vacío entre operadores de comparación: if age > 4:
- Para mas recomendaciones: https://python.org/dev/peps/pep-0008/

# AND
- Palabra clave para combinar las dos pruebas condicionales
- si pasan las dos pruebas, la expresión se evaluará como 'True'
- si no supera una de las dos, o las dos, la expresión se evalua como 'False'

# OR
- Palabra clave para combinar las dos pruebas condicionales
- si pasa una o ambas pruebas, la expresión se evaluará como 'True'
- si no supera las dos pruebas, la expresión falla y se evalua como 'False'

# NOT
- palabra clave para comprobar si un valor no está, en una lista, por ejemplo: 'if user not in users'

# get()
- ERROR: Si cabe la posibilidad de que no exista la clave que busca, considere usar el método get()
- método para acceder a valores en un diccionario
- requiere una clave como primer argumento
- Opcional, como segundo argumento, podemos pasar valor que se devolverá si la clave no existe
- si dejamos fuera el segundo argumento en la llamada, y la clave no exite, python devolverá el valor None ("No existe ningún valor")

# .items()
- nombre del diccionario seguido del metodo items(), para escribir un bucle for 
- for key, value in diccionario.items():
- devuelve una secuencia de pares clave-valor

# .keys()
- pasar en bucle por las claves
- devuelve una secuencia de todas las claves

# .set()
- resultado: una lista sin elementos repetidos
- identifica elementos únicos de la colección y crea un conjunto con ellos
- conjuntos: variable = {'elemento1','elemento2', ... , 'elementoN'}
- Por ejemplo, conjunto usando llaves y separando los elementos con coma
- conjuntos y diccionarios ambos usan llaves, pero los conjuntos no pares de clave-valor.
- Los conjuntos no mantienen los elementos en un orden específico

# input()
- La funcion input() pausa el programa y espera a que el usuario introduzca un texto

# int()
- transforma a un valor numérico de tipo entero

# %
- operador módulo
- dividir un numero entre otro, devuelve el resto

# break
- sentencia break para interrumpir un bucle por completo sin ejecutar el resto del código

# continue
- en lugar de interrumpir un bucle por completo, usamos la sentencia continue
- para volver al principio del bucle sin ejecutar el resto del código

# Control-C
- Para cancelar un bucle infinito

# def
- La primera linea usa la palabra  clave 'def' 
- para informar a Python de que estamos definiendo una función

# return
- Poder procesar datos en la función y devolver un valor o conjunto de valores
- La sentencia 'return' recoge un valor dentro de una función y lo envia de vuelta a la linea que ha llamado a la función

