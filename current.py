import time;
localtime = time.localtime(time.time())
print ("Local current time is:",localtime)
localtime2 = time.asctime(time.localtime(time.time()))
print ("Local current time2 is:",localtime2)