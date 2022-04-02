def changename(mylist):
    "This changes a passed list into this function"
    mylist = [1,2,3,4,5];
    print ("Values inside the function",mylist);

    mylist = [10,20,30,40,50]
    changename(mylist);
    print("Values outside the function",mylist);