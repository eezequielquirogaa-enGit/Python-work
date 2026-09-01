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

