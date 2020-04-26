def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}()")
        print(f"with {args}, {kwargs}")

        original_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}()")
        print(f"returned {original_result!r}")

        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name} {line}'

a = say('Jane', 'Hello World')
print(a)
