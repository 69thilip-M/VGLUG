#single inheritance 
'''class Akatsuki():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Display(self):
        print(self.name)
        print(self.age)
    def Details(self):
        print("My Name is {} and My Age is {}".format(self.name,self.age))
    def SayHi(self):
        print("hi")
        
class Pain(Akatsuki):
    def __init__(self,name,age,power,clan):
        print("Calling the child class")
        self.power=power
        self.clan=clan
        Akatsuki.__init__(self,name,age)

    def DisplayAll(self):
        print("My Name is {} and My Age is {}. power is {} and clan {} ".format(self.name,self.age,self.power,self.clan))
        
a=Pain("Tobi",13,"Sharingan","Uchiha")
a.DisplayAll()'''

#Polymorphism
'''def  add(a,b,c=10):
    print(a+b+c)
add(1,2,3)
add(1,2)'''


    
#method overriding
'''class Naruto:
    def Akatsuki(self):
        print("Villans")
    def Squad7(self):
        print("Legendary Sanin")
class OrochiMaru(Naruto):
    def Squad7(self):
        print("Sasuke")

class Jiraiya(Naruto):
    def Squad7(self):
        print("Minato Namikaze")
ob1=Naruto()
ob2=OrochiMaru()
ob3=Jiraiya()
ob1.Squad7()
ob2.Squad7()
ob3.Squad7()'''
