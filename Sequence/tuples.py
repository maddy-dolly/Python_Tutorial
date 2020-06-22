fruits_1 = ('graps', 'mango', 'banana','mango')
fruits_2 = ('guwawa', 'pinapple')
#inding to find value of the index
fruits_1_index = fruits_1.index('mango')
print(fruits_1_index)

#slicing
print(fruits_1[0:2])

#concatanation
print(fruits_1+fruits_2)

#repetation
#print(fruits_2 *)

#conut tuple repeted item
print(fruits_1.count('mango'))
#touple index(ye mango 2 bar hai but y phle wale ka index print karega)
print(fruits_1.index('mango'))

#del tuple
del fruits_2
#print(fruits_2)

print(fruits_1)