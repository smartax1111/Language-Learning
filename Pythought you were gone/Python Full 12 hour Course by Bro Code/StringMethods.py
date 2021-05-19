name = "TJ Uhler"

print("The Length of this string is" + str(len(name)))
print("U is the " + str(name.find("U")) + "th Character")
print("This is what your name looks like with the first capital letter: " + str(name.capitalize()))
print("This is your name with all capital letters: " + str(name.upper()))
print("This is your name with all lowercase letters: " + str(name.lower()))
print("The string is a digit: " + str(name.isdigit()))
print("The string is all letters: " + str(name.isalpha()))
print("There are " + str(name.count("e")) + " e's in the string")
print("We have replaced U with l and this is the result: " + str(name.replace("U", "l")))
print("The string times 10: " + str(name*10))