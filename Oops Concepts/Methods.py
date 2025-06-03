class student:
    college="oxford"
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks
    def welcome(self):
        print("welcome",self.name)
    def get_marks(self):
        return self.marks
s1=student("chandu",89)
s1.welcome()
print(s1.get_marks())

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum=sum+val
            avg=sum/len(self.marks)
        return avg


s1=student("chandana",[98,97,89])
print("hello",s1.name,"your avg is:",s1.get_avg())

