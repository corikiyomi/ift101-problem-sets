# User Defined Functions
    # creating multiple user-defined functions, hierarchical function calls

# Calculate cost and discount at checkout

# calculate total before discount
def calculate_total(num_items, item_price):
    total_cost = num_items * item_price
    return total_cost

# calculate discount
def calculate_discount(total_cost, discount_rate):
    if 0 < discount_rate <= 1:
        discount_amount = total_cost * discount_rate
        return discount_amount
    else:
        raise ValueError('Discount Rate — Please try again. Next time, enter a decimal number between 0 and 1.')

# calculate final price after discount
def calculate_final(items, price, min_items, discount_rate):
    if int(min_items) <= int(items):
        try:
            total_cost = calculate_total(items, price)
            discount_amount = calculate_discount(total_cost, discount_rate)
            final_price = total_cost - discount_amount
            print(f'The final cost is ${final_price:.2f} after a discount of ${discount_amount:.2f} has been applied to the total of ${total_cost:.2f}.\n')
        except ValueError:
            print('Error: Invalid input. Please enter a number.')
        except TypeError:
            print('Error — Please enter a positive number.')
        except Exception:
            print('Error — An unexpected error occurred. Please try again.')

    else:
        raise ValueError('Sorry, you do not have enough items to meet the required amount.')

# Get user input, assign to variables

num_items = int(input('Enter the number of items: '))
if num_items < 0:
    print('Please enter a positive number.')
    num_items = int(input('Enter the number of items: '))

item_price = float(input('Enter the price per item: '))
if item_price < 0:
    print('Please enter a positive number.')
    item_price = float(input('Enter the price per item: '))

min_discount_items = int(input('Enter how many items need to be purchased to qualify for a discount: '))
if min_discount_items < 0:
    print('Please enter a positive number.')
    min_discount_items = input('Enter how many items need to be purchased to qualify for a discount: ')
if min_discount_items > num_items:
    print('You do not have enough items to meet the minimum requirement.')
    
discount_rate = float(input('Enter the discount rate: '))
if discount_rate < 0:
    print('Please enter a positive number.')
    discount_rate = float(input('Enter the discount rate: '))

# Call function passing variables as parameters
calculate_final(num_items, item_price, min_discount_items, discount_rate)