--------> 15/03/24

# ! -----> Common function for list

l1 = [6, 7, 8, 9, 0]
print(len(l1))

print(max(l1))
print(min(l1))


l1 = [6, 8, 9, "P", "u"]
print(max(l1))-----> error coz its a combation of int and string
print(min(l1))-----> error coz its a combation of int and string


l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
index() ---> to get index value of specific element
print(l1.index(9))


l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
count() --> how many num of times an element is repeated
print(l1.count(6))

#! some functions which is specifically used for list


To add element inside list
# ? insert(index_value, element) ---> to add element at specific index position
l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2, "cars")
print(l1)


? To delete element from list
l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
pop() ---> last element will be deleted
l1.pop()
print(l1)


pop(index_value) ---> used to delete element at specific index
l1.pop(4) 4 is index value
print(l1)


#! remove(element)--> used to delete directly
l1.remove (8.89)
print(l1)

#! clear()--> to complete delete all element in list
l1.clear()
print(l1)


del ---> to delete the list
del l1 #or del(l1)
print(l1)


# ? -----> join 2 list

l1 = [9, 0, 8]
l2 = ("p", "o", "t", 34]
print(l1+l2)


# ! or

extent() ---> to cobine 2 lists
l1.extent(l2)
print(l1)


# ? -------> copy()

l1 = [6, 7, 8, 9, 3]
l2 = l1.copy()
print(l2)
print(l1)

print(id(l1))
print(id(l2))


# ! diff b/w shallow copy and deep copy
# *shallow copy
import copy
l1 = [8, 9, 0,[5, 6],[3, 2, 1]]
l2 = copy.copy(l1)
l1.append(890)
print(l2)
print(l1)


#*deeep copy ---> used to copy the list with nested list
import copy
l1 = [8, 9, 0,[5, 6],[3, 2, 1]]
print(l1[-1][1]) ---> to index nested list

l2 = copy.copy(l1)
l1.append(890)
print(l2)
print(l1)


# ? sort ---> arrange element in list in ascending or decending order
l1 = [9, 7, 45, 0,-6, 5, 12]
l1.sort() to arrange in ascending order
print(l1)

l1.sort(reverse=True) to sort in decending order
print(l1)

l1 = ['z', 'i', 'o', 'p', 9]
l1.sort()
print(l1)---> error

list constructor
list() ---> to conver other collection datatype to list
l3 = ((8, 9, 0))
print(list(l3))


l4 = (8, 9)
print(list(l4))

# ! ---> nested list

l1 = [8, 9,[0, 8, 7],["p", "o", "y"],[8, 't']]
print(l1[-2][1]) ---> o

print(l1[1:4])
print(l1[1:-1])

# ? TO delete 't' from l1
l1[-1].remove("t")
print(l1)


# ? combine these ["p", "o", 'y'][8, 't'] list in l1 to ["p","o","y",8,'t']
l1[-2].extent(l1[-1])
l1.pop(-1)
print(l1)


# ! --------> Tuple
# *char of tuple

1.) Tuple have to be surrounded by ()
2.) The elements inside tuple are not changable
3.) The elements inside tuple are indexed
4.) The element will execute in order
5.) It is heterogenous
6.) It allow duplicate elements



Eg:1
t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey",9+6j)
print(t1)
print(type(t1)

# ? indexing, slicing are all same as list
      
? ways to create tuple
l1 = (8)
print(type(l1)) int


l1 = (8,)
print(type(t1)) tuple


t1 = 8,9
print(type(l1)) tuple 

t2 = 8,
print(type(t2)) tuple


len(),min(),max(), index(), count()--->all same as list


to add element inside tuple -----> cannot add
cannot delete any element from tuple
      

# * join 2 tuple
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)


To add all element inside list and tuple
sum()      
l1 = (8, 9, 7, 6)
print(sum(l1))


# * sort tuple
t1 = (8, 9, 0, 89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=Ture)))

# * Iterate list and tuples

Iterate based on elements
l1 = [9,8,0,6,5]
for i in l1:
    print(i)  


# *Iterate based on index value 
l1 = [9,8,0,6,5]
for i in range(0, 5):
    print(i)

l1 = [9, 8, 0, 6, 5, 8,56]
for i in range(0,len(l1)):
    print(l1[i])


AFTERNOON 1:00 to 5:00
      
# ! --------> STRINGS

s1 = 'o'
print(type(s1))

s1 = "u"
print(type(s1))

      
s1 = "hell world"
# * To access string
print(s1)      
# indexing and slicing ---> same as list and tuple
print(s1[0:5])


# -----> common functions

len(), min(), max(), index(), count()
s1 = "hell world"
print(len(s1))
print(max(s1))
print(min(s1))


ord() ---> used to find the ASDCII value of a character
s1 = "u"
print(ord(s1))


# ! Functions of string
s1 = "hell world"


# ? to convert all characters to upper case
print(s1.upper())


# ? to convert to lower case
s1 = "HFRDGiou"
print(s1.lower())


# ? strip() -----> to eliminate the space in beginning and end of string
s1 = " Where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())


# split()---->to split the words in string based on a character
s1 = "Where are you?"
print(s1.split())
print(s1.split("r"))

print(s1.count('e'))


#* replace()
s1="where are you?"
print(s1.replace('r', '&&'))

# swapcase()-->to convert capital to small and small to capital at a time
s1="HEY there"
print(s1.swapcase())

# ! title()--> to write the string in formayt of title
s1='never giveUP'
print(s1.title())

# *CAPITALIZE-->1st cchar of string will be converted to capital
s1='never giveUP'
print(s1.capitalize())

# *join the strings s1='hello"
s2='world'
print(s1+s2)

s1='''
how are you
iam fine
hey there
'''
spliines()--> used to split the string  based on lines
print(s1.splitlines())


#! Find-->to find the index based on a charachter
s1="hello  world"
print(s1.find('z'))
print(s1.index('z'))

# *Join()-->
l1=["hey", "there"]
print(" ".join(l1))
print("$".join(l1))


s1="welcome to all"
 *print(s1.endswith('l'))
 *print(s1.startswith('w'))

s1="67"
print(type(s1))
print(s1.isdigit())

#* print the string in reverse manner
s1="welcome to all"
print(s1[::-1])

# !-->eg:1
#? wap to find the number of lower case letters
s1="HEY there you  aRE"
for i in s1:
   if i.islower():
        count+=1
print("the total num of lower case letters: ",count         
                                                                                                                            
# !--->eg:2  r-->$
s1='restarter'
S1="IMAGIN"
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst, "$")
       print(fst+txt)




# ! ------------>Eg:3

s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
s1 = s1.strip()

chracters = len(s1)
print(chracters)

words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))


space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)













