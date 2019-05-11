# Types of Arguments in Python
Arguments are basically of two types in Python
* Formal Arguments
   The arguments which are parameters which are used to receive values from the outside function are called formal arguments.
* Actual Arguments
   The arguments which are actually passed as parameters during the function call are called actual arguments.

# Types of Actual Arguments in Python
Actual Arguments are of 4 kinds
* Default Arguments.
* Keyword Arguments.
* Positional Arguments.
* Variable Length Arguments.

## Default Arguments
    The parameters which are defined in function definition by default are called Default Arguments, for example
    `def items(name, price=100.00)`

## Keyword Arguments
    Keyword arguments are arguments that identify the parameters by their names. For example
    `def items(item='Sugar', price=50.75)`

## Positional Arguments
    Arguments which are passed to a function in correct positional order are called positional arguments. For example
    `def items(a, b, c)`

## Variable Length arguments
    Variable length arguments can be defined in two ways, for example
    * `def(farg, *args)`. Here `*args` represent variable length arguments. Here the variable arguments are stored in a tuple. For example `def(5, 10, 11, 12)`
    * `def(farg, *kwargs)`. Here `*kwargs` represent variable length arguments that can take any number of arguments in the form of key value pairs. These key value pairs gets mapped in the backend as dictionary. For example `def(5, rno=10)`.

# Local and Global Variable
Variables can be of two types `local variables` and `global variables`
Local variables are the ones whose scope is limited to within a method or function.

Global variables are the ones whose scope is global and the scope of a global variable is throughout the entire program. To use a global variable within a function just call the variable inside the function or method. If you have to override the global variable inside a method just use the keyword `global`.

# Anonymous functions
In python a function which does not have a name are called anonymous functions. Anonymous functions in python can be defined using the keyword `lambda`.
For example

`f = lambda x: x*x
 value = f(5)
 print value
`
## Using lamdas() with Filter
Filter is used when filtering out elements from a sequence depending upon the results of a function (Operational on specific elements in the list). Conditional function.
`filter(function, sequence)`
For example
` lst = [10,11,12,13,14,15]
  f = list(filter(lambda x: (x%2)==0, lst))
  print f
`

## Using lambdas() with Map
The map function is similar to filter(), but it acts on every element on the list (Iterated on every element of the list).
`map(function, sequence)`
For example
```
  lst = [1,2,3,4,5]
  f = list(map(lambda x: x*x), lst)
  print f
```

## Using lambdas with reduce
The reduce function reduces a sequence of elements into a single element value by processing the elements according to the function supplied, reduce(function, sequence). For example
```
import functools
 lst = [1,2,3,4,5]
 f = functools.reduce(lambda(x,y: x*y), lst)
 print f
```

## Function Decorators
A decorator is a function that accepts function as a parameter and returns a function. A function takes a result of a function, modifies the result and returns it. For example
```
  def decor(fun):
    def inner():
      value=fun()
      return value+2
    return inner

  @decor
  def num():
    return 10

  print(num())
```
## Function Generators
Generators are functions that returns a sequence of values. A generator function is an ordinary function but uses the 'yield' statement. For example
```
  def mygen(x,y):
    while x<=y:
      yield x
    x+=1

  g = mygen(5,10)

  for i in g:
    print(i, end='')
```
## The Special Variable `__name__`
When a program is executed in Python there is a special variable internally created by the name `__name__`. This variable stores information regarding whether the program is executed as an individual program or as a module. When the program is executed directly the python interpreter stores the value `__main__` into this variable. When the program is imported as a module into another program then Python stores the module name into this variable.
