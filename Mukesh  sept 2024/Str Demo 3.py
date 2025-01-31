#"Python" in sentences
myLang="I know {}".format("Java")
print(myLang)

name="Python"
myLang="I know {}".format(name)
print(myLang)


myLang="I know {} {} {}".format("Java","C++","Selenium")
print(myLang)

myLang="I know {2} {0} {1}".format("Java","C++","Selenium")
print(myLang)

myLang="I know {p} {s} {j}".format(j="Java",p="Python",s="Selenium")
print(myLang)

print("****************** adding string************************")
name="Afshan"
prog="Python"
print(f"My name is {name} and I know {prog}")

print("***************** slicing and indexing*****************")
#indexing 2 types positive and negative
sent="Python is very easy"
print(sent[3])
print(sent[8])
print(sent[9])
#for last indexing use negative numbers
print(sent[-4])
print(sent[-6])
print(sent[-11])

#for slicing the sentences
name="Mynameismukesh"
print(name[2:6])
print(name[0:2])
print(name[6:8])

name="Pythonisveryeasy"
print(name[8:12])
print(name[6:8])
print(name[::2])#step skip




