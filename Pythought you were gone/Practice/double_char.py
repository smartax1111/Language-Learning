"""
Given a string, return a string where for every char in the original, there are two chars
"""

def double_char(string):
    full_string = ''
    for x in range(0, len(string)):
        full_string += string[x]*2
    return full_string

print(str(double_char('Hello')))