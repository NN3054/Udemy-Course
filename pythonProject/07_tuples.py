# tuples
# similar to lists but immutable

# tuple
t = (1, 2, 3)

# list
l = [1, 2, 3]

# check types
print(type(t))
print(type(l))

# check length
print(len(t))

# can contain different types
t = ('one', 2)

# works with indexing
print(t[0])

# index method
t = ('a', 'a', 'b')

# counts how often "a" appears in tuple t
print(t.count('a'))

# prints first index-occurrence of "a" in tuple t
print(t.index('a'))
# prints first index-occurrence of "b" in tuple t
print(t.index('b'))

# immutability
print(t)
print(l)

# works because of mutability
l[0] = 'NEW'
print(l)

# does not work because of immutability
t[0] = 'NEW'

# why should I use tuples?
# when passing around objects and I need to make sure they do not accidentally get changed (data-integrity)
