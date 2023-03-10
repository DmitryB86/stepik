# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
#
# subject_marks = sorted(subject_marks, key= lambda x: x[1])
# for i in subject_marks:
#     print(*i)

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# subject_marks = sorted(subject_marks, key = lambda x: x[1], reverse=True)
# for i in subject_marks:
#     print(*i)

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# subject_marks = sorted(subject_marks, key = lambda x:(-x[1], x[0]))
# # subject_marks = sorted(subject_marks, key = lambda x:x[0])
# for i in subject_marks:
#     print(*i)

# heroes = {
#     'Spider-Man': 80,
#     'Batman': 65,
#     'Superman': 85,
#     'Wonder Woman': 70,
#     'Flash': 70,
#     'Iron Man': 65,
#     'Thor': 90,
#     'Aquaman': 65,
#     'Captain America': 65,
#     'Hulk': 87,
# }
# for i in sorted(heroes.items(), key = lambda pare: (pare[1], pare[0])):
#     print(i)

models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]