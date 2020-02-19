import timeit

import numpy

class BenchMarker(object):
    def _newRand_(self,amountToReturn, low, high,float =False):
        new = [0 for i in range(amountToReturn)]
        if float:
            for i in range(amountToReturn):
                new[i] =numpy.random.uniform(low, high)
        else:
            for i in range(amountToReturn):
                new[i] =numpy.random.randint(low,high)
        return new

    def _wrapper_(self,func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped


    def doTestsWith(self,func,float:bool=False):
        count = 0
        for i in range(self.executeConst):
            count+=1
            newRandom=self._newRand_(self.sizeOfTests, self.lowRange, self.highRange,float)
            print([newRandom[int(i)] for i in newRandom[:-6:-1]])
            wrapped = self._wrapper_(func, newRandom)
            nameOfTest = f"{func.__name__} list {count}"
            print(f" execute count: {self.executeConst} Fun: {func.__name__} list: list{count}")
            self.finalResult[nameOfTest] = timeit.timeit(wrapped, number=1)

    def printResults(self):
        str=f"""    execute const: {self.executeConst}
        size of tests {self.sizeOfTests }
        low range {self.lowRange}
        high range {self.highRange}
        """
        print(str)
        for k,v in self.finalResult.items():
            print(f"{k} = {v}")

    def __init__(self,executeConst:int,sizeOfTests,lowRange,highRange):
        self.finalResult = {}
        self.executeConst= executeConst
        self.sizeOfTests = sizeOfTests
        self.lowRange = lowRange
        self.highRange = highRange

