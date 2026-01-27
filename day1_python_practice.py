#variables
name = "deepak"
age = 24
PI = 3.14

isPrime = None
print(type(isPrime))

#sum of 2 mums
a = 5
b = 10

sum = a + b
print(sum)

#operators and types of operators
#arithematic
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#relational
a = 10
b = 5

print(a<b)
print(a>b)
print(5>8)

a = 10
b = 10

print(a==b)
print(a!=b)

#assignment
a = 10
a = a+5 #15

print(a)

a = 10
a-= 5  # a = a -5

print(a)

a = 10
a%= 5  # a = a%5

print(a)

#logical
var = False
print(not var)#true

var = False
print(not (5>8))#true

var = False

print((3>2)and(8>4))

var = False

print((3<2)or(8<4))#false

#type conversion
ans = 5 + 10.0

print(type(ans))

ans1 = int(5 + 10.0)#catsing
ans2 = 5 + 10.0#conversion
print(ans1,type(ans1))
print(ans2,type(ans2))

val = (int("123"))

print(type(val))

val = (bool(0))

print(val,type(val))#false

val = (bool(-10))

print(val,type(val))#true

#input
username= input("enter your name:")
print("Welcome",username)

#sum of 2 nums
a = int(input("enter value a:"))
b = int(input("enter value b:"))

sum = a+b
print(sum)

#Calculate avg of 2 nums
a = float(input("enter value a:"))
b = float(input("enter value b:"))

Avg = (a+b)/2
print("Avg of 2 nums is:",Avg)

