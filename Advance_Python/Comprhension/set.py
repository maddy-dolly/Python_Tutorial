nums = [1,2,3,1,1,4,3,4,5,6,7,8,9,4,83,5,8]

my_set = set()
for n in nums:
    my_set.add(n)
print("using normal set",my_set)   

my_set_1 = {n for n in nums}
print("using set_comprhension",my_set_1)