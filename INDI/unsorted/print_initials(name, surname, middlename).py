def print_initials(name, surname, middlename):
    for i in name:
        name=name[0].upper()+"."
    for j in surname:
        surmame=surname[0].upper()+surname[1:].lower()
    for j in surname:
         middlename = middlename[0].upper()+"."
    text=surmame+" "+name+middlename
    print(text)

name=input()
surname=input()
middlename=input()
print_initials(name, surname, middlename)
