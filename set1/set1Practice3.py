numbers_list = list(range(1, 11))
print(numbers_list)

numbers_list.append(20)
print(numbers_list)

if 3 in numbers_list:
    numbers_list.remove(3)
print(numbers_list)

numbers_list.sort()
print(numbers_list)
