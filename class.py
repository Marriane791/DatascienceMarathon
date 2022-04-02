class Employee:
    #the value below is shared among all instances of employee class
    empCount = 0

    def __init__(self,name,salary):#creates a new instance of the class
        self.name = name
        self.salary = salary
        #the shared class is acessed in other instances as below 
        Employee.empCount += 1
        #other methods in the class are deaclared as normal functions except the first aergument must be self
        def displayCount(self):
            print("Total Employee %d % Employee.empCount")

            def displayEmployee(self):
                print("Name : ",self.name, ",Salary: ",self.salary)
                #create the instance object
                emp1 = Employee("Zara",2000)
                emp2 = Employee("Manni",5000)
                #display content
                emp1.displayEmployee()
                emp2.displayEmployees()
                print("Total Employee %d" % Employee.empCount)
                hasattr(emp1,name)
                getattr(emp2,"name")
                setattr(emp2,"name","wakavinya")
                emp1.__dict__:   #dictionary containing the class namespace
                emp1.__doc__:    #class documentation string
                emp2.__module__: #module name in which he class is identified
                emp2.__bases__:  #empty tuple containing the base classes in the oder in which they occour



    
