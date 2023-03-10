import os

def obhod(path, level=1):
    print('Level =', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Idem na dniwe', path+'\\'+i)
            obhod(path+'\\'+i,level+1)
            print('Vozvrat', path)

path = 'G:\\old'
obhod(path)