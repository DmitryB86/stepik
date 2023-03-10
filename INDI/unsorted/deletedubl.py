# s = "abbaca"


st='Two one One SIX two thrEE four four five SIX six one two three four five six ONE'
st_original=[]
st_no_original=[]
print(st.split())

for i in st.split():
    if i in st_original:
        st_original.append(i.lower())
    else:
        st_original.append(i)
        st_no_original.append(i)
print()
print(st_original)
print(st_no_original)
