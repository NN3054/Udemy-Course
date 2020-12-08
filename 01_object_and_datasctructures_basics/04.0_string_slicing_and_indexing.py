#String slicing & indexing

mystring = 'Hello World'
print(mystring)


#indexing (0,1,2,3,4...  0,-4,-3,-2,-1)
print (mystring[0])

print (mystring[8])


#negative indixing
print (mystring[-2])


#slicing #:3 -> up to but not including
mystring = 'abcdefghij'
print(mystring)
print(mystring[2:])
print (mystring[:4])

#subsequence
print(mystring[3:6])
print(mystring[1:3])

#stepsize
print(mystring[::3])
#start at index 2, till 8, in steps of 2
print(mystring[2:8:2])

#reverse string
print(mystring[::-1])