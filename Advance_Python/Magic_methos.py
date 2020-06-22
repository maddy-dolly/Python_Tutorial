class Employee:
    def __init__(self,fname,lname,salary):
        self.f = fname
        self.l= lname
        self.s= salary

    def __add__(self,other):
       return self.s + other    

    def __str__(self):
       return 'Employee ({}, {}, {})'.format(self.s,self.l,self.f)

    def __repr__(self):
       return 'Employee ({} {} {})'.format(self.s,self.l,self.f)    

employee = Employee('Maddy','Acharya',20000)       
print(employee)
print(employee.__add__(20000))
