# lists

# is defined by [] and objects are seperated by ,
my_list = [1,2,3,'String']

print(len(my_list))

my_list = ['one','two','three']
print(my_list)

# print list with index
print(my_list[0])

# slicing
print(my_list[1:])

another_list = ['four', 'five']

# print both lists
print(my_list + another_list)

# merge lists
new_list = my_list + another_list
print(new_list)

# change list (at index 0)
new_list[0] = 'ONE ALL CAPS'
print(new_list)

# add element to the end of the list
new_list.append('six')
print(new_list)

# removing from the end of a list
new_list.pop()
print(new_list)

# safe item of the end of list after removing
popped_item = new_list.pop()
print(popped_item)
print(new_list)

# remove from an index position (reverse indexing also works)
new_list.pop(0)
print(new_list)

# sorts and reverse
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

# unordered
print(new_list)
print(num_list)

# ordered (my_sorted_list  = new_list.sort() -> does not work
new_list.sort()
print(new_list)

# safe sorted list
new_list.sort()
my_sorted_list = new_list
print(f'This is sorted: {my_sorted_list}')

# sort num list
print(num_list.sort()) # <- does not work = type None
num_list.sort()
print(f'this works: {num_list}')

# reverse
num_list.reverse()
print(num_list)