# list = used to store multiple items in a single variable
print("------------------")
food = ["pizza","hamburger","hotdog","spaghetti"]
for x in food:
    print(x)
print("------------------")

# replacing hard code
food[0] = "sushi"
for x in food:
    print(x)
print("------------------")

# .append
food.append("ice cream")
for x in food:
    print(x)
print("------------------")

# .remove
food.remove("hotdog")
for x in food:
    print(x)
print("------------------")

# .pop
food.pop()
for x in food:
    print(x)
print("------------------")

# .insert
food.insert(0, "cake")
for x in food:
    print(x)
print("------------------")

# .sort
food.sort()
for x in food:
    print(x)
print("------------------")

# .clear
food.clear()
for x in food:
    print(x)