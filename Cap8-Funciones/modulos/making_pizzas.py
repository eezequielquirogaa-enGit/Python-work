# 1 - IMPORTAR UN MÓDULO COMPLETO

# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 2 - IMPORTAR UNA FUNCIÓN ESPECÍFICA

# from pizza import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 3 - USAR AS PARA DAR UN ALIAS A UNA FUNCIÓN

# from pizza import make_pizza as mp

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 4 - USAR AS PARA DAR UN ALIAS A UN MÓDULO

# import pizza as p

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5 - IMPORTAR TODAS LAS FUNCIONES DE UN MÓDULO
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


