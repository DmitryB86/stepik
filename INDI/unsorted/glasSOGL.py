s='дед мороз'
glas='йуеыаоэяию'
sogl='цкнгшщзхъждлрпвфчсмть'
glascount=0
soglcount=0
for i in s:
    for j in glas:
        if i==j:
            glascount+=1
    for jj in sogl:
        if i==jj:
            soglcount+=1
print(glascount)
print(soglcount)
