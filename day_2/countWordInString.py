import re
myString = "This is a my\nstring with\tmultiple space tabs and lines as delimimeters"
words = re.split(r'\s+', myString)

numWords = len(words)
print("The number of words in the string is : ", numWords)