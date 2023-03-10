n=int(input())
qubesINrow = 0
level = 0
QUBESsumm=0
while True:
    level+=1
    qubesINrow+=level
    QUBESsumm+=qubesINrow
    # print(level, qubesINrow)
    if QUBESsumm>n:
        break
if n==1:
    print("1")
else:
    print(level-1)
