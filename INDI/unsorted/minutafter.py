cet=12
nec=21

# c=cet//2
# n=nec//2
cc=cet%2
nn=nec%2
ccc=2*((cet+1)%2)
nnn=(nec+1)%2
# print(c,n)
print(cc,nn)
print(ccc,nnn)
print(cet+ccc+nec%2)