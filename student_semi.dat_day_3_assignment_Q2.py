import os
import datetime

number_of_words = 0
number_of_lines = 0
number_of_characters = 0

file_path = 'C:/Users/ashish.kumar1/PycharmProjects/pythonProject/student_semi.dat'
modification_time = os.path.getmtime(file_path)
dt_modification = datetime.datetime.fromtimestamp(modification_time)

file_name1 = os.path.basename(file_path)
file_size = os.path.getsize('C:/Users/ashish.kumar1/PycharmProjects/pythonProject/student_semi.dat')

file_name = "student_semi.dat"
if os.path.exists(file_name):
    with open(file_name) as file:
        for line in file:
            wordslist = line.split()
            number_of_lines = number_of_lines + 1
            number_of_words = number_of_words + len(wordslist)
            number_of_characters = number_of_characters + sum(len(number_of_words) for number_of_words in wordslist)

    print("File Name is : {}".format(file_name1))
    print("Total number of lines are : {}".format(number_of_lines))
    print("Total number of character are : {}".format(number_of_characters))
    print("File Size is : {}".format(file_size), "bytes")
    print("Modification time is : {}".format(dt_modification))