def find_single_number(nums):
    num_frequency = {}

    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    for num, frequency in num_frequency.items():
        if frequency == 1:
            return num


input_array = [4, 1, 2, 1, 2]
output = find_single_number(input_array)
print(output)
