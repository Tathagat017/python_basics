tuple1 = (11, [22, 33], 44, 55)


list_inside_tuple = list(tuple1[1])
list_inside_tuple[0] = 222


modified_tuple = (tuple1[0], list_inside_tuple, tuple1[2], tuple1[3])

print("tuple1:", modified_tuple)
