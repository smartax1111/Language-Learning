"""
a function takes an input 
if the number is divisible by 3 its output is Fizz
If it is divisible by 5 its output is Buzz
If it is divisible by both it prints FizzBuzz
If it is not any of these it will return the number inputted
"""

def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return str(input)

print(fizz_buzz(15))