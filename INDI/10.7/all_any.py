# s = 'acquaintance disAgree'
# check = [('a' in word) for word in s.lower().split()]
#
#
# print(all(check))
#
# # for i in s.split():
# #     print('a' in i)
s = input()
check = [(word.endswith('ought')) for word in s.lower().split()]
print(any(check))