class Parent :
    x = 100
    def __init__ (self):
        print ("calling the parent constructor")
        def parentMethod (self):
            print ("Calling the parent method",x,"times")
            def setAtrr(self,attr):
                Parent.x = attr
                def getAttr(self):
                    print("the parent attribute is:",Parent.x)
                    #defining achild class
                    class Child(Parent):
                        def __init__ (self):
                            print("this is the child constructor")
                            def childMethod (self):
                                print ("Calling the child method")
                                c = Child()
                                c.childMethod()
                                c.parentMethod()
                                c.setAttr(200)
                                c.getAttr()