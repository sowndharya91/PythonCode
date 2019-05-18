#Remove duplicates from list or print unique elements in the list
"""
list1 = [1,2,3,1,2,896875,9,9,9,853,1,2,3,4]
list2 = []

for i in list1:
  if i not in list2:
      list2.append(i)


print(list2)

"""
#Fetch the last value in list
##########
##Method1
"""
list1 = [6,"red","blue",5,8,9]
print(list1[-1])
"""
#Print number from 1 to 10 and reverse
##Method1 -  using for loop
"""
for i in range(1,11):
    print(i)
#code2 - using while loop
i = 1
while i <= 10:
    print(i)
    i+=1
else:
     print("loop exited")
##Method2 - reverse using for loop   

for i in range(10,0,-1):
    print(i)
"""

#Find the length of the string without using length cmd
#Method1
"""
x = "sowndharya"
i = 0
for len in x:
    i += 1
print("length of the string is %d",i)
#Method2 - using while loop
j = 0
while x[j:]:
    j+=1
    print(x[j:])

print(x[10:])
print("length of the string using while loop is %d", j)
#Method3 - using join and count
a = 'py'
print(a.join(x))
m = a.join(x)
print(m.count(a))
print(a.join(x).count(a) + 1)

"""

#string reverse
"""
x = "venkat"
#Method1
print(x[::-1])
#Method2
print("".join(reversed(x)))
#Method3
y = ""
for i in range(len(x)-1,-1,-1):
    y = y + x[i]

print(y)
#Method4
m = ""
for i in x:
    m = i + m
    print (m)

print(m)

"""
#Find the number is palindrome or not
"""
x = input("Ente153r the number\n")

temp = x
y = 0

while x>0:
    n = x%10
    y  = n + y*10
    x = x/10
if temp == y:
    print("the input is palindorme")
else:
    print("the input is not palindrome")
"""
#set a string and need to print the incrment of each character
"""
My_name = "sowndharya"
My_name_char_inc = ""
print()
for i in My_name:
    c = ord(i)
    c = c + 1
    c = chr(c)
    My_name_char_inc = My_name_char_inc + c

print("Incrmented each character \"{}\"".format(My_name_char_inc))
"""
#Return all the characters after the pattern "help" from the string "help is here"
"""
My_str = "help is here"
import re
My_str = re.match("help(.*)",My_str)
print(My_str.group(1))"""
#Return the character index of the last occurence of l in  "hello world"
"""a = "hello world"
print(a.rfind("l"))
"""
#Find the index of apr in the below list
 #set months {jan feb apr may june aug}
"""
Months = ["jan", "feb", "apr", "may", "june", "aug"]
print(Months.index("apr"))
"""
#Arrange the integer list in descending and ascending order
#****Using built in method--------------
"""
list1 = [1,2,5,6,89,2,4,4,1]
list1.sort()
print(list1)
list_asce = sorted(list1)
print(list_asce)
list_desce = sorted(list1,reverse=1)
print(list_desce)
list1.sort(reverse=1)
print(list1)

#------------Using logic------------
list1 = [1,2,5,6,89,2,4,4,1]
for i in range(len(list1)-1,0,-1):
    for j in range(i):
        print(list1[j],list1[j+1],i,j)
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
            
print(list1)
"""


#I will be writing the small programs in Python code using class and methods hereaby.
#inside the class all the small programs will be defined as function
#whenever need to print the output create object at that time
class Python_code:

    #script to print unique elements in a list [1 2 3 4 5 1 3 5]
    """
    #Method 1
    def print_unique_no_list(self,*nums):
        get_list = nums
        new_list = []
        print(len(get_list))
        for x in range(len(get_list)):
            count = 0
            for y in range(len(get_list)):
                print(get_list[x], get_list[y], x, y)
                if x != y:
                    if get_list[x] == get_list[y]:
                        count +=1


            if count == 0:
                new_list.append(get_list[x])

        return new_list
    #Method2
    def print_unique_no_list(self,*nums):
        get_list = nums
        new_list = []
        print(len(get_list))
        for i in range(len(get_list)):
            val = get_list[i]
            count = get_list.count(val)
            print(count)
            if count == 1:
                new_list.append(val)

        return new_list
"""

#Objects === script to print unique elements in a list [1 2 3 4 5 1 3 5]
"""
x = Python_code()
value= x.print_unique_no_list(1, 2, 3, 4, 5, 1 ,3, 5,9,8,1,8)
print("value is ", value)
"""



#get the string and make it to form dict with count of occurences
"""
def len_of_string(a):
    d = {}
    for i in a:
        if i in d.keys():
            d[i] += 1

        else:
            d.update({i: 1})
    print(d)
len_of_string("google.com")
"""
#Find the maximum of number in dict using value
"""stats = {'a':1000, 'b':3000, 'c': 100}
print max(stats)[0]
inverse = [(value, key) for key, value in stats.items()]
print(inverse)
print max(inverse)[0]
"""

#Write a Python program to get a string from a given
# string where all occurrences of its first char have
# been changed to '$', except the first char itself.
"""
def string(a):
    b = a[0]
    for i in range(1, len(a)):
        if a[i] == b:
            a = a[:i] + "$" + a[i + 1:]
            print(a[i+1:])
    print(a)


string("sowndharya.s")
"""

#Python: Swap comma and dot in a string
"""
from string import maketrans
str1 = "32.054,23"
aaa = maketrans(",.",".,")
translated = str1.translate(aaa)
print(translated)
"""
#to print the repated letters
"""
string = "sowndharyas"
for i in range(0,len(string)):
    a=string[i]
    print(a)
    count=1
    for i in range(i+1,len(string)):
        if a == string[i]:
            count += 1
    if count > 1:
        print(a,"is",count)
"""
#for print two times at a same time in list:
"""
l1=[1, 2, 3]
l2=[4, 5, 6]
d=dict(zip(l1,l2))
print(d)
r=zip(l1,l2)
print(r)
for x,y in d.items():
    print x,y
"""
#generator expression for power of 2
"""
x = (y ** 2 for y in range(1,11))
print(x)
print(next(x))
print(next(x))
print("hi")
for i in x:
    print(i)
"""


#how to sort a list with dictionary as variables.Sort should be based on dictionary value.
"""
#Method1
from operator import itemgetter
a = {'b':2},{'b':1},{'b':5},{'b':4}

print(sorted(a,key=itemgetter('b')))
print(sorted(a,key=itemgetter('b'),reverse=True))

#Method2
a = [{'b': 2}, {'b': 1}, {'b' : 5}, {'b' : 4}]
b = []
print(a)

for i in range(len(a)):
    for k, value in a[i].items():
        b.append(value)
        b.sort()
del a
a = []
print(b)
for j in range(len(b)):
    a.append({'b':b[j]})
print(a)

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(x.items())
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(operator.itemgetter(1))
print(sorted_x)
"""
#reverse a list with the given sub interval
"""
def rev_list(list,n):
    for i in range(0,len(list),n):
        print(n,i)
        list[i:i+n]=list[i:i+n][::-1]
    return list

list=[1,2,3,4,5,6,7,8,9,10,11,12]
print(list[10:20][::-1])
print(rev_list(list,5))
"""