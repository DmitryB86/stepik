# def shift_letter(s:str, n:int)-> str:
#     '''
#     Функция сдвигает символ letter на shift позиций
#     '''
#     return chr(((ord(s) - 97 + n) % 26) + 97)
#
# print(shift_letter('b', -3))

def caesar_cipher(s:str,n:int)->str:
    new_s = ''
    for i in s:
        if i.isalpha():
            new_s = new_s+chr(((ord(i) - 97 + n) % 26) + 97)
        else:
            new_s+=i
    return new_s


print(caesar_cipher('leave out all the rest', -1))   #'kdzud nts zkk sgd qdrs'