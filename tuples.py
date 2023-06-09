list_1 = ["apple", "banana", "cherry"]
list_2 = tuple(list_1)

print(list_1)
print(list_2)

list_1[0] = 'orange'

print(list_1)
print(list_2)

list_3 = list(list_2)
list_3[0] = 'orange'
list_2 = tuple(list_3)

print(list_1)
print(list_2)