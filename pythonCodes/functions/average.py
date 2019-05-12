def generator(x,y):
    while x<=y:
        yield x
        x+=1

g = generator(5,10)

def average():
    x = 0
    sum = 0
    for i in g:
        sum = sum + i
        x = x + 1
    average = sum / x
    print(average)

average()
