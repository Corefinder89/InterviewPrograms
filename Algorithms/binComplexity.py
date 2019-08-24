# Time complexity of Binary Search is O(log n) as because the number of iterations are carried over 
# binary intervals
# Derivation:
# At iteration 1 length of the array = n
# At iteration 2 length of the array = n/2
# At iteration 3 length of the array = (n/2)/2 = n/2^2
# So, At the end of iteration k the length of the array will be n/2^k
# After k divisions the length of the array becomes 1
# so, length of the array is n/2^k = 1
# n = 2^k
# log2n = log22^k
# log2n = klog22
# log2n = k
import time
import random
class Binarysearchcomplexity():
    def __init__(self, arraySize):
        self.arraySize = arraySize

    

    def generateNumbers(self):
        try:
            listVal = random.sample(range(0,self.arraySize),self.arraySize)
            return listVal
        except ValueError:
            print("Sample sixe exceeded population size")