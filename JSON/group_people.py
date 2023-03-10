import json

with open('group_people.json') as f:
    data = json.load(f)
    id_rez =0
    count_rez=0
    for element in data:
        id_el = element['id_group']
        # print(f' ID of group: {id_el}', type(id_el))
        count = 0
        for women in element['people']:
            if women['gender']=='Female' and women['year']>1977:
                count+=1
        if count>count_rez:
            count_rez=count
            id_rez=id_el
        # print(f'Quantity of women above 1977:{count}')
    print(id_rez, count_rez)