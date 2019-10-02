# Program to find unique elements in 

from functools import reduce

mylist = [1,1,2,2,4,5,6,7,8,9]

# Using lambda function
unique1 = reduce(lambda l, x: l.append(x) or l if x not in l else l, mylist, [])

# Using list comprehension
t = set()
unique2 = [x for x in mylist if x not in t and (t.add(x) or True)]

print(unique1)
print(unique2)
