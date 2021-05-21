# dictionary = A changeable. unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

#capitals.update({'Germany':'Berlin'})
#capitals.pop('China')
#capitals.clear()

print(capitals['Russia'])
print(capitals.get('Russia'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)