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
print(name)'''

#Sets

'''collection={4,5,7,8,"hello","world","hello"}
print(collection)
print(type(collection))
print(len(collection))

collection=set() #empty set creation
print(type(collection))

collection=set()
collection.add(1)
collection.add(7) #add element to the set
collection.add("chandana")
print(collection)
print(len(collection))

collection=set()
collection.add(1)
collection.add(7) #add element to the set
collection.add("chandana")
collection.clear() #empties the set
print(collection)
print(len(collection))

collection={"hello","python","world","chandan"}
print(collection.pop())
print(collection.pop())

set1={1,4,6}
set2={4,7,9}
#union to combine two set and return new value
print(set1.union(set2))
#combine common value and return new
print(set1.intersection(set2))

sub={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(sub))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 9, 6}
# Difference: Elements in set1 but not in set2
result = set1.difference(set2)
print("Difference (set1 - set2):", result)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Symmetric Difference: Elements not common to both sets
result = set1.symmetric_difference(set2)
print("Symmetric Difference:", result)

#Dictionary

dict={"name":"chandana",
    "age":21,
    "bloodgroup":"ab+",
    "marks":[67,90,78],
    12:94 }
print(dict)
print(type(dict))
print(dict["name"])
print(dict["age"])
dict["surname"]="naik"
print(dict)

#nested dictionary

student={
    "name":"chaitanya",
    "subjects":{
    "physics":90,
    "chemistry":89,
    "math":87
   }
 }
print(student["subjects"]["chemistry"])

student={
    "name":"chaitanya",
    "subjects":{
    "physics":90,
    "chemistry":89,
    "math":87
   }
 }
print(student.keys()) #return all key values
print(list(student.keys()))
print(len(list(student.keys())))
#return all the values
print(student.values())
#return all (key,value) pairs as tuples
print(student.items())
#return the key according to value
print(student.get("name"))
#insert the specified value to dictionary
student.update({"city":"banglore","rollno":78})
print(student)









