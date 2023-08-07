
str1 = "PyNaTive"
lower = ''.join(sorted(filter(str.islower, str1)))  
upper = ''.join(sorted(filter(str.isupper, str1))) 

arranged_string = lower + upper
print(arranged_string)
