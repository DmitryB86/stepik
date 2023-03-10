a,b = map(int, input().split())
aa=[]
bb=[]
cc=[]
dd=[]
while len(aa)<a:
   aa=list(map(int, input().split()))

while len(bb)<b:
    bb=list(map(int, input().split()))

while len(cc)!=0:
    dd.append(min(cc))
    (aa+bb).remove(min(cc))
print(dd)