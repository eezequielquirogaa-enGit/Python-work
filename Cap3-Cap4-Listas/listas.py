# --------------- acceder a elementos de una lista
# bicycles = ['trek','cannondale','redline','specialized']
# # print(bicycles)

# # print(bicycles[0])
# # print(bicycles[0].title())
# # print(bicycles[-1])
# # print(bicycles[-2])

# message = f"My first bicycle was a {bicycles[0].title()}"
# print(message)

# --------------- modificar elementos de una lista
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

# --------------- añadir elementos a una lista
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)

# --------------- insertar elementos a una lista
# motorcycles = ['honda','yamaha','suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# --------------- eliminar definitivamente elementos de una lista
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)

# --------------- eliminar elementos de una lista, con método pop()
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# --------------- sacar elementos de cualquier posición de una lista, con método pop()
# motorcycles = ['honda','yamaha','suzuki']
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

# --------------- eliminar un elemento por valor, usando remove()
# motorcycles = ['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# motorcycles = ['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me .")

# --------------- Ordenar una lista alfabeticamente de manera permanente con método sort()
# cars = ['bmw','audi','toyota','subaru']
# print(cars)
# cars.sort()
# print(cars)

# --------------- Ordenar una lista alfabeticamente inverso de manera permanente con método sort() usando como argumento reverse=True
# cars = ['bmw','audi','toyota','subaru']
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# --------------- Ordenar alfabeticamente una lista temporalmente con método sorted()
# cars = ['bmw','audi','toyota','subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# --------------- Ordenar alfabeticamente inverso una lista temporalmente con método sorted(nombre_lista, reverse=True)
# cars = ['bmw','audi','toyota','subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars, reverse=True)) 
# print("\nHere is the original list again:")
# print(cars)

# --------------- Imprimir una lista en orden inverso con metodo .reverse()
# cars = ['bmw','audi','toyota','subaru']
# print(cars)
# cars.reverse()
# print(cars)

# --------------- Descubrir la longitud de una lista con función len()
# cars = ['bmw','audi','toyota','subaru']
# print(len(cars))

# --------------------------------------------------------------
# --------------- bucle for para imprimir listas ---------------
# --------------------------------------------------------------

# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(magician)
    
# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# --------------- Función range()
# for value in range(1, 5):
#     print(value)

# --------------- Usar range() para hacer una lista de numeros con método list()
# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)

# --------------- Estadisticas con lista de numeros
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# --------------- Listas por comprensión
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# treses = []
# for value in range(3, 30, 3):
#     treses.append(value)
# print(treses)

# treses = [value for value in range(3, 30, 3)]
# print(treses)

# cubos = []
# for value in range(1, 10):
#     cubos.append(value**3)
# print(cubos)

# cubos = [value**3 for value in range(1, 10)]
# print(cubos)

# --------------- Trabajar con parte de una lista. Trozo o Slice

# --------------- incluye los 3 primeros
# players = ['charles','martina','michael','florence','eli']
# print(players[0:3])

# --------------- comienza en indice 1 y termina en indice 4 sin incluirlo
# players = ['charles','martina','michael','florence','eli']
# print(players[1:4])

# --------------- sin un índice inicial, empieza por el comienzo
# players = ['charles','martina','michael','florence','eli']
# print(players[:4])

# --------------- omitir el segundo indice, devuelve todos entre el tercero y el ultimo
# players = ['charles','martina','michael','florence','eli']
# print(players[2:])

# --------------- imprime los 3 últimos
# players = ['charles','martina','michael','florence','eli']
# print(players[-3:])

# NOTA puede incluir un tercer valor entre los paréntesis, inidica cuantas veces tiene que saltar entre elementos en el rango especificado

# --------------- Pasar en bucle por un trozo
# players = ['charles','martina','michael','florence','eli']
# print("Here are the first three players on my team")
# for player in players[:3]:
#     print(player.title())
    
# --------------- Copiar una lista
# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# --------------- Copiar una lista, y agregar elemento separados
# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# ------------------------------------------------
# ----------- Tuplas (Lista inmutable) -----------
# - Listas de elementos que no se pueden alterar -

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# --------------- Tupla con un solo elemento
# my_t = (3,)

# --------------- Pasar un bucle por todos los valores de una tupla
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)
    
# --------------- Sobreescribir una tupla - reasignar una variable es válido
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
    
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)