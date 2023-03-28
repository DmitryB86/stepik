l = [i for i in range(1,5)]
print(l)
l.clear()
if len(l)==0:
    print('Emptey')
    print(l is None)
    l.append(12)
print(l[-1])