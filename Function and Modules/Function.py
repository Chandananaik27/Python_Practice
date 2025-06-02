def sum(a,b): #parameters
    return a+b
calc_sum=sum(3,4) #function call;arguments
print(calc_sum)

def cal_avg(a,b,c):
    avg=(a+b+c)/2
    return avg
print(cal_avg(6,3,5))

def cal_prod(a=1,b=2): #default argument
    print(a*b)
    return a*b
cal_prod()

def student(name, age, bloodgroup): #keyword argument
    print("Name:", name)
    print("Age:", age)
    print("bloodgroup:",bloodgroup)

student(age=20, name="Asha",bloodgroup="ab+")

def total(*numbers):
    print("Total is:", sum(numbers))

total(10, 20, 30)

def info(**details):
    for key, value in details.items():
        print(key, ":", value)

info(name="Ravi", age=21)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Calling the function
num = 5
print("Factorial of", num, "is:", factorial(num))

cities=["delhi","bhatkal","bunder","banglore"]
heroes=["yash","rahul","puneeth","ironman"]
def print_len(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heroes)




