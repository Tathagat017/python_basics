def is_anagram(word1, word2):
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())

    return sorted_word1 == sorted_word2

# Test the function with the given input
input_word1 = "cinema"
input_word2 = "iceman"
output = is_anagram(input_word1, input_word2)
print(output)
