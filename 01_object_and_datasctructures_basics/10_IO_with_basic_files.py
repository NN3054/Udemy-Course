# basic files

# creating txt file
f = open("test.txt", "w+")

# write in the file
for i in range(3):
    f.write("This is line %d\r\n" % (i+1))

# set a textfile as variuable
f = open('test.txt', "r")


# output of the content of the test.txt file (can be done without if)
if f.mode == "r":
    contents = f.read()
    print(contents)

# does not work because the "cursor" is at the end
contents2 = f.read()
print(contents2)

# set "cursor" to start
f.seek(0)

# works now as we reseted the cursor
contents3 = f.read()
print(f'NOW IT WORKS: \n{contents3}')

# seek back to 0
# read seperate lines (not needed in this example)
f.readlines()

# close file
f.close()

# avoiding errors with double opening
with open('test.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

# reading and writting files
# opening as "r" (read-permission), r = read, w = write (will overwrite or create new), a = append, r+ = reading and writing, w+ = writing and reading (same as w)
with open('test.txt',"r") as myfile:
    contents = myfile.read()

# only reading
print(f'Itteration 4: \n{contents}')

# adding a fourth line
f = open("test.txt", "a")

# add new line
for i in range(2):
    f.write("\nADDED LINE")

# close as it's opened in "a" so not readable
f.close()

# open in "r" so it's readable
f = open("test.txt", "r+")
contentappended = f.read()
print(contentappended)

with open ('test2.txt', "w") as f2:
    f2.write('this file just got created')

with open("test2.txt", "r") as f2:
    print(f2.read())