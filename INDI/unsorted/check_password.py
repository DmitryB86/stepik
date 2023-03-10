
def check_pass(password):
    # password = input()
    # password = 'asdFG123!@#'
    usl1=0
    usl2=0
    usl3=0
    for i in password:
        if len(password)<10:
            break
        elif i.isdigit():
            usl1+=1
        elif i.isupper():
             usl2+=1
        elif i in "!@#$%*":
            usl3+=1
    if usl1>=3 and usl2>=1 and usl3>=1:
        textout = 'Perfect password'
    else:
        textout = 'Easy peasy'
    print(textout)

passw=input()
check_pass(passw)