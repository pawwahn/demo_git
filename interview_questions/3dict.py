l1 = ['a','b','c']
l2 = [1,2,3]

d1 = zip(l1, l2)
print(d1)   #gives zip object
d1 = dict(d1)
print(d1) #{'a': 1, 'b': 2, 'c': 3}

d2 = {'x':10, 'y':20, 'z':30}
d1.update(d2)

print(d1)
print(d2)

print(d2.items())

for k,v in d2.items():
    print(k,v)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

##### valid from 3.9 ####
#merged_dict = dict1 | dict2 # OR operator
#print(merged_dict)   #{'a': 1, 'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2} #python 3.5 and above - unpacking
print(merged_dict)

dict2.pop('c')
print(dict2)

#dict2.pop('m')  #key not found but still does not throws error
#print(dict2)


dict2.popitem()
print(dict2)






