#Lists

marks=[45,4,5,6,37]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])

student=["chan",45,78,"Chai"]
print(student)
student[0]="ram" #changing value
print(student)

marks=[96,78,67,45.67,43]
print(marks[1:4])
print(marks[:4]) #slicing
print(marks[1:])
print(marks[-3:-1])

list=[5,7,9,3]
list.append(1) #add elements in the end
print(list.sort()) #sort in asc order
print(list.sort(reverse=True)) #sort in desc order
print(list)
list=["chan","chai","leo","ram"]
list.reverse()
print(list)
list=[4,2,5]
list.insert(1,1)
print(list)
list=[2,1,3,1]
list.remove(1) #removes first occurence of element
print(list)
list=[2,1,3,1]
list.pop(2) #remove element at index
print(list)

numbers = [4, 1, 3, 2]
# Use list comprehension to get square of each number
squares = [x*x for x in numbers]
squares.sort()
print("Sorted squares:", squares)

#Tuple
tup=("Hello",4,5,6)
print(tup)
print(type(tup))

grade=("c","d","a","a","b","b","a")
print(grade.count("a"))

#garde=(3,5,6,8,1,9)#
print(grade[1:3])
print(grade[-4:])
print(grade[:-1])

names=("chan","mike","chai","leo","lakshman")
name=list(names)
name.append("chandana")
print(name)









