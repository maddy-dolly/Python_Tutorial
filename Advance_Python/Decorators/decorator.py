def dec1(fun_1):
    def nowexe():
        print("executing now")
        fun_1()
        print("executing now")
    return nowexe

@dec1
def who_is_harry():
    print("harry is a good boy")
#who_is_harry = dec1(who_is_harry) iss line ki jgh @dec1 lekh dete hai
who_is_harry()            