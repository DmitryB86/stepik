s = 'californication,can’t stop,dani california,by the way,around the world,dani,Californication,give it away,can’t stop'
# l_s = s.lower().split(',')

ll=[]
for i in s.lower().split(','):
    if not i in ll:
        ll.append(i)
    else:
        ll.append('ДА')
for i in ll:
    if i=='ДА':
        print('ДА')
    else:
        print('НЕТ')