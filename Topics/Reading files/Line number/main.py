# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
i = 0

for _ in file:
    i += 1
print(i)

file.close()
