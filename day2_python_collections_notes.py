#tuple
mytuple = ('a','b','c','d')
#concatinate
mytuple_1 = ('a','b','c','d')
mytuple_2 = ('e','f')
mytuple_1+=mytuple_2

print(mytuple_1)

#repetation
mytuple_2 =('e','f') * 2
print(mytuple_2)

#set
my_set = {1,2,3,4,5}
print(my_set)

#union
myset_1 = {1,2,'c'}
myset_2 = {1,'b','c'}
print(myset_1|myset_2)

#intersection
myset_1 = {1,2,'c'}
myset_2 = {1,'b','c'}
print(myset_1&myset_2)

#difference
myset_1 = {1,2,'c'}
myset_2 = {1,'b','c'}
print(myset_1-myset_2)

#dictionary
myDict = {1:'John', 2:'Bobby', 3:'Alice'}
print(myDict)

#empty
myDict={}
print(myDict)

#pairing
myDict_1 = dict([(1,'apple'),(2,'ball')])
print(myDict_1)

#length
myDict_2 = {1:'word_1', 2:'word_2'}
myDict_2.keys()
print(myDict_2)

#values
myDict_3 = {1:'apple',2:'ball'}
myDict_3.values()
print(myDict_3)
