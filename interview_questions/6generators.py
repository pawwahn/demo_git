'''Generators in Python are a special type of iterator, implemented with a function that uses
the yield statement to produce a series of values lazily, meaning they generate values
one at a time and only as needed.
This is useful for handling large datasets or streams of data where it is impractical to load
everything into memory at once.'''

#print(__doc__)

#Basic Generator
def  my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
#print(gen)

print(next(gen))    #1
print(next(gen))    #2

''' or '''
for value in gen:
    print(value)    #3 ; value starts from 3 but not from 1 because in the same execution, there was 2 next

