class justCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

        counter = justCounter ()
        counter.count()
        counter.count()
        