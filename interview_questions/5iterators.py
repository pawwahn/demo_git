# Iterators are objects that travers through all the elements in a collections like list, tuple, dict,
# one element at a time when it is called

#dictonary
dct = {'a':10, 'b':20, 'c':30}
iter_dct = iter(dct)
print(next(iter_dct))

#lists
lst = [1,2,3]
iter_lst = iter(lst)

print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))
#print(next(iter_lst)) #StopIteration Error

