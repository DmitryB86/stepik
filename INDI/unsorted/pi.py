import requests

with open('C:\\Users\\Dmitry\\Downloads\\input.txt') as in_f_obj:
	url = in_f_obj.read().strip()

r = requests.get(url)
counter = 0

for line in r.text.splitlines():
	counter += 1

# Цикл выше можно заменить более простой конструкцией
#print(len(r.text.splitlines()))

with open('C:\\Users\\Dmitry\\Downloads\\input.txt', 'w') as out_f_obj:
	out_f_obj.write(str(counter))