'''
for control_variable in range()
'''
for j in [10,20,30]:
    print(j+5)
for num in range(1,11):
    print(num)
for num in range(11,21,2):
    print(num,end=" ")
print()
for i in range(5):
    print(i,end=" ")
#WAP to print all even nubers from 1-10
for num in range(1,11):
    if(num % 2 == 0):
        print(num, end = " ")
#While
i = 0
while(i < 0):
    print(i+100)
    i= i+1;   
#WAP to print numbes from 1-10 but if number is 6 then
#skip printing
for i in range(1,11):
    if(i==6):
        continue

    print(i)
# WAP to print numbers from 1-10 but if number is 5 then stop printing
for i in range(1,11):
    if(i == 5):
        break
    print(i)