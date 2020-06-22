my_list = ['roti','sabzi','chawal']
# if  loop is normally stop
for my in my_list:
    print(my)

else:
    print("This for loop ended properly")

#if  loop is not normaaly brake

for my in my_list:
    if my == "roti":
        break
else:
    print("print nahi hounga")    