import random
import time
class BigONotations():
    def __init__(self, arraySize):
        self.arraySize = arraySize

    def lin_search(self):
        startTime = int(round(time.time()*1000))
        listSearch = self.generateNumbers()
        for i in listSearch:
            if (i==56789):
                break
        endTime = int(round(time.time()*1000))
        lapsedTime = endTime - startTime
        print("The lapsed time is "+str(lapsedTime)+" milliseconds")

    def generateNumbers(self):
        try:
            listVal = random.sample(range(0,self.arraySize),self.arraySize)
            return listVal
        except ValueError:
            print("Sample size exceeded population size")
        
obj = BigONotations(100000)
obj.lin_search()
obj = BigONotations(200000)
obj.lin_search()
obj = BigONotations(300000)
obj.lin_search()
obj = BigONotations(400000)
obj.lin_search()
obj = BigONotations(500000)
obj.lin_search()