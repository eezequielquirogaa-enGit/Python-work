# --------------------- Valores de retorno
# def get_formatted_name(first_name, last_name):
#     """Devuelve un nombre completo, con un formato elegante."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

 
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# --------------------- Argumentos opcionales
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Devuelve un nombre completo, con un formato adecuado.""" 
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# --------------------- Devolver un diccionario
# def build_person(first_name, last_name):
#     """Devuelve un diccionario con información sobre una persona."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     """Devuelve un diccionario de información sobre una persona."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# --------------------- Usar funciones con un bucle while
# def get_formatted_name(first_name, last_name):
#     """Devuelve un nombre completo, con un formato adecuado."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
    
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
    
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")
    
# --------------------- Pasar una lista
#pagina 232