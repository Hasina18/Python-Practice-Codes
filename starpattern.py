rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*",end='')
    print()

print()
for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print()
print()
for i in range(rows):
    for j in range(i,rows):
        print("*",end=' ')
    print()
print()
for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end=' ')
    print()
print()

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,rows-1):
        print(' ',end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i+1):
        print(' ',end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    print()
print()

for i in range(rows):
    for j in range(i,rows):
        print(' ',end="")
    for j in range(i): # o remove extra coulmn is removed
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i+1):
        print(' ',end="")
    for j in range(i,rows):
        print("*",end="")
    for j in range(i,rows-1):
        print("*",end="")
    print()


