s = 'abc'
from itertools import permutations
lst = []
for p in permutations(s):
    x = ''.join(p)
    lst.append(x)
print(lst)