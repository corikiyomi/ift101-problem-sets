# Text File Handling
# reading from and writing to plain text files
def write_file():
    # Write user input to a text file
    # Prompt user for name of a file to append to
    try:
        user_file = str(input('\nEnter the name of the text file to append to: '))
        print()
        # Open file requested, append sentence from user input
        file = open(user_file, mode='a')
        user_sentence = input('Please enter a sentence: ')
        file.write(f'{user_sentence} \n')
        file.close()
        # Read contents from new text file; print complete file to shell
        file = open(user_file, mode='r')
        print(f'\nThe contents of {user_file} is now: \n\n{file.read()}')
        file.close()

    # Exception handling:
    except FileNotFoundError as err:
        print('A file name must be entered.\n')
        write_file()
    except OSError as err:
        print(f'Error: {user_file} was found, but there was an error reading it. Please try again.\n')
        write_file()
    except Exception as err: # Catch-all
        print(f'Error: Something bad happened and I can\'t explain it.\n')
        write_file()

write_file()