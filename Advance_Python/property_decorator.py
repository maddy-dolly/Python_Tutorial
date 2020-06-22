class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = self.fname + self.lname + '@gmail.com'
    @property
    def email(self):
        if self.fname== None or self.lname == None:
            return "Email is not set"
        else:    
           return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split('@') [0]
        self.fname= names.split(".") [0]
        self.lname= names.split(".") [1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
   
employee = Employee('Madhu','Acharya')  

employee.lname = 'vyas' 
print(employee.lname)
employee.email = 'maddy.acharya@gmail.com'
print(employee.fname)
print(employee.lname)
print(employee.email)
#when am not using property decorator than only print print(employee.email())

del employee.email

print(employee.email)
#print(employee.email = 'maddy@gmail.com') this is posible using setter decorator

