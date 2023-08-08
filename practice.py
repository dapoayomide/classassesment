#list comprehension
'''
sum = [1 ,2 , 3 , 4 , 5 , 6]
new = []
comp =[x for x in sum if x%2==0]
new = [x for x in sum if x%3==0]
print(comp)
print(new)

#set comprehension
set = {"hello" , "world"}
comp ={x for x in set if "world" in set}
print(comp)

#dictionary comprehension
dict = {12 : "new"}
for key , value in dict.items():
    print(f'index = {key} , value = {value}')

#enumerate a list 
the_list = range(10)
new_list = [i + x  for i,x in enumerate(the_list)] 
#enumerating a list loops through a list and provides the index of the items in the list
print(new_list)
#this code loops through the values of the lists and adds them to their corresponding indexes

#Ternary assignment
the_list = ['even' if i % 2 == 0 else 'odd' for i in range(16)]
print(the_list)


#functions
def new_function(food):#(a)parameter
    for x in food :
        print(x)
fruits = ["banana" , "pine" ,"apple"] 
new_function(fruits)#arguement

def math_func(x):
    return 5 * x
print(math_func(3))
math_func(4)

#modules 
'''
stack = [1 , 2 , 3 , 4]
x = stack.pop()
print(x)
print(stack)
