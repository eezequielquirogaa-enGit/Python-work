# --------------------------------------------------------------
# ---------------  DICCIONARIOS - Clave - Valor  ---------------
# --------------------------------------------------------------

# --------------- Acceder a los valores de un diccionario
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# --------------- Añadir nuevos pares clave-valor
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# --------------- Empezar con un diccionario vacío
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# --------------- Modificar valores en un diccionario
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
# # Mueve el alien hacia la derecha.
# # Determina cuanto se muev el alien basándose en su velocidad actual
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else: 
#     # Debe ser un alien rápido.
#     x_increment = 3
# # La nueva posición es la antigua más el incremento
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# --------------- Eliminar pares clave-valor
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# --------------- Un diccionario de objetos similares
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# --------------- get() para acceder a valores
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# --------------- Pasar en Bucle por un diccionario 
# --------------- Pasar en Bucle por todos los pares clave-valor
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# --------------- Pasar en Bucle por todas las claves
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# for name in favorite_languages.keys():
#     print(name.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# --------------- Pasar en Bucle por las claves de un diccionario en un orden particular    
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# for name in sorted(favorite_languages.keys()):
#     # lista con todas las claves del diccionario y la ordene antes de iniciar el bucle
#     print(f"{name.title()}, thank you for taking the poll.")
    
# --------------- Pasar en Bucle por todos los valores de un diccionario    
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# --------------- Lista sin repeticiones usando metodo set()    
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# --------------- ANIDACIÓN
# --------------- Lista de diccionarios
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# Lista vacia para guardar aliens
# aliens = []
# # Crear 30 aliens verdes
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # Muestra los 5 primeros aliens
# for alien in aliens[:5]:
#     print(alien)
# print(" ... ")
# # Muestra cuantos aliens se han creado
# print(f"Total number of aliens: {len(aliens)}")

# Lista vacia para guardar aliens
# aliens = []
# # Crear 30 aliens verdes
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# # Muestra los 5 primeros aliens
# for alien in aliens[:5]:
#     print(alien)
# print(" ... ")
# for alien in aliens[3:6]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
# # Muestra los 5 primeros aliens
# for alien in aliens[:15]:
#     print(alien)
# print(" ... ")

# --------------- Lista en un diccionario
# Guardar la información sobre una pizza que se está pidiendo
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms','extra cheese'],
#     }
# # Resume el pedido
# print(f"You ordered a {pizza['crust']} - crust pizza\nWith the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t" + topping)
    
# favorite_languages = {
#     'jen': ['python','rust'],
#     'sarah': ['c'],
#     'edward': ['rust','go'],
#     'phil': ['python','haskell'],
#     }
# for name, languages in sorted(favorite_languages.items()):
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# --------------- Un diccionario en un diccionario
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")