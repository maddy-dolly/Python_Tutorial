course_1 = ['History', 'Math', 'Physics', 'Hindi']
#append new item in a list
course_1.append('Arts')
#insert new item i a list
course_1.insert(0,'English')
#extend list 2 in lis1
course_2 = ['Bhugol', 'Html']
course_1.extend(course_2)
#Indx find the index of  a item
index = course_1.index('Arts')
print(index)
#remove item from the list
course_1.remove('Html')
#sorting list
sorting = course_1.sort()
#recerse the list
course_1.reverse()
#change value in list
course_1[0] = 'google'
#copy of a list
course_3 = course_1.copy()
print("copy", course_3)
# remove list
del course_3


#access list value
print(course_1[2])
#access using slicing
print(course_1[0:3])
#add item in a list
print(course_2[-1])
print(len(course_1))
print(course_1)