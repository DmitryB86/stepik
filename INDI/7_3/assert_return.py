def get_domain_name(url):
    # Строка url может начинаться с протоколов
# http://  https:// или с www. URL,
# начинающиеся с протоколов http://  https://, могут также содержать www.
    if '//' in url:
        url = url[url.find('//'):]
    return url

# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')