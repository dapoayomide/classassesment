'''
for x in range(1500,2701):
    if x%5==0 and x%7==0:
        print(x)
'''

'''
guess = int(input('guess a number between 1 and 9' ))
for x in guess:
if guess != range(1,9):
    print(t)
'''
'''
my_name = ("oladapo")
print(my_name.split("d"))
'''
'''
i = 1
while i < 11:
    print(i)
    if i==10:
        break
    i+=1
'''
'''
fruits = ["apple", "banana", "cherry"]
for f in fruits :
    print(f)
    if f=="banana":
        break
'''
'''
fruits = ["apple", "banana", "cherry"]
for f in fruits :
    if f== "banana":
        break
print(f)
'''
'''
numbers = [5, 12, 7, 15, 17, 20, 29]
new_list = []
for x in numbers :
    if (x > 10 and x % 2 == 0):
       new_list.append(x)
    else:
         is_prime = True
    for i in range(2, int(x ** 0.5) + 1):
       if x % i == 0:
        is_prime = False
        break
    if is_prime:
      new_list.append(x)
print(new_list)
'''
'''
x = input("enter number here ")

if x.isalpha():
    print('That is not a diigit')
elif x.isdigit():
    print(int(x)**2)
    break
else:
'''
'''
squares = []
for i in range(11):
    squares.append(i * i)
print(i)
'''
import os

os.rename("practice","new_name.py")
 