# CSV File Handling
    # reading from, writing to CSV files, exception handling
import csv

# Prompt user to enter a student's name, their grade, and course name
def grades_csv():
    grades = []
    try:
        name = grades.append(input('Please enter student\'s name: ').capitalize())
        course = grades.append(input('Please enter course number: ').upper())
        grade = int(input('Enter grade: '))
        grades.append(str(grade).strip())
        # if grade not valid, raise error, ask for input again
        if grade < 0:
            print('Invalid input. Please enter a number.')
            grade = int(input('Enter grade: '))
            grades.append(str(grade).strip())
    # handle exceptions for no permissions, file not found, IO errors
    except IOError:
        print('Error')
    except ValueError:
        print('Invalid input. Please enter a number.')
        grade = int(input('Enter grade: '))
        grades.append(str(grade))
    except FileNotFoundError:
        print('Error — File not found.')
    try:
        # Open new file in write mode named student_grades.csv
        with open('student_grades.csv', mode='w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_STRINGS)
            writer.writerow(grades)
        # Open student_grades in read mode
        # Read content of file, store in variable
        with open('student_grades.csv', mode='r') as file:
            student_grades = csv.reader(file, delimiter=',')
            for row in student_grades:
                read_file = row
    # handle exceptions for no permissions, file not found, IO errors
    except IOError:
        print('Error')
    except FileNotFoundError:
        print('Error — File not found.')

    # Print contents of variable to shell
    print(f'The content of this file is:\n{read_file}\n')

grades_csv()
