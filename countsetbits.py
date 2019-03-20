# Question: Give a method to count the number of 1s in a "n" (e.g. 32) bit number

def countsetbits():
    n = input("Enter integer: ")
    bitnami = '{0:b}'.format(n)
    print bitnami
    count = 0
    for i in bitnami:
        if i == '1':
            count = count + 1
    print count

countsetbits()
