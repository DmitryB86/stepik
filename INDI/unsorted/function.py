def modify_list(l):
    # put your python code here
     lz=[]
     for i in l:
        if i%2==0:
            lz.append(i//2)
     return lz

# l = [int(i) in input().split()]
l=[10, 5, 8, 3]
l=modify_list(l)
print(l)