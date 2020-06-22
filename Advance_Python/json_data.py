import json

data = '{"Var1":"harry", "Var2":56}'

# 1-> loads function
print(data)
parsed = json.loads(data)
print("json_loads_data",parsed)
print("dumps_parse_data",json.dumps(parsed))
print("type_of_data",type(parsed))
data2 = {
    "animal":"cow", 
    "fridge":('roti','daal','chawal'),
    "cars":['bmw','audio','nano'],
    "isbas":False
    }
dumps = json.dumps(data2, sort_keys=True)
print("json data",dumps)
print("python dictionay",data2)
# this is not posible in that type of data that's why am use the json module 
#print(data["Var1"])

#json module(four main function)
#1 loads() -> that convert json data into dictonary
#2 dumps() -> this function convert python dictonary to json formate
#3 load() -> this function work for the file.
#4 dump() -> this function also work for the file.


