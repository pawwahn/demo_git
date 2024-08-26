l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = [i**2 for i in l if i%2==0]
print(k)

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = ['even' if i%2 == 0 else 'odd' for i in l]
print(k)

m = [i*3 if i%2 == 0 else i%3 for i in l]
print(m)

