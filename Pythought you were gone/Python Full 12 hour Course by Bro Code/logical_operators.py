# logical operators (and,or) = used to check if tow or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("go outside!")


