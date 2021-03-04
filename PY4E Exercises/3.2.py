"""
Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:

"""
def numcheck(i):
    try:
        int(i)
    except:
        print('Please enter a number')
        exit()

def hourly_pay(hours, rate):
    if hours > 40:
        return ((40 * rate) + ((hours - 40) * (1.5 * rate)))       
    return hours * rate

def main():
    a = input("Enter Hours: ")
    numcheck(a)
    b = input("Enter Rate: ")
    numcheck(b)
    print(hourly_pay(int(a), int(b)))

main()
