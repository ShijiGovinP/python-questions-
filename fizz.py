def Fizzbuzz(num):
    result=[] //initializing array
    for i in range(1,num+1): 
        if i%3==0 and i%5==0:
            result.append("FizzBuzz") //appends the string 
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

number=int(input("enter the number:"))
print(Fizzbuzz(number))//prints the result
