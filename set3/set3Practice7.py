def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())

        with open(output_file, 'w') as file:
            file.write(f"Number of words: {word_count}")

        print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print("File not found.")


input_file_name = "input.txt"
output_file_name = "output.txt"
count_words_in_file(input_file_name, output_file_name)
