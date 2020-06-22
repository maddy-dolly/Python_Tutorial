dic1 = {0:"item", 1:"item1"}

#print("print using normsl dict",dic1)

dict2 = {i:f"Item {i}" for i in range(100) if i%100}
#print("print using comprhension dict",dict2)

names = ['Bruce', 'Clork', 'maddy', 'Login', 'Wadd']
hero = ['Batman', 'Superman', 'Spiderman', 'Susantsingh', 'Deadpool']
my_dict={names:hero for names, hero in zip(names,hero) if names!='peter'}

print(my_dict)