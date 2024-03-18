--------> 18/03/24

2.)python program to determine if the given sets are Disjoint not without using inbuilt in functions


set1 = {'python','java', 'data scince'}
set2 = {'ML','AI','R Language','python'}
set3 = {'Data Analytics','Robotics','Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
     if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
     if c==3:
        for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flage==0:
    print('Disjoint')
else:
    print('joint')


3.)
list1 = ["m","na","i","ke"]
list2 = ["y","me","s","lly"]

l3 =[]
for val in range(len(list1)):
    ans = list1[val]+list2[val]
    l3.append(ans)
print(l3)

i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)


# ! -----> Functions
? DEF
Function is a block of code which is used to perform a specific functionally
Function can be created using def keyword


Function has 3 parts
1.Function declaration
2.Function defination
3.Function call

# ! Eg:1
def greet(): Function defination 
    print("Greetings User!!")
greet()
greet() 
greet()
greet()
greet()
greet() function calling

# ! Eg:2
Function with parameter
def greeting(name):
    print("Welcome",name)

for val  in range(3):
    username = input("Enter the name:")
    greeting(username) Username is argument

# ! Eg:3
def profile(name,age,place):
    print(name,age,place)
profile("sid",29,"Ap")








         
            
