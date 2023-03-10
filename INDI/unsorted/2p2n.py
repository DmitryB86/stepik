# n=int(input())
n=5
count=0
cnt=[]
# 10...20     11, 13, 17, 19....1,3,5,67
for i in range(n,2*n):
    if i%2!=0 and i%5!=0 or i**0.5 is not int or i==2 or i==5:
        count+=1
        cnt.append(i)
print(count)
print(cnt)
