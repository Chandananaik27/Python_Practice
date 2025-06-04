f=lambda a:a*a
result=f(5)
print(result)

from functools import reduce
nums=[3,2,6,8,4,6,2,9]
even=list(filter(lambda n: n%2==0,nums))#output[2,6,8,4,6,2]
doubles=list(map(lambda n: n*2,even))
print(even)
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)
