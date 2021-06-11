# read sums.txt
file = open('sums.txt', 'r')

lines = file.readlines()
for text in lines:
    text = text.strip('\n')
    numbers = text.split()
    print(int(numbers[0]) + int(numbers[1]))

file.close()
