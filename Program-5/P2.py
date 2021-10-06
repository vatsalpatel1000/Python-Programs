# Multilevel inheritance
class Student:
    def __init__(self):
        self.usn=''
        self.name=''
        self.age=''
    def getdata(self):
        self.usn=int(input("Enter the USN:"))
        self.name=input("Enter the Name:")
        self.age=int(input("Enter the age:"))

class Derived1(Student):
    def __init__(self):
        self.s1=0
        self.s2=0
        self.s3=0
        self.s4=0
        self.s5=0

    def getmarks(self):
        super().getdata()
        self.s1=int(input("Enter the subject1 marks:"))
        self.s2=int(input("Enter the subject2 marks:"))
        self.s3=int(input("Enter the subject3 marks:"))
        self.s4=int(input("Enter the subject4 marks:"))
        self.s5=int(input("Enter the subject5 marks:"))
d={}
class Derived2(Derived1):
    def __init__(self):
        super().__init__()
    def display(self):
        self.total=self.s1+self.s2+self.s3+self.s4+self.s5
        self.percent=self.total/500*100
        print("USN :", self.usn)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Total :",self.total)
        print("Percentage :", self.percent)
    def dis(self):
        for key in d:
            print(key,d[key])


n=int(input("Enter the number of students:"))
if n==0:
    print("Enter a valid input")
else:
    for i in range(1,n+1):
        d2=Derived2()
        d2.getmarks()
        d2.display()
        d[d2.name]=d2.__dict__
        print(d)
