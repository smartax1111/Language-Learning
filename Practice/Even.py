"""Even Numbers between 1-10"""
numberCount = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(str(x))
        numberCount += 1
print('We have ' + str(numberCount) + ' even numbers')