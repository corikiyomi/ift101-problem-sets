# Exception Handling
    # user-defined functions, exceptions

#Initial state
play = 'y'

#Title
print('Safe Division Program\n')

#Initial user input
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

#Write a function named safe_division, print result
def safe_division(num1, num2):
    play = 'y'
    while play == 'y':
        try:
            result = float(num1) / float(num2)
            print(f'Result: {result}\n')
            play_again(safe_division)
        except ValueError:
            print('Result: Error — Both inputs must be numbers.\n')
            play_again(safe_division)
        except ZeroDivisionError:
            print('Result: Error — Cannot divide by zero.\n')
            play_again(safe_division)
        break

#Create a function to prompt another round
def play_again(safe_division):
#Ask if user would like to try again:
    play = input('Would you like to try again? y/n: ').lower()
    print()
    if play == 'y':
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        safe_division(num1, num2)
    elif play != 'y' and play != 'n':
        print('Error — Please enter a \'y\' or \'n\'\n')
        play_again(safe_division)
    elif play == 'n':
        print('Thank you for using the Safe Division Program!\n')

safe_division(num1, num2)