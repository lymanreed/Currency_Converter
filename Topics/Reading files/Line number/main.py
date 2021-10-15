file = open('sample.txt', 'r')
c = 0
for line in file:
    c += 1
file.close()
print(c)
