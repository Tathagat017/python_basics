def two_sum(nums, target):
    complement_map = {}  

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i

    return []


input_nums = [2, 7, 11, 15]
input_target = 9
result = two_sum(input_nums, input_target)
print(result)
