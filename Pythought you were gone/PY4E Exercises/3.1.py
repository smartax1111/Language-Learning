"""
Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
"""

def hourly_pay(hours = int(input('Enter Hours:')), rate = int(input('Enter Rate: '))):
    if hours > 40:
        return ((40 * rate) + ((hours - 40) * (1.5 * rate)))
    return hours * rate

print(str(hourly_pay()))