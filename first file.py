print("hello world")
print("hello"+" "+"world")

#Workin with Python variables
name =input ("what is your name")
age = input ("what is ur age?")
len=len(name)
print(len)
print(age)

# datatypes
age=20
name="chandu"
price=78.88
print(type(age))
print(type(name))
print(type(price))

#arithmatice operators
a=6
b=11
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

#relational operator
a=13
b=12
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

#assaignment operator
num=10
num+=10
num-=10
print(num)

#logical operator
val1=50
val2=10
print(not False)
print(not (val1 > val2))

#operation on string
str1="chan"
str2="naik"
concat=str1+str2
print(concat)
print(len(concat))
print(concat[4])

#slicing
str="chandana naik"
print(str[1:4])
print(str[9:13])
print(str[5:])
print(str[:4])
print(str[-4:-1])
print(str[:-4])

str="hello what are u doing and how are you."
print(str.endswith("you."))
print(str.capitalize())
print(str)
print(str.replace("o","a"))
print(str.find("a"))
print(str.count("a"))

#conditional statements
age = 20
if age>=18:
    print("eligibel for voting")
else:
    print("not eligible")
marks=int(input("enter marks:"))
if(marks>=90):
    grade="a"
elif (marks>=80 and marks<90):
    grade="b"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="d"
print("grade of student",grade)
age=81
if (age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
    print("can vote")
else:
    print("cannot vote")

#loops
count=1
while count<=5:
    print("hello")
    count+=1
i=1
while i<=5:
    print(i)
    i+=1

i=1
while i>=5:
    print(i)
    i-=1
num=(1,4,9,16,25,36,49,64,81)
x=36
i=0
while i<len(num):
    if (num[i]==x):
        print("found at index",i)
    else:
        print("not found")
    i+=1
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
i=0
while i<=5:

    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1
