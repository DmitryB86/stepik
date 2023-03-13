def create_actor(**kwargs):
    d_base = {'name': 'Райан', 'surname': 'Рейнольдс','age': 46, }
    for k,v in kwargs.items():

            d_base[k]=v

    return d_base

print(create_actor(name='Jack', age=20))
