list1=[ 10, 30, 50, 60]
print(list1)
print(type(list1))
print(len(list1))

list2=[ "afshan", 26, 34, 56, 67, True]
print(list2)
print(len(list2))

list3=list1+ list2
print(list3)
print(len(list3))

#indexing in python
list4=[ 12, 89, 34.45, 56, 56, 78, 89]
print(list4[3])
print(list4[-2])
print(list4.count(56))
print(list4.count(200))# just gives 0 if number is not present

print('----------slicing the list-------------------')
print(list4[0: 4])
print(list4[2:6])
print(list4[-5 :-2])# negative indexing not working


print("************************--'append'-----*****************************")
list4.append(889)
#print(list4)

list4.append("Mukesh")
list4.append("sereen")
print(list4)











