# Immutability
name = "Sam"
print (name)

# not possible because of immutability
# name[0] = "P"

# string concatenation
last_letters = name[1:]
print(last_letters)
print("P" + last_letters)

x = "Hello World"

print(x + ", what's up?")

x = x + ", what's up?"

print (x)


#  multiplication of letters

letter = "a"

print(letter *10)


# careful on dynamic typing
print(2+3)
print('2'+'3')

# functions
x = 'Hello World'

print(x.upper())
print(x.lower)
print(x.split())

# split, default on whitespace
x = "Hi this is a string"
print(x.split())
print(x.split('i'))
