# concept 1
l = [i for i in range(10) if i % 2 == 0]
print(l)

# concept 2
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''
l1 = []
for mat in matrix:
    for m in mat:
        l1.append(m)
print(l1)
'''

l2 = [m for mat in matrix for m in mat]
print(l2)
