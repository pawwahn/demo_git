l1 = [1,2,3,4]
l2 = [1,2,3,4]
d = {}
for i,j in zip(l1,l2):
    d[i] = j
print(d)

d.update({10:10})
print(d)