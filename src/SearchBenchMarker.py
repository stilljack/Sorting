import random
import timeit
import numpy


class SearchBenchMarker(object):

    def newRandList(self):
        list = []
        if self.float:
            for i in range(self.listTotal):
                list.append(numpy.random.uniform(self.rangeLow, self.rangeHigh))
        else:
            for i in range(self.listTotal):
                list.append(numpy.random.randint(self.rangeLow,self.rangeHigh))
        list.sort()

        return list

    def randRandToSearchFor(self,collection):
        size=len(collection)
        return random.randint(0,size)

    def makeTestForSearch(self, searchFunc, collection,countID):
        targetIndex = self.randRandToSearchFor(collection)
        mArgs =[collection, collection[targetIndex]]
        wrapped = self._wrapper_(searchFunc, *mArgs)
        strs = searchFunc.__name__ + str(countID)
        print(f"str{strs} targetid ={targetIndex} target ={collection[targetIndex]}")
        print(collection[0:5:1])
        self.finalResult[strs] = timeit.timeit(wrapped, number=1)

    def multiTests(self,searchFunc):
        list =self.newRandList()
        for i in range(self.numberTests):
            self.makeTestForSearch(searchFunc, list,i)

    def _wrapper_(self,func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    def printResults(self):
        floatStatus=""
        if self.float:
            floatStatus="floats"
        else:
            floatStatus="ints"
        str=f"""    tests executed per multi call: {self.numberTests}
        size of lists {self.listTotal }
        low range {self.rangeLow}
        high range {self.rangeHigh}
        type: {floatStatus}
        """
        print(str)
        for k,v in self.finalResult.items():
            print(f"{k} = {v}")

    def __init__(self, rangeLow, rangeHigh, listTotal, numberTests, float):
        self.rangeLow=rangeLow
        self.rangeHigh=rangeHigh
        self.listTotal=listTotal
        self.numberTests=numberTests
        self.float=float
        self.finalResult = {}
