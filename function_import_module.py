# Import entire module
import function_pizza
function_pizza.make_pizza(16, 'pepperoni')
function_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Import entire module as alias
import function_pizza as pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# Import specific function from a module
from function_pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# Import specific function from a module as alias
from function_pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')



# Import all function from a module
from function_pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
