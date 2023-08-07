def is_palindrome(word):
  
    cleaned_word = word.replace(" ", "").lower()
    reversed_word = cleaned_word[::-1]

    if cleaned_word == reversed_word:
        return True
    else:
        return False


input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")
