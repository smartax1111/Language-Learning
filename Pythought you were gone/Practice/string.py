# basic string
msg = "Hello World\n\n"
print(msg)


#escape string
msg2 = "Hello \nWorld\n\n"
print(msg2)


#concatenation strings
msg3 = "you're cute"
msg3Part2 = "hmu"
print(msg3 + "... " + msg3Part2 + "\n\n") #expecting 1 argument --> concatenation


#concatenation with string literals
full_message = msg3 + "... " + msg3Part2
print(full_message + "!\n\n")


#indexes
poem = "Where am I?"
print(poem[0],poem[1],poem[2],poem[3],poem[4],poem[5],poem[6],poem[7],poem[8] + "\n\n")


#slicing strings
print("slicing strings",'"',poem[5:],'"')
print("slicing strings on the negative",'"',poem[:-7],'"',"\n\n")


#slicing strings through a range
print(poem[6:8])

start = 6
print(poem[start:start+2], "\n\n")


#strings are immutable
task = "Subscribe"
print(id(task))

different = task
different = "yes"
print(task, "\n\n")


#length of strings
msg = "pls subscribe"

print("You message was " + str(len(msg)) + " characters long :)")
print("You message was ", len(msg), " characters long :)", "\n\n")#alternative


#nested function practice (extra)
import math
age = 15
print(len(str(id(str(age)) + math. floor(2.6)))) 

#or we can do this to show the steps

age_str = str(age) 
id_age_str = id(age_str)
other = math.floor(2.6)
added = id_age_str + other
added_str = str(added)
len_added_str = len(added_str)
print(len_added_str)






