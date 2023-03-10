def file_read(file_name):
    file = open(file_name, encoding='utf-8')
    print(file.read(file_name))
# file_name = 'grades.txt'
file_read('grades.txt')

# file = open('grades.txt', encoding='utf-8')
# print(file.read())