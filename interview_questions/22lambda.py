'''
lambda is annonymous 1 liner function
syntax : lambda arguments : expression
'''

add = lambda a, b: a+b

print(add(2,5))

#maps:
numbers = [1, 2, 3, 4, 5, 6]
sqr = list(map(lambda a: a**2, numbers))
print(sqr)

#filters
numbs = [10, 20, 30, 40, 50, 60]
filt_recs = list(filter(lambda a: a % 2 == 0, numbs))
print(filt_recs)

