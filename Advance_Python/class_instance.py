class Person:
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = self.first_name  +  self.last_name + '@gmail.com'

    def fun_1(self):
        return self.email

obj_1 = Person('madhu','acharya','19')            
print(obj_1.fun_1())