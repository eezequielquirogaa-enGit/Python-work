# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}")

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# --------------- Dejar que el usuario elija cuando salir
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
        
# --------------- Usar una bandera
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# --------------- Usar break para salir de un bucle
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# --------------- Usar continue en un bucle
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
    
# --------------- Usar un bucle while con listas y diccionarios

# --------------- Pasar elementos de una lista a otra

# Empieza con usuarios que hay que verificar,
# y una lista vacía para alojar a los usuarios confirmados. 
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# Verifica cada usuario hasta que ya no hay usuarios sin confirmar.
# Mueve a cada usuario verificado a la lista de usuarios confirmados.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}") 
#     confirmed_users.append(current_user)

# # Muestra todos los usuarios confirmados.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
    
# --------------- Eliminar todos los casos de valores específicos de una lista
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# --------------- Rellenar un diccionario con entrada del usuario

responses = {}
# Configura una bandera para indicar que la encuesta está activa.
polling_active = True

while polling_active:
    # Pide el nombre y la respuesta de la persona. 
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
    
    # Guarda la respuesta en el diccionario.
    responses[name] = response

    # Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# La encuesta está completa. Muestra los resultados.
print("\n--- Poll Results ---") 
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")