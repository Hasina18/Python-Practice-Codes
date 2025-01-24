'''
Features of list
1.In list we can store Homogenous as well as Heterogenous Type of data.
2.IN list we can store duplicate values.
3.List is an ordered collection of data:Order of insertion
will remain same as it is in the output.
4.List are Mutable: Once we declare the list we can modify.
'''
li1 = [10,20,30,40,True,"Kodnest",20]
print(li1,type(li1))

# Acessing specific element
print(li1[0])

# append(): Will add element at the end of the list

li1.append(300)
print(li1)
#insert(index,element):inserts an ele.at specified index

li1.insert(1,15)
print(li1)
#remove(ele):Removes the first occurence of specified elements

li1.remove(20)
print(li1)
#in and not in Operator:
print(2000 in li1)#false
print('Kodnest' in li1)#True
#pop():without argument will delete and return  last ele, from list
removed=li1.pop()
print(removed)#ele
print(li1)# [10,20,30,40,True,"Kodnest",20]
#pop(index):with argument will delete the ele. at specified index
removed_ele=li1.pop(4)
print(removed_ele)
print(li1)
#del keyword: will remove the element at specified index
# pop will return removed element.pop is builtin function
#del wont return removed element.del is a keyword
#functions will reeturn the value not the keyword
#li1.pop(1)
del li1[1]
print(li1)
del li1
print(li1) #Error:name'li1' is not defined