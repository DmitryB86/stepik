
file = open('numbers.txt')

rows = file.readlines()
count_triple = 0
summ_double = 0
for row in rows:
    if len(row.strip()) == 3:
        count_triple += 1
    if len(row.strip())==2:
        summ_double+=int(row.strip())

print(f'{count_triple},{summ_double}')