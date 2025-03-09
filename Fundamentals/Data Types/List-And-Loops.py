animals = ['Dog', 'Cat', 'Horse', 'Elephant', 'Lion']
for animal in animals:
    print(animal)
    
for i in range(len(animals)):
    print(animals[i])

animals.appends('Tiger', 'Zebra')
animals.append('Penguin')
animals.insert(2, 'Giraffe')
animals.remove('Elephant')

print(animals)
del animals[2]

if 'Dog' in animals:
    print('Dog is in the list.')    
    
print(animals.index('Lion'))
word = animals[1]
if word in animals:
    print(word +' is in the list.')
    
animals.sort()
print(animals)

for animal in animals:
    print(animal)
    