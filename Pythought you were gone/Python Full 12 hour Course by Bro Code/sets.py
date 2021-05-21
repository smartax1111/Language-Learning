# set = collection which is unorder, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)

dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for x in utensils:
    print(x)