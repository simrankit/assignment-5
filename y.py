
print("question 1:")
def reverse(s):
    s=s[::-1]
    return s
s=input(" ")
print("The original string is:")
print(s)
print("The reversed string is:")

print("question 2:")
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
      if (i%n==0):
         print(i)

print("question 3:")
a=float(input("Enter the first side of the triangle:"))
b=float(input("Enter the second side of the triangle:"))
c=float(input("Enter the third side of the triangle:"))
if a+b>c and b+c>a and c+a>b:
      #semi perimeter
      s=(a+b+c)/2
      #area
      area=(s*(s-a)*(s-b)*(s-c))**0.5
      print("The area of the triangle is:",area)
else:
      print("triangle is not formed:")

print("question 4:")
n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

print("question 5:")
rows=int(input("Enter:"))
print("Pattern is:")
alphabet=65
for i in range(rows):
      for j in range(i+1):
         print("%c"%alphabet,end="")
         alphabet=alphabet+1
      print()

print("question 6:")
lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)

print("question 7:")
lower=1
upper=500
for i in range (lower,upper+1):
    if (i%7==0 and i%11==0):
        print(i)

print("question 8:")
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
d=int(input("Enter a value:"))
e=int(input("Enter a value:"))
f=int(input("Enter a value:"))
g=int(input("Enter a value:"))
h=int(input("Enter a value:"))
i=int(input("Enter a value:"))
j=int(input("Enter a value:"))
list1=[a,b,c,d,e,f,g,h,i,j]
for i in list1:
    if i>0:
        print("Positive number:",i)
    elif i<0:
        print("Negative number:",i)
for j in list1:
    if j%2==0:
        print("Even number:",j)
    else:
        print("Odd number:",j)
def counter(list1,x):
    count=0
    for item in list1:
        if (item==x):
            count=count+1
    return count
x=int(input("Enter the value whose count you want to find in the list:"))
y=counter(list1,x)
print("The element",x,"appears",y,"times in the list")

print("question 9:")
str=input("Enter line of string")
str=str.split()
i=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"Present",count,"Times")
    i=i+1
    

