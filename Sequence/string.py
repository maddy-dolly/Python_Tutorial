str_1 ="Madhu Acharya"
str_2 ="Manisha Acharya"
str_1 = str_1.replace('Madhu', 'Monu Madhu')
#new_str1 = str_1.replace('Madhu', 'Monu')
#print(new_str1)
print(len(str_1))
print(str_2[0:4])
#for all method about str_1
print(dir(str_1))
print(str_1.count("Monu"))
print(str_1.find('Monu'))
concunate_1 = "Hello"
concunate_2 = "Maddy"
add_concunate_1_2 = concunate_1+ ',' +concunate_2
print(add_concunate_1_2)
#uper wala complicated hai to iski jgh hum place-holder use karte hai.
new_add_concunate_1_2 ='{} {}, Welcome!'.format(concunate_1,concunate_2)
print(new_add_concunate_1_2)
#but in python3 new concept f-string for formating string
#lower()
#upper()
#cont()
#find()
new_fstring_concunate_1_2 = f"{concunate_1},{concunate_2.lower()}.Welcome!"
print(new_fstring_concunate_1_2)