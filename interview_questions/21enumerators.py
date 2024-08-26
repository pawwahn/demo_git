ls = ['apple', 'banana', 'cherry']
print(enumerate(ls))   #enumerate object
for i, j in enumerate(ls):
    print(i,j)

# how to give starting value to the index
print("\nnext concept")
for i, j in enumerate(ls, start=10):
    print(i,j)

print('\nupdating items in a list')
for i, j in enumerate(ls):
    ls[i] = j.upper()
print(ls)
