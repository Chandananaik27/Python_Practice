def div(a, b):
    print(a / b)
sum=div(2,4)
print(sum) #output 0.5

def div(a,b):
        print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
div1(2,4) #output 2


