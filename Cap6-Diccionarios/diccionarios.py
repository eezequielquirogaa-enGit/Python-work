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
#pagina 168