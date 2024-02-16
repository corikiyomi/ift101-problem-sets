#Count Odd and Even Using Loops
    #Loops, lists, and string methods

user_input = input('Please enter integers separated by commas: ')
split_list = user_input.split(',')
split_list = [int(x) for x in split_list]

print(f'You have entered {len(split_list)} numbers.')

#variables
evens = 0
odds = 0
i = 0

#evens with while loop
while i < len(split_list):
    if split_list[i] % 2 == 0:
        evens += 1
    i += 1

#odds with for loop
for num in split_list:
    if num % 2 != 0:
        odds += 1
    i += 1

print(f'{evens} are even (counted with while loop).')
print(f'{odds} are odd (counted with for loop).')
