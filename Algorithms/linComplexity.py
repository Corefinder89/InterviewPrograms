# Time complexity of linear search is O(n) as the execution time increases exponentially
# with the number of inputs

import random
import time

class Linearsearchcomplexity():
    def __init__(self, arraySize):
        self.arraySize = arraySize

    def lin_search(self, search_element):
        startTime = int(round(time.time()*1000))
        listSearch = self.generateNumbers()
        search_at = 0 #Starting search position
        search_res = False #Default search result
        pos = 0 #Initial position
        while search_at < len(listSearch) and search_res is False:
            if listSearch[search_at] == search_element:
                search_res = pos
                print("Element found at "+str(search_res))
                break
            else:
                search_at = search_at + 1
            pos = pos + 1
        if search_res is False:
            print("Element not found")
        endTime = int(round(time.time()*1000))
        lapsedTime = endTime - startTime
        print("The lapsed time is "+str(lapsedTime)+" milliseconds")

    def generateNumbers(self):
        try:
            listVal = random.sample(range(0,self.arraySize),self.arraySize)
            return listVal
        except ValueError:
            print("Sample size exceeded population size")
        
obj = Linearsearchcomplexity(100000)
obj.lin_search(10000)
obj = Linearsearchcomplexity(200000)
obj.lin_search(20000)
obj = Linearsearchcomplexity(300000)
obj.lin_search(30000)
obj = Linearsearchcomplexity(400000)
obj.lin_search(40000)
obj = Linearsearchcomplexity(500000)
obj.lin_search(50000)