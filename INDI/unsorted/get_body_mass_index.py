def get_body_mass_index(w,h):
    index=w/((h/100)**2)
    if index<18.5:
        print('Недостаточная масса тела')
    elif 18.5<=index<=25:
        print('Норма')
    else:
        print('Избыточная масса тела')
w,h = map(int,input().split())
get_body_mass_index(w,h)