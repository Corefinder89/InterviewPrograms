# Classic example of using recursion in python

def factorial(n):
    if n == 0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

for i in range(1,11):
    print(factorial(i))
