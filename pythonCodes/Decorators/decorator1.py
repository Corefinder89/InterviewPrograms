def null_decorator(func):
    def modify_string(name):
        actual_string = func(name)
        modified_string = actual_string.upper()+". WELCOME TO PYTHON"
        return modified_string
    return modify_string

@null_decorator
def greet(name):
    return name

a = greet("soumyajit")
print(a)
