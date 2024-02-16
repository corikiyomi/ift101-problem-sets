# Get two numbers from the user
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

# Perform multiplication

# SyntaxError: multiplication uses * not x
# TypeError: num1, num2 are 'str' type, cannot be multiplied
result = int(num1) * int(num2)
# TypeError: + should be ,; string should be f'string
# LogicError: product should be float to match example
print(f'The product of the numbers is: ', float(result))

# Perform division, if possible

# TypeError: num1 is a string type and cannot use >
# num1 must be changed to 'int'
# LogicError: if statement should include num2 > 0 to avoid error if num2 input is 0
if (int(num1) > 0) and (int(num2) > 0) :
    # SyntaxError: division uses / not :
    # num1, num2 should be changed to 'int' type
    # string should be f'string
    result = int(num1) / int(num2)
    print(f'The division of the numbers is: ', result)
    
else:
    print('Division not possible: Cannot divide by zero!')