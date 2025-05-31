'''nums=[1,4,9,16,25,36,49,64,81,100]
for num in nums:
    print(num)

char="chandana"
for char in char:
    print(char)

name = ("diggibyte")
for i in name:
    print(i)
else:
    print("end of exexcution")

nums=(1,4,9,16,25,36,49,64,81,100)
x=49
index=0
for num in nums:
    if num==49:
        print("number found at index",index)
        break
    index+=1'''

'''str="chandana"
for char in str:
    if(char=='d'):
        print("d found")
        break
    print(char)
else:
    print("loop end")
    
#Range
for i in range(5):
    print(i)

for i in range(2,6):
    print(i)

for i in range(5,0,-1):
    print(i)

n=int(input("enter number:"))
for i in range  (1,5):
    print(n*i)'''

sum=0
n=int(input("enter number:"))
for i in range(1,n+1):
    sum+=i
print(sum)

n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("fact =",fact)


