ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

print("using normal list process",ls)

#using list comprhension

ls_c = [i for i in range(100) if i%3==0]
print("using list_comrhension",ls_c)

num =[1,2,3,4,5,6,7,8,9,10]
my_list = [n*n for n in num]
print(my_list)

my_list_1 = map(lambda n: n*n,num)
print(my_list_1)