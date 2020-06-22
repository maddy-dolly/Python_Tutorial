dic_1 = {1:'value', 'key':2}

print("dic_1[1] =",dic_1[1])
print("dic_1['key'] =",dic_1['key'])
#print(type(dic_1))
#example of dict

my_dic = {"customer_name":'Madhu',"order_id":1234,"segment":"Machine Learning"}
print(my_dic["customer_name"])
print(my_dic["segment"])
print(my_dic["order_id"])

#change segment
my_dic["segment"] = "Data Science"
print(my_dic["segment"])

#add item
my_dic['rigion'] = "West"

#print length
print("length",len(my_dic))

#drop one value
my_dic.pop("rigion")

#my_dic.clear()
#del my_dic
print(my_dic)