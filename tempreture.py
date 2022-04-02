def tempreture (Tempreture):
    assert(Tempreture >= 0) , "Colder than absolute zero!"
    return ((Tempreture-273*1.8)+32)

    print(tempreture)(273)
    print (int (tempreture(505.78)))
    print (tempreture (-5))

