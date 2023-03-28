# Two one One SIX two thrEE four four five SIX six one two three four five six ONE

s = 'Two one One SIX two thrEE four four five SIX six one two three four five six ONE'
s1 = list(s.split()) #читаем входной список
s2 = []
s3 = []
for i in s.split():
    if i.lower() not in s2:
        s2.append(i.lower())
        s3.append(i)

print(s2)
print(s3)