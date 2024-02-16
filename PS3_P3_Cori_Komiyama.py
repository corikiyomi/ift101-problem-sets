# Sun Devil
    # Branches, loops, loop control statements

# Define variables
user_input = ''

while user_input != 'stop':
    # Get user input
    user_input = input('Please enter a number or "stop": ')
    
    if user_input != 'stop':
        
        if ((int(user_input) % 2) == 0) and ((int(user_input) % 3) == 0):
            print('SunDevil\n')
            continue

        elif (int(user_input) % 2) == 0:
            print('Sun\n')
            continue
        
        elif (int(user_input) % 3) == 0:
            print('Devil\n')
            continue
        
        else:
            print(f'{user_input} \n')
            continue
        
    elif user_input == 'stop':
        break

print('\nThank you for playing SunDevil, Sun Devil!')
