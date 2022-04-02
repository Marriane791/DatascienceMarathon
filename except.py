try:
    fh = open("testfile","r")
    fh.write("This is the firsttest file with exceptions")
    finally:
        print("cannot find the file or read the data")
       