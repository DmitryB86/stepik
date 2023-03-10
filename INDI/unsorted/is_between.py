def is_between(a,b,c):
    if b<=a<=c or c<=a<=b:
        print('True')
    else:
        print('False')

ap,bp,cp = map(int, input().split())
is_between(ap,bp,cp)