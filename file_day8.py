-------> 19/03/24

Eg:3
def profile(name, age, place):
    txt ="My name is {}.Iam {} years old. Iam from {}."
    print(txt.format(name,age,place))
profile("surendra", 23, "kadapa")

# ! Eg:4
? Function with return statement

# ! return
1.) A variable declared inside the function can be accessed outside the function
   using return
2.) return does not print anything
3.) we cannot write any code below return statement


def f1():
    z = 8
f1()
print(z) error ------> cannot use outside the function


def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj = f1(6 ,8)
obj1 = f1(4, 6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)


# ? problem:1

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value"))
palindrome(a)

# ? Based on the declaration of parameter and args
# ? functions are divided into 5 catagories

-> Positional args
-> Keywords args
-> Default args
-> Variable length args
-> Keyword variable length args

# * Position args
#? The position of parameter have to be same as position as argument
#! Eg:1
def profile(name, phone, mark):
    txt ="My name is {}. My phone number is {}. I got {} marks."
    print(txt. format(name, phone, mark))

profile("surendra", 9949192954, 99) unexpected output


# * Keywords args
# ! Eg:1
 ? To overcome the advantage of position args,ArithmeticError we use keyword args
 It is the process of initialising the parameter with args while calling the function

def profile(name, phone, mark):
    txt ="My name is {}. My phone number is {}. I got {} marks."
    print(txt. format(name, phone, mark))

profile(name="surendra", phone=9949192954, mark=99)


# todo ----> Exception of keyword args function

def profile(name, phone, mark):
    txt ="My name is {}. My phone number is {}. I got {} marks."
    print(txt. format(name, phone, mark))

profile(name="surendra", phone=9949192954, mark=99) error--> positional args follow keyword
profile(9949192954, name="surendra", mark=99) error--> name has multiple values
profile("surendra",mark=99, phone=9949192954)


# * Default args
The method of assigning the argument to the parameter while declaring the function
# !EG:1
def profile(name, phone, place="kadapa"):
    txt ="My name is {}. My phone number is {}.  I am from {}."
    print(txt. format(name, phone, place))

profile("surendra", 9949192954)


# Eg:2

def profile(name, phone, place="KADAPA"):
    if place =="kadapa" or place=="KADAPA" or place=="kadapa":
        txt ="My name is {}. My phone number is {}. I am from {}."
        print(txt. format(name, phone, place))
    else:
        print("You are not eligible to Signup")


profile("surendra", 9949192954)


# ! Exception

profile(name, place="KADAPA", phone): error-->coz defalut args should not follow
                                      positional parameter
 if place =="kadapa" or place=="KADAPA" or place=="kadapa":
        txt ="My name is {}. My phone number is {}. I am from {}."
        print(txt. format(name, phone, place))
    else:
        print("You are not eligible to Signup")


profile("surendra", 9949192954)



# * Variable length args
To pass more then 1 arg to a parameter means we use variable length args
To convert normal parameter to variable length param, add* to there prefix of parameter

# ! Eg:1

 name =  "surendra", 'name2', 'name3'
def profile(*name):
    for val in name:
        print("My name is",val)
profile("surendra", 'name2', 'name3')


Afternoon 1:00 to 5:00

# ! Eg:2
def profile(*name, age):
    for val in name:
        print("My name is",val, "my age is", age)
profile("surendra", 'name2', 'name3', 23) error ---> age has no args

 
def profile(age, *name):
    for val in name:
        print("My name is",val, "my age is", age)
profile(24, "surendra", 'name2', 'name3')


# * Keyword variable length args
Kwargs ---> which is used to provide the args in the form of key value pair.
Eg:1
def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)


n = 5
{1:1, 2:4, 3:9, 4:16, 5:25}


n = int(input("Enter the number:"))

def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)


# ! -------> object oriented programming
The paradigns of objects oriented programming are

Class
Objects
inheritance
polymorphism
abstraction
encapsulation

# ! Class is a blue print of an object
l1 = [1,2,3,4,5,6]


? Eg:1
class c1:
    name1 = "surendra"
    print(name1)


? eg:2
class person:
    name = "surendra"

c = person() c os object
The process of creation of an object is called as Instantiation
print(c.name)

? Eg:3
create of a method
When the function is created with a class is called as method

# ! Method without parameter
class person:
    def display():  It is a method
        print("Hello welcome to classes")

p = person()
p.display()


?Eg:4
# ! Method with parameter
class person:
    def display(person, name, age):
        print(name, age)

p = person()
p.display("surendra", 23)


? Eg:5
class person:
    fname = "surendra" #attribute or static variable
    1name = "B"
    
    def first_name(self):
        print(self.fname):

    def full_name(self):
        print(self.fname+""+self.1name)

p = person1()
p.first_name()
p.full_name()

? Eg:6
Constructors -----> _int_()
This is a special method which has the ability to excute itself without
calling it manullay through the process of instantiation

class profile:
    def _int_(self): # constructor method
        print("hey")

p = profile() #execution of constructor through this process











    

    


