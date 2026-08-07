
#Input a number and check whether it is even or odd.
n = int(input("Enter a number: "))
if n%2==0:
    print("The entered number is EVEN")
else:
    print("The entered number is ODD")

#Largest of 3 Numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if (a>b & a>c):
    print("1st number is the largest ",a)
elif (b>a & b>c):
    print("2nd number is the largest ",b)
else :
    print("3rd number is the largest ",c)


