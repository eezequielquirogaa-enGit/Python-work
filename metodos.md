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

SEGUIR PAGINA 94