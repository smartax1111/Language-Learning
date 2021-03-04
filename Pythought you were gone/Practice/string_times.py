"""
Given a string and a non-negative int n, return a larger string that combines the original string
"""

def string_times(string, iterations):
    return string*iterations 

print(string_times(str(input("text:")), int(input("Iterations:"))))