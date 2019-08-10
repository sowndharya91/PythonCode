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

#Method3
#descring order of a list :


n = [ 7, 9, 8, 4,31, 1,3, 2, 5, 6]

print(len(n))
for i in range(len(n)):
    for j in range(len(n)):
        print(i,j)
        if n[i] > n[j]:
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
#        print(n)

print("sorted list", n)
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
#Dict Comprehension
"""
item = {n: n*2 for n in range(10)}
print(item)
"""


# Function to check if x is power of 2
"""
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        print(n)
        if (n % 2 != 0):
            return False
        n=n / 2

    return True


# Driver code
if (isPowerOfTwo(128)):
    print('Yes')
else:
    print('No')
if (isPowerOfTwo(64)):
    print('Yes')
else:
    print('No')

"""

#Fibonacci code
#0 1 1 2 3 5
"""
get_max = int(input("enter the num"))
start = 0
next = 1
while(start <= get_max):
    print(start)
    temp = start
    start = start + next
    next = temp
"""
#List reverse
"""
#Method 1
lis =[1, 2, 3, 4, 5, 6, 7, 8,9]
for i in range(0, len(lis) // 2):
    lis[i], lis[len(lis) -1 -i] = lis[len(lis) -1 -i], lis[i]
    print( lis[i], lis[len(lis) -1 -i])
print(lis)

#Method2
lis = [4,7,8,9]
lis.reverse()
print(lis)

#Method3
print(lis[::-1])

#Method4
lis =[1, 2, 3, 4, 5, 6, 7, 8,9]
lis1 = []
print(len(lis))
for i in range(len(lis)-1,-1,-1):
    lis1.append(lis[i])

print("lis1 is ",lis1)
"""

#print max and min of a numbers thrugh classes:
"""
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        print(arg)
        if test(arg, res):
            print(res,arg)
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print (minmax(grtrthan,4, 2, 5, 6, 3))
"""

#binary to decimal:
#Method1
"""
num = int(input("enter the num"))

dec = 0
p = 0
i = 1

while (num > 0):
    p = num % 10
    r = p * i
    dec = dec + r
    i = (i * 2)
    num = num // 10

print(dec)
"""
#Method2
#Needs to implement by me

#Inceremnet the ip address:
"""
def incr_ip(ip,no_of_incr):
    print(ip)
    ip_list=ip.split(".")
    a=int(ip_list[0])
    b=int(ip_list[1])
    c=int(ip_list[2])
    d=int(ip_list[3])
    for i in range(0,no_of_incr):
        d+=1
        if d>255:
            d=0
            c+=1
        if c>255:
            c=0
            b+=1
        if b>255:
            b=0
            a+=1
        if a>255:
            a-=1
            print("cannpot inceremnt the ip")
        print(a,".",b,".",c,".",d)

print(incr_ip("256.255.255.255",10))
"""

#decimacl to binary
"""
numb=10
binary=''
while (numb):
    print(numb,binary)
    if (numb % 2 == 0):
        binary+='0'
    else:
        binary+='1'
    numb=numb // 2


binary = ''.join(reversed(binary))
print(binary)
"""


#check for a prime num in the range:
"""
for x in range(3,50):

    for y in range(2,x):
        if x % y ==0:
            break
    else:
        print(x)


a=[x for x in range(3,50) if all(x%y !=0 for y in range (2,x))]
print(a)

"""

#Count the number of characters
"""
c=dict()
str = "ergeg"
for i in str:
    if i in c.keys():
        c[i]=c[i] + 1
    else:
        c[i]=1

print(c)
"""
#Enumerete
"""
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(list(enumerate(color)))
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
"""

#To get n lines from a file:
###Method1
"""
with open("D:\HCL WORKING\sowndharya\PYTHON\python progs\python programes2 _file_op.txt") as myfile:
    head = [next(myfile) for x in range(3)]
print (head)

###Method2
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('D:\HCL WORKING\sowndharya\PYTHON\python progs\python programes2 _file_op.txt', 3)

###Method3
#easy method:

file2=open("D:\HCL WORKING\sowndharya\PYTHON\python progs\python programes2 _file_op.txt",'r')
line=file2.readline()
n= 4
while(n>0):
    print("line is ",line)
    line=file2.readline()
    n = n - 1
file2.close()

"""
