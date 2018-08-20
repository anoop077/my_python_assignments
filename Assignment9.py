#Question1
'''
class animal:
    def animal_att(self,string):
        print("The Tiger is the symbol of power."+string)
class tiger(animal):
    def show(self):
        self.animal_att("They are quite cautious and energetic.")
'''
#Question2
'''
A A
'''
#Question3
'''
class cop:
    name=""
    age=""
    work_experience=1
    designation=""
    def add(self,n,a,w,d):
        self.name=n
        self.age=a
        self.work_experience=w
        self.designation=d
    def display(self):
        print("NAME: ",self.name)
        print("AGE: ",self.age)
        print("WORK_EXPERIENCE: ",self.work_experience)
        print("DESIGNATION: ",self.designation)
class mission(cop):
    def add_mission_details(self,m):
        print("MISSION: ",m)
'''
#Question4
'''
class shape:
    length=int()
    breadth=int()
    def area(self,l,b):
        self.length=l
        self.breadth=b
        return self.length*self.breadth
class rectangle(shape):
    def display(self):
        l=int(input("Enter the length: "))
        b=int(input("Enter the breadth: "))
        print("Area of Rrectangle is ",self.area(l,b))
class square(shape):
    def display(self):
        a=int(input("Enter the length: "))
        print("Area of Square: ",self.area(a,a))
'''
