# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "TJ Uhler"

first_name = name[:2]
last_name = name[3:]
funky_name = name[::2]
reversed_name = name[::-1]

print(funky_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])