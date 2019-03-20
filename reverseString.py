# Question: Given an array of characters which form a sentence of words. Give an efficient algorithm to reverse the order of words
# (not characters) in it.
def reverse_String():
    string = "I like programming in python"
    s = string.split(' ')

    print " ".join(s[::-1])

reverse_String()
