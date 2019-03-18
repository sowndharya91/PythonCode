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
#code1
"""
list1 = [6,"red","blue",5,8,9]
print(list1[-1])
"""
#Print number from 1 to 10 and reverse
#code1 -  using for loop
"""
for i in range(1,11):
    print(i)
#code2 - using while loop
i = 1
while i <= 10:
    print(i)
    i+=1
else:
#Code1 - reverse using for loop    print("loop exited")

for i in range(10,0,-1):
    print(i)
"""

#Find the length of the string without using length cmd
#code1
"""
x = "sowndharya"
i = 0
for len in x:
    i += 1
print("length of the string is %d",i)
#code2 - using while loop
j = 0
while x[j:]:
    j+=1
    print(x[j:])

print(x[10:])
print("length of the string using while loop is %d", j)
#code3 - using join and count
a = 'py'
print(a.join(x))
m = a.join(x)
print(m.count(a))
print(a.join(x).count(a) + 1)

"""

#string reverse
