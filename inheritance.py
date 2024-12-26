
#single lavel inheritance
"""
print("---------------------Single lavel inheritance--------------------")
class parents:
    def name(self):
        print("I am parent class")

class child(parents):
    def sernmae(self):
        print("I am child class")
        
object = child()
object.name()
object.sernmae()
"""


#multy lavel inheritance 
"""
print("---------------------Multy lavel inheritance--------------------")
class parent1:
    def name(self):
        print("My name is Jay.")
        
class parent2(parent1):
    def sername(self):
        print("My Sername is gohil")

class parent3(parent2):
    def fathername(self):
        print("My father name is mayurbhai")
        
object = parent3()
object.sername()
object.name()
object.fathername()


"""

#multiple inheritance

"""
print("---------------------Multiple inheritance--------------------")

class parent1:
    def name(self):
        print("My name is Khavad")

class parent2:
    def surname(self):
        print("my surname is Vyas")
        
class parent3(parent1,parent2):
    def fathername(self):
        print("My father name is Jasubhai")
        
obj1 = parent3()
obj1.surname()
obj1.name()
obj1.fathername()
        
"""
#Hierarchical inheritance 
"""
print("---------------------Hierarchical inheritance--------------------")

class parent:
    def surname(self):
        print("my surname is soni")

class parent1(parent):
    def name(self):
        print("My name is Jay")
        
class parent2(parent):
    def fathername(self):
        print("My father name is Jasubhai.")

class parent3(parent):
    def grandfather():
        print("My grand father name is Kagjidada")
        
#parents1 class object
obj1= parent1()
obj1.name()
obj1.surname()

#parents2 class object
obj2= parent2()
obj2.surname()
obj2.fathername()

#parents3 class object
obj3= parent3()
obj3.surname()
obj3.grandfather()

"""

#Hybrid inheritance


print("---------------------Hybrid inheritance--------------------")
class parent:
    def surname(self):
        print("My surname is Meva")

class parent1(parent):
    def name(self):
        print("my name is shivam.")
        
class parent2(parent):
    def fname(self):
        print("My Fname is Ghanshyam bhai")
        
class parent3(parent1,parent2):
    def gname(self):
        print("My gname is Muljidada")
        
#object creation for Parent1 class
obj1 = parent1()
obj1.name()
obj1.surname()

#object creation for Parent2 class
obj2 = parent2()
obj2.surname()
obj2.fname()

#object creation for Parent3 class
obj3 = parent3()
obj3.surname()
obj3.name()
obj3.fname()
obj3.gname()