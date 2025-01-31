#ffor adding quotes in quotes- \
from ctypes import pythonapi

programming="\"Python\""
print(programming)

#for adding space in string- \t
name="I knowPython"
print(name)
name="I know\tPython"
print(name)

#skipping into line- \n
name="I know Python"
print(name)

name="I know\nPython"
print(name)

name="I\t know\nPython"
print(name)


print(type(name))

# methods

#size or length
sent="I love Python"
print(len(sent))

# to find index(if lower case given like I--i it throws error substring error
print(sent.index('l'))
print(sent.index('t'))

# to replece P with J
print(sent.replace('P','J'))

# SPLIT method
print(sent.split('P'))
print(sent.split(" "))

# to convert to upper case and lower case
print(sent.upper())
print(sent.lower())

print("*************small case to title*********************************")
sent="i love python"
print(sent.title())

print(sent.islower())
print(sent.isupper())
print(sent.count('o'))


