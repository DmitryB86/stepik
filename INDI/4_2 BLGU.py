

def check_in(text:str, NameClass):
    list_value = []
    person_list = [i for i in NameClass.__dict__]

    for word in text.split():
        if word.lower() in person_list:
            list_value.append((f'{word}-YES'))
        else:
            list_value.append((f'{word}-NO'))
    return list_value

class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


text = 'NAME GeNdEr work hobby'
for couple in check_in(text,Person):
    print(couple)
# print(check_in(text,Person))