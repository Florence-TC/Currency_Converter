# read animals.txt
# and write animals_new.txt

file = open('animals.txt', 'r')
animals = file.readlines()
new_animals = []
for animal in animals:
    animal = animal.strip('\n')
    new_animals.append(animal)

new_file = open('animals_new.txt', 'w', encoding='utf-8')
for animal in new_animals:
    new_file.write(animal + ' ')

file.close()
new_file.close()
