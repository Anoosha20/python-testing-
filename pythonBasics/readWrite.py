file = open('test.txt')

# read all the contents of file
# read n num of characters by passing parameter
# print(file.read(5))
# read one  single line at a time readline()
# print(file.readline())
#print(file.readline())

# *** one method
line = file.readline()
while line!='':
    print(line)
    line = file.readline()
# ***other method
for lin in file.readlines():
    print(lin)

file.close()
