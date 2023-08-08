'''
def reverse_words(x,y):
    return [x,y[::-1]]

print(reverse_words("they" , "cloned"))
'''

def grade_average(a,b,c,d):
    for x in a,b,c,d:
        if x >= 90:
            print("A")
        elif x >=80:
            print("B")
        elif x >= 70 :
            print("c")
        elif x >= 60:
            print("D")
        else:
            print("F")
    
grade_average(90,67,24,78)




