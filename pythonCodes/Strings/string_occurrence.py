# Count the number of occurrences of a character within a string 

from collections import Counter

def occurrence(str_var):
    count = Counter(str_var)
    print ("Count of occurrences of characters within a string: "+str(count))

occurrence("Geeks for Geeks")
