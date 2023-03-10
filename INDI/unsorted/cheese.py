s=input()
s=s.lower().replace(" ","")
glas='уеыаоэяию'
sogl='цкнгшщзхъждлрпвфчсмть'
# print(s)\
glascount=0

for i in s:
    for j in glas:
        if i==j:
            glascount+=1
soglcount=len(s)-glascount
print(glascount)
print(soglcount)
