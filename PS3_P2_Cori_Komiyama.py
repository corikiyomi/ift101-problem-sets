user_word = str()
word_str = str()
answer = 'y'
word = list(user_word)

while (len(user_word) >= 0) and (answer == 'y'):
    user_word = input('Enter the word to check for palindrome: ')
    word = list(user_word)
    word_str = ''

    for index in word:
        continue

    for index in reversed(word):
        word_str += index

    if user_word == word_str:
        print(f'Yes, {user_word} is a palindrome.')
    
    else: 
        print(f'No, {user_word} is not a palindrome.')

    answer = input('\nWould you like to try again? (y/n): ')
    print()

else:
    print('\nThank you for using my palindrome checker!')