my_list = [0,1,2,3,4,5,6,7,8,9]
#          0,1,2,3,4,5,6,7,8,,9
#          -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
#list[start:end:step]
#step is use foe escaping the letter according to the step and bydefalut step is 1

print(my_list[0:5])
print(my_list[1:-2])
print(my_list[1:9])
print(my_list[1:])
print(my_list[:-1])
print(my_list[:])
print(my_list[2:-1:2])
print(my_list[2:-1:-1])
print(my_list[-1:2:-1])
print(my_list[-2:1:-2])
print(my_list[2:-1:-1])
print(my_list[::-1]) #all list value isin reverse order

#string slicing

str_1 = "http://facebook.com"

print(str_1)

#reverse str
print(str_1[::-1])

#get the top level domain
print(str_1[-4:])

#print the url without http
print(str_1[7:])