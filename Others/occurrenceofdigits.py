# Question: Given two integer numbers n and d. The task is to find the number between 0 to n which contains the
# specific digit d

def isdigitpresent(x,d):
    while x > 0:
        if (x % 10 == d):
            break

        x = x / 10

    return x > 0

def printNumbers(n, d):
    for i in range(0, n+1):
        if (i == d or isdigitpresent(i,d)):
            print i

n = 47
d = 7

printNumbers(n,d)
