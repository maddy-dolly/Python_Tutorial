#inding is not supportable
set_1 = {1,2,3,4,4,5,6,6,6,7,7}
list_1 = [9,9,10,20,30,50,80]

set_2 = set(list_1)
print(set_2)
#add item in set
set_1.add(100)

#update set
set_1.update(set_2)

#remove sets
set_1.remove(20)
set_1.discard(80)

#remove intial value
set_1.pop()

#clear set
#set_1.clear()

#del set_1

print(set_1)