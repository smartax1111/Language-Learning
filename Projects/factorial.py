# import math
# print(math.factorial(int(input("Input the number you want to use in a factorial:"))))
# easy way 

factorial_n = 1
for factorial in range(1, int(input("What number would you like to use for factorial: ")) + 1): factorial_n *= factorial
print(factorial_n)

