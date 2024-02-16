# Basic Data Structures
    # Lists, sets, tuples, dictionaries

#List
dogs = ['Bulldog', 'Poodle', 'Beagle', 'Terrier']
print(f'List: {dogs}')

#Convert to tuple
dogs_tuple = tuple(dogs)
print(f'Tuple: {dogs_tuple}')

#Convert to set
dogs_set = set(dogs)
print(f'Set: {dogs_set}')

#Convert to dictionary
lengths = []
for i in dogs:
    lengths.append(len(i))

key_value_pairs = zip(dogs, lengths)
dogs_dict = dict(key_value_pairs)
print(f'Dictionary: {dogs_dict}')

#Modify List
dogs.append('Pug')
dogs.append('Chihuahua')
dogs.remove('Beagle')

print(f'Updated List: {dogs}')

#Update Dictionary
lengths.clear()

for i in dogs:
    lengths.append(len(i))
    
key_value_pairs = zip(dogs, lengths)
dogs_dict = dict(key_value_pairs)
print(f'Updated Dictionary: {dogs_dict}')
