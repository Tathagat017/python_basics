def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


input_num = 16
output = is_power_of_two(input_num)
print(output)
