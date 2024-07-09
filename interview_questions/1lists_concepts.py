a = []
print(a)    #empty list

print(type(a))  #<class 'list'>

#print(a.append('a', 'b', 'c')) # append() takes only 1 argument

print(a.append('a')) #None

print(a)    #['a']

print(a.index('a')) #0

new_a = a.append('b')
print(a,new_a)  #['a', 'b'] None
print(new_a)    #None

new_b = a
print(new_b)

a.extend(['pavan','kumar'])
print(a)    #['a', 'b', 'pavan', 'kumar']

a.append(['kota','444'])
print(a)    #['a', 'b', 'pavan', 'kumar', ['kota', '444']]

a.insert(2,'c')
print(a)    #['a', 'b', 'c', 'pavan', 'kumar', ['kota', '444']]
a.reverse()
print(a)
print(a[::-1])


b = [10,20,30]

print(a+b)  #[['kota', '444'], 'kumar', 'pavan', 'c', 'b', 'a', 10, 20, 30]
print(a.__doc__)

print(b[2:3])   #[30]
