# s=input()
s='abcdebcfaghi'
lenS=len(s)
for i in s:
    if s.count(i)==1:
        print(i)
        break
    # print(i, s.count(i), s.index(i))