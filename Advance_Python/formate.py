person = {'name':'Madhu Acharya', 'age':23}

setence = 'My name is ' +  person['name'] + ' and i am ' + str(person['age']) + ' year old'
setence_1 = 'My name is {0} and I am {1} year old.'.format(person['name'],person['age'])
setence_2 = 'My name is {0[name]} and I am {1[age]} year old.'.format(person,person)
setence_3 = 'My name is {0[name]} and I am {0[age]} year old.'.format(person)
print(setence_3)

#access attribute from the class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def my_fun(self):
        if self.age > 18:
            return True
        else:
            return False

p1 = Person('maddy',15)
print(p1.my_fun())
                
obj = Person('Jack','33')
setence_4 = 'My name is {0.name} and I am {0.age} year old.'.format(obj)

print(setence_4)