#  str to integer conversion is not allowed.
x = 'Kod'
print(x,type(x))

# y = int(x)
# print(y,type(y))

# p = float(input('Enter float type data'))
# print(p,type(p))

#bool()
q = ''
print(q,type(q))
q = bool(q)
print(q,type(q))
'''
1.while converting into bool for all non zero values
 we will get True
2.While converting into bool for 0 and empty strings 
we will get false
'''