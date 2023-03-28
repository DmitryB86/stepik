with open("animal.txt", 'r', encoding='utf-8') as animal:
    rows = animal.readlines()
    for row in rows:
        print(row)