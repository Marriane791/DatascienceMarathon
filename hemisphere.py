print("in the northern hemisphere:")
month_integer = [1,2,3,4,5,6,7,8,9,10,10,11,12]
for month in month_integer:
    if month < 3:
        print("Month {} is in winter".format(month))
    elif month < 6:
        print ("Month {} is in spring".format(month))
    elif month < 9:
        print("Month {} is in Summer".format(month))
    elif month < 12:
        print("Month {} is in fall".format(month))
    else:
        print("Month {} is in Winter".format(month))