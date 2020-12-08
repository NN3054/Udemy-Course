# formatting with .format()

# 'String{}.format('something1','something2')
# 'something gets inserted in the {}

print('This is a String {}'.format('INSERT'))

# advantages: strings can inserted as index positions

print('The {} {} {}'.format('fox','brown','quick'))

# rearranged with index positions
print('The {2} {1} {0}'.format('fox','brown','quick'))

# repeating indexes
print('The {0} {0} {0}'.format('fox','brown','quick'))

# using keywords
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

# float formatting ({value:width.precision f}

result = 100/777
print(result)

# rounding on decimals
print("The result was {r:3.5f}".format(r=result))

# f-string formatting
name = "Jose"
print(f'His name is {name}')

age = 17
print(f'Name: {name} Age: {age}')

# more to come...