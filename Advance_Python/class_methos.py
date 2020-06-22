class Mobile:
    fp = 'Yes' #class Variable
    @classmethod #decoratoe
    def show_model(cls, r): #class method
         cls.ram = r
         print(cls.fp, cls.ram) #accessimng class variable inside class

realme = Mobile()
#realme.show_model() ye use nahi karenge kyuki ager object k sath kam karna hai to class method ka use kyu kan hai
Mobile.show_model('4Gb')