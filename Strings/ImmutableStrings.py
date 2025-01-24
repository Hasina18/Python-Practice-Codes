'''1.Strings are Immutable: Once we declare the string we cannot modify it, if we try to modify
the String it will create new String.
2. If new String does not have any refernce variable the it will 
removed
Python Internally uses String Interning.
 String Interning  is the process of checking string intern pool before creating any new object
5. whenever we want to create new object, Python first will check string
intern pool, whether that ojject already exist or not.
6. When object already exist in the string intern records then 
address of existing object will be reused
'''

# s1 = 'Kodnest'
# s1=s1.upper()
# print(s1)

# s2 = 'K'
# s3 = 'H'
# print(s2,id(s2))
# print(s3,id(s3))
s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))
print(id(s1[0]))
print(id(s2[-1]))

print('s1 Id of H:',id(s1[0]))
print('s2 Id of W:',id(s2[1]))

print('s2 Id of H:',id(s2[1]))
print('s1 Id of W:',id(s1[-1]))

print('s1 Id of l:',id(s1[2]))
print('s2 Id of l:',id(s1[3]))
print('s2 Id of l:',id(s2[3]))