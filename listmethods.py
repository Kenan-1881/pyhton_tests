numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.insert(5, -1)
print(numbers)

print(len(numbers))

for item in numbers:
    print(item)

numbers = range(5, 10)
for number in numbers:
    print(number)
    
numbers = range(5, 10,2)
for number in numbers:
    print(number)