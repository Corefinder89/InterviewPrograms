# Find the permutations of a string 

from itertools import permutations

def find_permutations(str_var):
    perms = [''.join(p) for p in permutations(str_var)]
    for i in perms:
        print(i)

find_permutations("stack")
