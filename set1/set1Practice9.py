def fibonacci_sequence(n):
    sequence = [0, 1]

    if n <= 2:
        return sequence[:n]

    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence

input_n = 5
fibonacci_result = fibonacci_sequence(input_n)
print(f"{fibonacci_result}")
