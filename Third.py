'''#Lists
#marks1 = 94.4
#marks2 = 87.5
#marks3 = 95.2
#marks4 = 66.4
#marks5 = 45.1
# all the above valus could be written in one single variable using lists
marks = [94.4, 87.5, 95.2, 66.4, 45.1] #this is called a list in python
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks))

student = ["Vaishnavi",21,"Bengaluru"]
print(student)

#str = "hello"
#print(str[0])
#str[0] = "y"
#This can't be done in a string it gives error
#But is allowed in lists
student = ["Vaishnavi",21,"Bengaluru"]
print(student[0])
student[0] = "Nithya"
print(student)

#student = ["Vaishnavi",21,"Bengaluru"]
#print(student[5]) #This is not possible gives error
#Because we can only access the index assigned and cannot cross the limit

marks = [85,94,56,63,76]
print(marks[1:4])
print(marks[:3])
print(marks[2:])
print(marks[-3:-1])

list = [2,1,3]
list.append(4) #After this we have to print list again else will give NONE
print(list)
print(list.sort())
print(list)
print(list.sort(reverse = True))
print(list)

list = ["banana","apple","cucumber","f","d","e"]
print(list.sort())
print(list)
print(list.sort(reverse = True))
print(list)

list = [2,1,3]
list.reverse()
print(list)

list = [2,1,3]
list.insert(1,5)
print(list)

list = [2,1,3,4]
list.remove(1)
print(list)

list = [2,1,3,4]
list.pop(1)
print(list)

tup = (2,1,3,4)
print(tup)
print(tup[0])
print(tup[3])
print(tup[1:3])
#tup[0] = 5 #This is not allowed because tuple is immutable values cannot be changed

tup = ()
print(tup)
print(type(tup))

tup = (1) # this will be an integer because this is how a value will be written
print(tup)
print(type(tup)) # this answer will be int
#If we want a single element in tuple here is the right way to do it
tup = (1,)
print(tup)
print(type(tup)) 
#If the values assigned should be treated as tuple then there should be a comma after a single element may be of any type

tup = (2,1,3,1,4,1)
print(tup)
print(tup.index(1))
print(tup.count(1))

#WAP to ask the user to enter their 3 favourite movies and store them in a list
movies = []
a = str(input("Enter your favorite movie 1 : "))
b = str(input("Enter your favorite movie 2 : "))
c = str(input("Enter your favorite movie 3 : "))
movies.append(a)
movies.append(b)
movies.append(c)
print(movies)

#OR
a = str(input("Enter your favorite movie 1 : "))
b = str(input("Enter your favorite movie 2 : "))
c = str(input("Enter your favorite movie 3 : "))
list = [a,b,c]
print(list)
print(type(list))

#WAP to check if a list contains a palindrome of elements (Hint: use copy() method)
list1 = [1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("The list is palindrome")
else:
    print("The list is not palindrome")
print(list1)

list2 = [1,2,3]
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("The list is palindrome")
else:
    print("The list is not palindrome")
print(list2)

list3 = ['m','a','a','m']
copy_list3 = list3.copy()
copy_list3.reverse()
if(copy_list3 == list3):
    print("The list is palindrome")
else:
    print("The list is not palindrome")
print(list3)

list4 = ['m','o','t','h','e','r']
copy_list4 = list4.copy()
copy_list4.reverse()
if(copy_list4 == list4):
    print("The list is palindrome")
else:
    print("The list is not palindrome")
print(list4)

#WAP to count the number of students with the "A" grade in the following tuple 
# ["C","D","A","A","B","B","A"]
grade = ("C","D","A","A","B","B","A")
print(grade)
print(grade.count("A"))

#Store the above values in a list and sort them from "A" to "D"
grade = ["C","D","A","A","B","B","A"]
print(grade)
print(grade.sort())
print(grade)
'''
