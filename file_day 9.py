1------>20/03/24   day 9

find the uncommon words from 2 strings
s1 = "Hello how are you"
s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
         print(val)

Write a code print the 8th fibanochi number
0,1,1,2,3,5,8

num = 5
n1 = 0
n2 = 1
ans = 0+1==>1

n1 = 1
n2 = 1
ans = 1+1==>2

n1 = 1
n2 = 2
ans = 1+2==>3

n1 = 2
n2 = 3
ans = 2+3==>5

for val in range(5):
    ans = n1+n2
    print(ans)

# Find the 8th fibanochi number

num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)


# ! constructors
?Eg:2
* unparametarised constructor
class profile:
    def __init__(self):
        print("hello world")

obj = profile()
obj.__init__()


? Eg:3
* parametarised constructor
class profile:
    def __init__(self, id, name, age):
        print(id, name, age)
        
obj = profile(1, "surendra", 23)


? Eg:4
class c1:
    email = "sid@gmail.com"

    def m1(self):
        name = "surendra"
        place= "cbe"
        print(name,place)
        print(self.email)

object = c1()
object.m1()

? Eg:5
class c1:
    def m1(self):
        name = "surendra"
        age = 23
        return name,age
    def display(self):
        # ! print(name,age)
        # ! print(self.name,selt.age)
        print(self.m1())

object = c1()
object.display()

? Eg:6
 To use the variable inside the constructor in another method
class class1:
    email = "sid@gmail.com" ----> static variable
    def __init__(self):
        name = "sid"------> instance variable
        email = "sid@gmail.com"
        return name, email error ----> cannot use return with constructor

def display(self):
    print(self.name,self.email)

c1 = class1()
c1.display()


# ! ------> 
The process of utilising the methods and attributes of parent class
through the object of child class it is called as Inheritance

# ? 5 types of Inheritance
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hybrid Inheritance
5. Heirarichal Inheritance

# * Single Inheritance
It has only one parent class and only one child class
# ! Eg:1
class parent:
    def m1(self):
        print("Iam parent class")

class child(parent):
    def m2(self):
        print("Iam child class")

obj = child()
obj.m1()

# ! Eg:2
class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass

obj = child1()


# ! Eg:3
class parent:
    name = "surendra"
    
class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()


# ! Multilevel Inheritance
?Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


?EG:2
class honda_city : 
    def honda_city_engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,HP,torque,fuel_type,num_of_piston)

    def honda_city_body_specs(self,colour,weight,length,vehicle_type):
        print(colour,weight,length,vehicle_type)
        
class amaze (honda_city):
    def amaze_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
        print (cc, Hp, torque, fuel_type, num_of_piston)

    def amaze_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)

class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, "Hatchback")
        



# ! Multiple Inheritance
 It has multiple parent and 1 child

class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
        
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
        
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
        
p=petrol()
p.defanition()
p.function_o()

# ! Eg:2
# MRO --> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
        
    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc = division() 
# calc.add(3, 4)
calc.mul(4, 2)


# ! Heirarichal Inheritance
 The one parent class will acts as parent for all the child class
class catagory:
    def cat_name(self,weight):
        print("weight")

class Tomato:
    def tomato_specs(self):
        color="black"
        taste="neutral taste"

class carrot(category):
    def carrot_specs(self):
        color="green"
        taste="sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")


t=tomat()
t,tomato_specs()
t.weight("20gms")


# ! Hybrid Inheritance
The combation of above 4 inheritance is called  Hybrid Inheritance
class c1:
    def m1(self):
        print("Class1")
class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6(c5,c3):
    def m6(self):
        print("Class 6")

obj=c6()
obj.m3()


# !----------> Polymorphism

poly - many,morph-->
A function which has the ability to perform more than 1 functionality
then it is considered to be as polymorphism


ploymorphism in built in functions
len()-->which is used to find the length of list,tuple,dict etc..
index()
max()
min()
count()
pop()
and more...

polymorphism in operators
+
print(8+8)
print("k" +'1')
print([1,2,3]+[5,6])



print(6*7)
l1 = {12,3,4,5,6}
print(*11)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)


polymorphism in classes
we can achieve polymorphism in 2 ways
1.method overloading---->it is not possible in python
2.method overriding












