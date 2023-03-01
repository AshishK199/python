import os

def main():
    file_name = 'student_comma.dat'
    if os.path.exists(file_name):
        with open(file_name) as file:
            for each_line in file:
                print(each_line)
                # each_line = each_line.strip()
                # each_line = each_line.split(';')
                # print('Name {} Area {} '.format(each_line[1],each_line[5]))
if __name__ == '__main__':
    main()