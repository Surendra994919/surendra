14/03/24

# ----> while loop
# -----> break using while loop

Eg:1
1.)Iterate form 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
    
Eg:2
i = 20
while i<31:
    print(i)
    i+=1
    if i ==27:
        break
    
Eg:3
i = 20
while i<31:
    print(i)
    if i ==27:
        break
    i+=1
    


Eg:4
i = 20
while i<31:
    if i ==27:
        print(i)
        break
    i+=1

# !---> continue
eg:1
i = 20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1

eg:2
i = 20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)

eg:5   
# while to iterate from 12 to 22
# find the sum all numbers

i = 12
while i<23:
    print(i)
    i=i+1
    
i =12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)

Eg:6
# Find the average of value from 20 to 25

i = 20
sum=0
while i<26:
    sum=sum+i
    i+=1
print(sum/6)

    
# Find the average of value from 20 to 30

i = 20
sum = 0
count = 0
while i<=30
    sum = sum+1
    count+=1
    i+=1
print(sum/count)

# ! -----> Nested for loop
Eg:1

for i in range(1, 3):
    for j in range(1, 4);
        print(i,j)

for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row,col)

Eg:2
 * * * *
 * * * *
 * * * *
 * * * *

for row in range(4):
    for col in range(4):
        print("*")
        
rows = int(input("enter the rows:"))
cols = int(input("enter the cols:"))

for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
    print()


AFTERNOON 1:00 TO 5:00


for row in range(5):
    for cool in range(5):
        print(row, end=" ")
    print()

sum = 0
for row in range(5):
    for cool in range(5):
        sum= sum+1
        print(sum, end=" ")
    print()

# ! to print stars in right angle tirangle

for row in ragne(0,6):
     for col in range(0,row+1):
        print("*", end=" ")
     print()

     

for row in range(0,6):
     for col in range(row+1,6):
        print("*", end=" ")
     print()

##
* * * * *     
*       *
*       *
*       *
* * * * *

for row in range(5):
     for col in range(5):
         if col == 0 or col==5-1 or row == 0 or row == 5-1:
          print("*", end=" ")
         else:
          print(" ", end=" ")
     print( ) 
    

##
     
   *
 * * *
* * * *

for row in range(0,5):
    for col in range(0,5):
        if ((row==0 and col==3) or (row==1 and(col>=2 and col<=4))or(row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
       print( ) 


# !----> list


# ------> Datatypes
# Primary


# Number ---> int, float complex
# String
# Boolean
# None


# Collection
# list
# tuple
# set
# dictionary


# ? ----> List

1.) if the collection of element are surrounded by square brackets, it is considerd to be list
# ! eg:
    11 = [4, 7, 9, 9.89, "hello", 7+9], [8, 9, 0]]



# * charactristics of list
 1.) List have to be sorrounded by []
 2.) It is mutable (the element in list are changable)
 3.) Every element inside list is 
 4.) The elements inside list will be ordered format
 5.) It can hold duplicate values
 6.) Its heterogenous

To access the elements in list
lst1=[1,4,1,7,89,7,7,5,"p","i"]
   print(l1)


----> indexing
In the collection datatypes like list, tuple, string,the elements will be alloted
With pre defined unique value called index value

We have 2 types of indexing
Positive indexing----> starts with 0 from left hand side
Negative indexing----> starts with -1 from right hand side


# ? ----> Positive indexing
list = [1, 4, 1, 7,7.5,"p", "i"]
print(lst1[])
print(lst1[4])
print(lst1[20])----> error
        

# ? ------> Negative indexing
lst = [1, 4, 1, 7,89.7, 7.5,"p","i"]
print(lst1[-1])        
print(lst1[-5])


# ? ----> slicing
lst = [1, 4, 1, 7,89.7, 7.5,"p","i"]        
lst[start_index:end_index:step]
        
print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])


print(lst1[0:7:1]) #lst1[0:7] --> both are same
print(lst1[0:7:2])        

 
Trial = int(input())
        

lst1 = [1, 4, 1, 7,89.7, 7.5,"p","i"]
print(lst1[-4:-1])        
print(lst1[-1:-4]) -->[]        
print(lst1[-7:-1])        
print(lst1[-7:-1:2])        


#! To insert at add element inside list

append() ---> used to add element at last position of list
l1 = [9, 8, 0, 6]
l1.append("car")
print(l1)







