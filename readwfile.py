
#open file
try:
fo = open("foo.txt" ,"r+")
except IOError:
    print("cannot open the file")
    else:
         str = fo.read(10)
        print("The read string is:",str)
        #check the current position
        position = fo.tell()
        print ("The current position is:",position)
        #reposition the counter to the first position
        position = fo.seek(0,0)
        str = fo.read(10)
        print ("again the string is:",str)
        fo.close()
