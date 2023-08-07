sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys_to_extract = ["name", "salary"]
extracted_dict = {key: sample_dict[key] for key in keys_to_extract}

print(extracted_dict)
