------> 21/03/24
# ! Method over- riding
 * ploymorphism in class
? Eg:1

class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def rayio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()
    

?EG:2

class USA:
    def langauge(self):
        print("English")

    def capital(self):
        print("Washington DC")

class India(USA):
    def langauge(self):
        print("None")
        
    def capital(self):
        print("New delhi")

I = India()
I.langauge()
I.capital()


EG:3

 ploymorphism using objects

c1, c2 ----> c1 = print(c1), print(c2)
f1, f2


class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        print("class2")

obj1 = c2()
obj1.f1()

obj2 = c1()
obj2.f1()

Eg:4

class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        print("class2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)


#* changing the functionality of builtin functions
class shoping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shoping([1,2,3,4,5])
print(len(s))


# ! -------> Method over loading
# ! Eg:1
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
s.add(4, 3) # ----> error
s.add(4, 5, 1)
        
# ! Eg:2
class suming:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj= suming()
obj.add(2)
obj.add(3, 4)
obj.add(1, 2, 3)


# --------->  AFTERNOON 1:00 to 5:00

# ! -----> Abstraction
The process of hiding the implimentation details is abstraction

? Eg:1
from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

    def sides(self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
        
tr = triangle()
tr.traingle_sides()
tr.name()


# ! Rules to define abstract class 1
1.) Abstract class cannot be instantiated
2.) From abc import ABC, abstractmethod
3.) subclass the normal class with ABC
4.) Convert the normal method inside the abstract class to abstract method
5.) All the child classes have to be subclassed with abstract class
6.) The abstract method should be present in the child classes


# ! Eg:2
# super() ---. used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass

class2 = c2()
class2.m2()

# Eg:3
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd
    

class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name, '!!')
            print("Login Sucessful")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)



# ! Encapsulation

# *------->Eg:1
class car:
    __name = "BMW"  private variable
    print(__name)


c1 = car()
print(c1.name) error
c1.name = "Audi"
print(c1.name) error

# *---> Eg:2
Accessing private data outside the class
class c1:
    __phone = '9949192954'

    def display(self):
        print(self.__phone)
c = c1()
c.display()



# *-----> Eg:3
declare private method
class class1:
    def __m1(self): #private method
        print("Iam private method")

    def __init__(self):
        self.__m1()
c = class1()
c.__m1() #error



# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.display()
    
    







a = 9
b = 6
print(a+b)
print(a.__add__(b)) # ? dunder method or mafic method
















