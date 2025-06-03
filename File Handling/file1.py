'''f=open("text","r")
data=f.read() #read entire file
print(data)
print(type(data))
f.close()

f=open("text","r")
data=f.read(6)
print(data)
print(type(data))
f.close()

f=open("text","r")
line2=f.readline() #read one line at a time
print(line2)
print(type(line2))
f.close()

f=open("text","a")
f.write("\nI want to learn oops today") #adds to the file/append
f.close()

f=open("text","w")
f.write("\nI want to learn powerbi today") #overwrite the entire file
f.close()

#r+ is for reading and writing
f=open("text",'r+')
f.write("heyyy")# it overwrites
print(f.read())
f.close()

f=open("text",'w+')
#f.write("what u want to learn?")# it overwrites
print(f.read())
f.write("What is ur name?")
f.close()

f=open("text","a+")
print(f.read())
f.write("\nmy name is chandana")
f.close()

with open("text","r") as f:
    data=f.read()
    print(data)

with open("text","w") as f:
    f.write("\nhow are you?")

with open("practice.txt","w") as f:
    f.write("hi all\nwe are learning python")
    f.write("\ni like programming")

with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("programming","python")
print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)'''

def check_for_line():
        word="learning"
        data=True
        line_no=1
        with open("practice.txt", "r") as f:
            while data:
                data=f.readline()
                if word in data:
                    print(line_no)
                    return
                line_no+=1
        return -1
check_for_line()

