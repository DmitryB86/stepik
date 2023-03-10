# # author (author_id, name_author);
# # genre (genre_id , name_genre);
# # book (book_id, title, author_id, genre_id, price, amount);
# # city (city_id, name_city, days_delivery);
# # client (client_id, name_client, city_id, email, discount);
# # buy (buy_id, buy_description, client_id);
# # buy_book (buy_book_id, buy_id, book_id, amount);
# # step (step_id, name_step);
# # buy_step (buy_step_id, buy_id, step_id, date_step_beg, date_step_end);
#
# # st='buy_step (buy_step_id, buy_id, step_id, date_step_beg, date_step_end);'
n=int(input())
d={}
for i in range(n):
    st=input()

    for i in st.split('\n'):
        # st_value=st[st.index('(')+1:-2].split(',')
        # st_value=st[st.index('(')+1:-2]
        # print(st_value, type(st_value))
        # d={st[:st.index(' ')]:st_value for i in st.split()}

        d[st[:st.index('(')]]=st[st.index('(')+1:st.index(')')]    #d[key]=value
print(d)
for key,value in d.items():
    print(f'SELECT {value} From {key};')

# from pathlib import Path
# import os
# Path('spam') / 'bacon'/ 'egg'
# home_folder= r'G:\PythonProjects'
# # for i in range(10):
# #     os.makedirs(home_folder+fr'\\test\\folder{i}')
# print(Path.cwd(), Path.home(), Path('spam') / 'bacon'/ 'egg',Path.cwd()/Path('spam') / 'bacon'/ 'egg', sep= '\n')
