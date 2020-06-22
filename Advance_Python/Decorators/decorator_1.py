def function_1(function_2):
    def inner():
        a= function_2()
        add = a + 5
        return add
    return inner
    
@function_1
def function_2():
    return 10
print(function_2())    