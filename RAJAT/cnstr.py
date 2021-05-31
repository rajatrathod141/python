class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
s=Student("rajat",1)
print(s.name)
print(s.rollno)



class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def  __str__(self):
        return "rollno:-{} name:-{}".format(self.rollno,self.name)
s=Student(1,"rathod")
print(s)
