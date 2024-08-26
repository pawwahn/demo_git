'''
A set is a collection of unique elements.
Sets are unordered, meaning that the elements do not have a specific order, and they are not indexed.
Sets are useful for storing collections of unique items and for performing mathematical set operations
like union, intersection, and difference.
'''

st1 = {1, 2, 3, 4, 5, 1, 3}
print(st1)

st2 = {10, 20, 30, 4}
print(st2)

#st3 = st1.add(st2) #unhashable type : set error
#print(st3)

st1.add(10)
print(st1)

#st1.remove(20)  #KeyError as 20 is not present
#print(st1)

st1.discard(100)    #Discard does not throw any error even if the key is not present
print(st1)
print("=========")

popped_element = st1.pop()
print(popped_element)

