def number(num):
    result=0
    for no in num:
        result^=no //exclusive or operator is used to eliminate same values un array
    return result //returns 
num=[1,2,2,1,3,3,4]
print(number(num)) 
