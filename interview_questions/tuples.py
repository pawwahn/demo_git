tup = ()
print(tup,type(tup))

#tup[0] = 'a'    #TypeError: 'tuple' object does not support item
#print(tup)

tup1 = ('a','b','c')
ind = tup1.index('b')
print(ind)
print(tup1)

tup2 = (10,20,30)
tup2 = tup1 + tup2
print(tup2)
print(tup2.__contains__('c'))