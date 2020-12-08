# sets
# unordered collections of UNIQUE elements

# create set
myset = set()
print(myset)

# add 1 to set
myset.add(1)
print(myset)

# add another object
myset.add(2)
print(myset)

# add 2 again (does not work as it's added already -> unique values)
myset.add(2)
print(myset)

# what is this useful for?
# having a list with repeating values
mylist = [1,1,1,1,2,2,2,3,3,3,]
print(mylist)

# can cast set() on mylist to get each unique value once
setlist = set(mylist)
print(setlist)
print(mylist)