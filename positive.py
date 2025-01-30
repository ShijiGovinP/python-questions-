def positive(n):
    total = 0  
    for i in range(1, n):  
        if n % i == 0:  // n value divisible by i gets a remainder
            total=total+i // add
    return total == n  // returns the  total value equals to given n value
num = int(input("Enter a number: "))  
if positive(num):  
    print("is a perfect number",num)  
else:  
    print( "is not a perfect number",num)
