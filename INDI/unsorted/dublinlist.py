import numpy as np
a = str(input()).split(' ')
a = np.array([int(item) for item in a])
print(a)
# заданный массив: a
# a=np.unique(a)
# last=len(a)
# # a=np.unique(a)
# # last=len(a)
#     #...
# for i in range(last):
#     print(sorted(a[i]), end=' ') # вывод без дубликатов чисел