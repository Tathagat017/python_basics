def find_missing_number(nums):
    n = len(nums)
    total_sum = (n * (n + 1)) // 2
    array_sum = sum(nums)
    missing_number = total_sum - array_sum
    return missing_number


input_array = [3, 0, 1]
output = find_missing_number(input_array)
print(output)
