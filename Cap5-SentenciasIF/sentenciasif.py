# --------------------------------------------------------------
# ---------------     SENTENCIAS IF SIMPLES      ---------------
# --------------------------------------------------------------

# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
        
# --------------- comprobación de igualdad
# car = 'Audi'
# print(car == 'audi')
# - False

# car = 'Audi'
# print(car.lower() == 'audi')
# - True

# --------------- comprobación de la desigualdad 
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# --------------- comprobación númericas
# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again")

# --------------- comprobación varias condiciones con AND
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)
# age_1 = 22
# print(age_0 >= 21 and age_1 >= 21)

# --------------- comprobación varias condiciones con OR
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)
# age_0 = 18
# print(age_0 >= 21 or age_1 >= 21)

# --------------- comprobar si un valor no está en una lista con NOT
# banned_users = ['andrew','carolina','david']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# --------------------------------------------------------------
# ---------------      SENTENCIAS IF - ELSE      ---------------
# --------------------------------------------------------------
# age = 17
# if age >= 18:
#     print("You are old enough to vote")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")
    
# --------------- Cadena if-elif-else
# - SI SOLO QUIERE QUE SE EJECUTE UN BLOQUE DE CÓDIGO

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is ${price}.")

# --------------- SERIES DE SENTENCIAS IF INDEPENDIENTES
# - SI SE QUIERE EJECUTAR MAS DE UN BLOQUE DE CÓDIGO

# requested_topping = ['mushrooms','extra cheese']
# if 'mushrooms' in requested_topping:
#     print("Adding mushrooms.")
# if 'peperoni' in requested_topping:
#     print("Adding peperoni.")
# if 'extra cheese' in requested_topping:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

# --------------- Utilizar sentencias if con Listas
# requested_toppings = ['mushrooms','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# --------------- Comprobar que una lista no está vacía
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# --------------- Usar múltiples listas
# available_toppings = ['mushrooms','olives','green peppers','peperoni','pineapple','extra cheese']
# requested_toppings = ['mushrooms','french fries','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making your pizza!")