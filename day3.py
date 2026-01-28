#control flow statement
#for
fruits = ["apple","strawberry","cherry"]
for x in fruits:
    print(x)


#while
a = 1
while a < 3:
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
    a += 1


#break
a = 10
while a > 0:
    a -= 1
    if a == 5:
        break
    print(a)

#functions

#user defined-functions

def add(a,b):
   sum = (a+b)
   return sum

#pass by value func:
a = 10
def myfunc_1(b):
   print("The value of b is","b")
   b = 100
   print("The new value of b is","b")
   myfunc_1(a)


#pass by refernce:
c = [22,44,88]
def myfunc_2(d):
   print("value of d is","d")
   d[0]
   d[1]
   d[2]
   print("new value of d is","d")
   myfunc_2(c)  


#lambda func;
x = lambda a: a+100
print(x(a))

r = lambda x,y:(x*y)
print(r(12,4))

z =lambda x,y:(x*y)
print(z(22,44))

#power of lambda
def myfunc(n):
   return lambda a: (a*n)

doubleme = myfunc(2)
print(doubleme(12))

#file handling
f = open("deepak:/testfile.txt","x")

#read {Hello! Deepak welcome to GitHub}
f = open("deepak:/demofile.txt","r")
print(f.read())

#loop through file
f = open("deepak:/demofile.txt","r")
for x in f:
   print(x)

#delete
f.close
import os 
os.remove("deepk:/demofile.txt")



      

