def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return 1
    return - 1    

courses = ['history', 'math', 'PE']

index = find_index(courses, 'PE')
print(index)