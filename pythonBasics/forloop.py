obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
    print(i * 2)

# sum of first natural numbers 1+2+3+4+5=15
# range(i,j) ~> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("****************")
for k in range(1, 10, 3):
    print(k)
print("******skipping first index *******")
for m in range(10):
    print(m)