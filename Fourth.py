"""
dict = {
    "key" : "value",
    "name" : "Vaishnavi",
    "learning" : "coding",
    "subjects" : ["Python","C","Java"],
    "Topics" : ("dict","set"),
    "age" : 35,
    "is_adult" : True,
    11 : 100,
    12.6 : 88.33
}
print(dict) # all the elements inside dict will be printed
print(type(dict))
print(dict["key"]) #to access a individual value of the particular key
print(dict["age"])

null_dict = {}
null_dict["name"] = "Vaishnavi"
print(null_dict)
dict["name"] = "Nithya" #overwrites
dict["surname"] = "HD"
print(dict)

#Nested dictionary
student = {
    "name" : "vaishnavi",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])

#Methods in dictionary
student = {
    "name" : "Vaishnavi",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student.keys())
print(list(student.keys()))
print(len(student.keys()))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
print(pairs[1])

print(student["name"]) 
print(student.get("name")) #both will give same answer
#print(student["name2"]) #error
print(student.get("name2")) #no error --> None
# when an error occurs, all the nxt lines will not run and code stops at the error
# so we should avoid errors while coding in real time scenario

new_dict = {"name" : "Nithya" , "city" : "Bengaluru" , "age" : 21} #name will be overwritten
student.update(new_dict)
print(student)

#Set in python
#List and dictionary cannot be stored in set because they are mutable
collection = {1,2,3,4}
print(collection)
print(type(collection))

collect = {1,2,2,2,"hello","world","world",4} #Duplicate values will be ignored
print(collect)
print(type(collect))
print(len(collect))

#Methods in sets
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("Vaish")
collection.add((1,2,3))
#collection.add([1,2,3]) --> unhashable(in which elements are mutable) error
collection.remove(1)
collection.clear()

print(collection)
collection = {"hello","Vaish","world","coding","python"}
print(collection.pop())
print(collection.pop())

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))

#Practice quetions
#WAP to store the following words in py dictionary
dict = {
    "table" : ("a peice of furniture","list of facts and figures"),
    "cat" : "a small animal"
}
print(dict)

#WAP, you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#Start with an empty dictionary and add one by one. Use subject name as key and marks as value
marks = {}
x = int(input("enter phy : "))
marks.update({"phy" : x})
y = int(input("enter chem : "))
marks.update({"chem" : y})
z = int(input("enter math : "))
marks.update({"math" : z})
print(marks)

#Figure out a way to store 9 and 9.0 as separate values in a set.
#(You can take help of built-in data types)
#1
set = {9,"9.0"}
print(set)
#2
set = {
    ("float",9.0),
    ("int",9)
}
print(set)
"""

