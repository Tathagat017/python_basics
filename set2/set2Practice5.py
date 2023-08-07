list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result_list = []
for item1, item2 in zip(list1, list2):
    result_list.append(item1 + item2)


if len(list1) > len(list2):
    result_list.extend(list1[len(list2):])
else:
    result_list.extend(list2[len(list1):])

print(result_list)
