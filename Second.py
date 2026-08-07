'''
str1 = "This is a string.\n We are creating it in python"
str2 = "Vaish's"
print(len(str2))
str3 = """String"""
len1 = len(str3)
print(len1) 
final_str = str2+str3
print(final_str)

str = "Vaishnavi B U"
print(ch)

str = "Vaishnavi B U"
print(str[0:5])
print(str[5:len(str)])
print(str[5:])
print(str[:5])
print(str[-5:-1])

str = "I am studying engineering"
print(str.endswith("ing")) #returns true if string ends with the characters passed(substr), False if not
print(str.endswith("eng"))

str = "i am studying engineering"
print(str.capitalize()) #Writes first charater in capital letter 

str = "i am studying engineering"
print(str.replace("g","r")) # repalce all occurrences of old character with new character passed
print(str.replace("am"," "))

str = "i am studying engineering"
print(str.find("a")) #returns first index of the first occurence of the character passed
print(str.find("study"))

str = "i am studying engineering"
print(str.count("am")) #counts the number of occurences of the substring passed in the main string
print(str.count("i"))

# WAP to input users first name and print it's length
name = str(input("Enter your first name: ")) 
print(len(name))

# WAP to find the occurances of "$"" in a string
a = str("I have 10$, and can lend you 5$ and keep 5$ with me")
print(a.count("$"))


#Conditional statements
#if
age = 21
if(age >= 18):
    print("Can vote and apply for license")

#elif
light = "green"
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Move")
elif(light == "Yellow"):
    print("Slow")
print("End of code")

#else
light = "black"
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Move")
elif(light == "Yellow"):
    print("Slow")
else:
    print("Light is broken")
print ("end of the code")

#only if and else can also be used
age = 21
if(age >= 18):
    print("Can vote") #the space here before print statement is indentation(proper spacing)(used instead of curly braces{})
else:
    print("Cannot vote")
print("End")

#Grade students based on marks
a = int(input("Enter marks: "))
if(a>=90):
    print("Grade A")
elif(90>a>=80):
    print("Grade B")
elif(80>a>=70):
    print("Grade C")
elif(70>a>=0):
    print("Grade D")
else:
    print("Invalid Marks")
print("End")

#Nested statements
age = int(input("Enter age: "))
if(age>=18):
    if(age>=80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")

# Write a program to check if a number entered by user is odd or even
n = int(input("Enter a number: "))
if(n%2 == 0 ):
    print("Even number")
else:
    print("Odd number")

#WAP to find greatest of 3 numbers entered by the user
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
if(a>b and a>c):
    print("First is largest ",a)
elif(b>a and b>c):
    num = print("Seconf is largest ",b)
else:
    num = print("Third is largest ",c)

#WAP to print whether the number is multiple of 7 or not
n = int(input("Enter a number: "))
if(n%7 == 0 ):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")
'''

