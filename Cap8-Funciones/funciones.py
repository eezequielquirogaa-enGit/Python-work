# --------------------- Definir una función
# def greet_user():
#     """Muestra un simple saludo."""
#     print("Hello!")
# greet_user()

# --------------------- Pasar información a una función
# def greet_user(username):
#     """Muestra un simple saludo."""
#     print(f"Hello, {username.title()}!")
# greet_user('Ezekiel')

# --------------------- Argumentos posicionales
# def describe_pet(animal_type, pet_name):
#     """Muestra información sobre una mascota."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')

# --------------------- Múltiples llamadas a una función
# def describe_pet(animal_type, pet_name):
#     """Muestra información sobre una mascota."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# --------------------- Argumentos de palabra clave
# def describe_pet(animal_type, pet_name):
#     """Muestra información sobre una mascota."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# --------------------- Valores predeterminados
# def describe_pet(pet_name, animal_type='dog'):
#     """Muestra información sobre una mascota."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# # Un perro llamado Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # Un hámster llamado Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

