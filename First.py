"""
print("Hello world")

print("My name is Vaishnavi")
print("My age is 21")
print("My name is Vaishnavi","My age is 21")

print(23)
print(23+35)

name = "Vaishnavi" #string
age = 23 #integer
price = 25.99 #float(with decimals)
print("My name is ",name)
print("My age is ",age)
print(price)
print(name,age,price)

name = "Vaishnavi"
age = 23 
price = 25.99 
print(type(name))
print(type(age))
print(type(price))

name1 = "vbu"
name2 = 'vbu'
name3 = '''vbu'''
print(name1)
print(name2)
print(name3)

age = 21
old = False
a = None
print(type(old))
print(type(a))

#sum,difference,product,quotient of 2 numbers
a = 5
b = 30
sum = a+b
diff = a-b
pro = a*b
quo = a/b
print(sum)
print(diff)
print(pro)
print(quo)

#Arithmetic opetators
a = 5
b = 2
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division (It always appears in float)
print(a%b) #Remainder
print(a**b) #Power

#Relational operators
a = 50
b = 20
print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b) #True
print(a<=b) #False
print(a<b) #False

#Assignment operators
num1 = 10
#num1 = num1 + 10 #10 + 10 => 20
num1 += 10 # Instead of num+10
print("Num :",num1)

num2 = 10
num2 -= 10 # Instead of num-10
print("Num :",num2)

num3 = 10
num3 *= 10 # Instead of num*10
print("Num :",num3)

num4 = 10
num4 /= 10 # Instead of num/10
print("Num :",num4)

num5 = 10
num5 %= 10 # Instead of num%10
print("Num :",num5)

num6 = 10
num6 **= 10 # Instead of num**10
print("Num :",num6)

#Logical operators
#not, gives the opposite value
print(not False)
print(not True)

a = 50
b = 30
print(not(a>b))
#and, both values should be true
val1 = True
val2 = True
print("And operator:",val1 and val2) 
#or, any one value should be true
num1 = True
num2 = False
print("Or operator:",num1 or num2)

#Type conversion
a = 2
b = 4.26
sum = a+b
print(sum)
print(type(sum)) #It directly converts to float as it is the superior value
# a ="2"
# b = 3
#sum = a+b #Which is error because string and integer cannot be added

#type casting
a = int("2")
b = 4.26
print(type(a))
print(a+b)
# type casting only works for valid for type that is it converted into

#User input
name = input("Enter your name: ")
print("Welcome ",name)
print(type(name))
age = int(input("Enter your age: "))
print("Your age is ",age)
print(type(age))
marks = float(input("Enter your marks: "))
print("Your marks is ",marks)
print(type(marks))

#WAP to input 2 numbers and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a+b
print("Sum = ",sum)

#WAP to input side of a square and print its area
a = float(input("Enter the side value of square: "))
area = a*a
print("Area = ",area)

#WAP to input 2 flaoting point numbers and print their average
a = float(input("First: "))
b = float(input("Second: "))
print("Average = ", (a+b)/2)

#WAP to input 2 integers, a and b. Print True if a is greater than or equall to b.if not False
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a>=b)
"""
