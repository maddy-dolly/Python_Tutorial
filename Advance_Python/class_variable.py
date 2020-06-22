class Circle:
    pi = 3.14 #class variable
    def __init__(self,radius):
        self.radius = radius #instance variable
        
        
    def fun_1(self):
        #return 2*self.pi*self.radius
        #when use class varible
        return 2*Circle.pi*self.radius
        #ager varible ki value change karni hai function call k time to uss time self.varible k name ka use kar lenge.
obj_1 = Circle(5)            
print(obj_1.fun_1())


#another example of class_vaiable
class Laptop:
    discount = 10 #class variable
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.Laptop_name = brand + '' + model_name
    def apply_discount(self):
        off_pri = (self.discount/100) * self.price
        return self.price - off_pri

obj_2 = Laptop('hp','pavilion',62000 )  
print(obj_2.__dict__)
obj_2.discount = 100 # change the class variable value using object 
print(obj_2.discount)
print(obj_2.apply_discount())          