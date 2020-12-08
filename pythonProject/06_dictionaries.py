# dictionaries
# syntax: {'key1':'value1', 'key2':'value2'}
# dictionaries are unordered and can not be sorted
# when I want a value without needing to know it's index
# has only key-value mapping


# creat dictonary
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)

# print only key1 value
print(my_dict['key1'])

# useful for searching for example a price
prices_lookup = {'apple': 2.99, 'oranges':1.99, 'milk': 4.99}
print(prices_lookup['apple'])

# are flexible in datatypes they can hold (can hold lists and other dic)
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insidekey':100}}

# print list in dict "d"
print(d['k2'])

# print dict "k3" in dict "d"
print(d['k3'])
# print value of inside key in dict "k3" in dict "d"
print(d['k3']['insidekey'])

# lowercase list
c = {'key1':['a', 'b', 'c']}

# create list just out of dict "c", key1 value
mylist = c['key1']

# create variable out of the value of index position 2 in mylist
letter = mylist[2]

# set letter uppercase
print(letter.upper())

# all the above in one command
print(c['key1'][2].upper())


# adding new key-value
d = {'k1':100, 'k2':200}
print(d)
# add "k3" with value 300
d['k3'] = 300
print(d)

# overwrite existing key value pair
d['k1'] = 'NEW VALUE'
print(d)

d = {'k1': 100, 'k2': 200, 'k3': 300}

# print all keys in dict "d"
print(d.keys())

# print all values in dict "d"
print(d.values())

# print all keys with it values of dict "d"
print(d.items())
