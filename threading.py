import threading
import time
exitFlag = 0
#define a new subclass of the thread class
class Threading(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Threading.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting" + self.name)
        print_time(self.name,self.counter,5)
        print ("Exiting"+self.name)
    def print_time(threadName,delay,counter):
        while counter:
            if exitFlag:
                threadName.exit()
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter-=1
    #create new threads 
    thread1 = Threading(1,"Thread-1",1)
    thread2 = Threading(2,"Thread-2",2)
    #start new threads
    thread1.start()
    thread2.start()
    print("Exiting the main thread")        
