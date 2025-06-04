data=["hello","world"]
result=list(map(lambda x:list(x),data))
print(result)

#flatmap
#it flattens nested result into a single unit
from itertools import chain
data=["hello","world"]
result=list(chain.from_iterable(map(lambda x:list(x),data)))
print (result)
