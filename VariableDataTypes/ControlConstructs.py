'''
1.Conditional: if-else, if-elif
2.Looping: for, while
3.jumping: break, continue, pass
'''
def checkAge(age):
    if(age>18):
        print("Age is greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

def checkEligible(age):
    if (age < 18):
        print("child")
    elif (age > 18 and age < 65):
        print('Adult')
    elif(age > 65):
        print('Senoir Citizen')
checkEligible(int(input('Enter age')))