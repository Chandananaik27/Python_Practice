def topten():
    yield 1
    yield 2
    yield 3
    yield 4
for number in topten():
    print(number)

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
value=topten()
for i in value:
    print(i)
