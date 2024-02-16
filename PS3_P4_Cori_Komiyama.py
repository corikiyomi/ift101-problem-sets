# Multiplication Tables
    # range(), branches, nested loops

# Get user inputs
low_limit = int(input('Enter the minimun number for the multiplication table: '))
high_limit = int(input('Enter the maximum number for the multiplication table: '))
print()

# Define variables
int_list_x = []
int_list_y = []

# Create integer list
for x in range(low_limit, high_limit + 1):
    int_list_x.append(x)
    
for y in range(low_limit, high_limit + 1):
        int_list_y.append(y)

for x in int_list_x:
    for y in int_list_y:
        if y <= x:
            prod = x * y
            print(prod, end = '	')
        if y > x:
            print('*', end = '	')


