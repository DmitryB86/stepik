# 4
# 1 4 6 2
# 5
# 5 1 5 7 9

boys = [1, 4, 6, 2]
girls = [5, 1, 5, 7, 9]
couples = 0
boys.sort(reverse=True)
girls.sort(reverse=True)
i = 0
while len(boys) != 0 or len(girls) != 0:
    # for b in range(0,len(boys)+1):
    #     for g in range(0,len(girls)+1):
    if abs(boys[i] - girls[i]) > 1:
        if boys[i] > girls[i]:
            boys.remove(boys[i])
        else:
            girls.remove(girls[i])
    else:
        couples += 1
        boys.remove(boys[i])
        girls.remove(girls[i])
    i+=1
print(couples)
