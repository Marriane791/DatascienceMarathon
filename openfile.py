fo = open ("foo.txt","wb")
print ("Name of the file:",fo.name)
print ("Closed or not:",fo.closed)
print ("Opening mode:",fo.mode)
fo.write("Python is a great language \n It also supports machine learning\n")
# to close an opened file 
fo.close ()