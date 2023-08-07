def climb_stairs(n):
    if n == 0 or n == 1:
        return 1


    first, second = 1, 1

    for _ in range(2, n + 1):
   
        next_step = first + second

     
        first, second = second, next_step

    return second


input_steps = 3
output = climb_stairs(input_steps)
print(output)
