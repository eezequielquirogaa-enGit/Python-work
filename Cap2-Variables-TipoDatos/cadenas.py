# name = "ada lovelace"

# # ------------------ método .title() cambia cada palabra a formato de título
# print(name.title()) 

# name = "Ada Lovelace"

# # ------------------ método .upper() para mayúsculas
# print(name.upper())
# # ------------------ método .lower() para minúsculas
# print(name.lower())

# ------------------ uso de variables en cadenas (pag55)
# first_name = "ezequiel"
# first_name = first_name.title()
# last_name = "quiroga"
# last_name = last_name.title()
# full_name = f"{first_name} {last_name}"
# print(full_name)

# first_name = "ezequiel"
# last_name = "quiroga"
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}!"
# print(message)

# # ------------------ para tabulación \t (pag57)
# print(f"\t{message}")

# # ------------------ para añadir nueva linea en una cadena \n
# print(f"\t{message}\n\tHow are you?")

# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# ------------------ método rstrip() para eliminar espacios en blancos a la derecha
lenguaje_favorito = "python "

# print(lenguaje_favorito.lstrip())

# # ------------------ método lstrip() para eliminar espacios en blancos a la izquierda
# lenguaje_favorito = " python"

# print(lenguaje_favorito.lstrip())

# # ------------------ método strip() para eliminar espacios en blancos ambos lados
# lenguaje_favorito = " python "

# print(lenguaje_favorito.lstrip())

# ------------------ método eliminar prefijos .removeprefix('https:// ')
# url = 'https://www.enlace.com'
# url_fix = url.removeprefix('https://')
# print(f"{url}\n{url_fix}")

# ------------------ método eliminar extensión de archivo .removesuffix()
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))

# ------------------ 