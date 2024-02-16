# Student Management
    # OOP, simple Employee Management System

# Create class Student
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        
    def get_summary(self):
        print(f'Student {self.name} (ID: {self.student_id}) got a grade of {self.grade}.')

# Create class Course, inherit Student attributes
class Course(Student):
    student_list = []

    def add_student(self, student):
        self.student_list.append(self)
        print(f'Student {student} added to course IFT 101.')
    
    def get_summary(self): # overwrite get_summary to exclude student ID
        print(f'Student {self.name} got a grade of {self.grade}.')

    def get_course_gpa():
        all_grades = []
        sum = 0
        for x in Course.student_list: # access Student objects in list to access each student grade
            x.get_summary()
            all_grades.append(x.grade)
        for i in all_grades: # get sum of all grades to calculate course GPA
            sum += i
        gpa = sum / len(all_grades)
        print(f'The GPA for course IFT 101 is {gpa:.2f}.')
    
    def remove_student(self, student_id):
        if self.student_id == student_id:
            Course.student_list.remove(self)
            print(f'Student {self.name} removed from course IFT 101.')


# Instantiate
student1 = Student('Niko', 1, 75)
student2 = Student('Sarah', 2, 99)
student3 = Student('Alice', 3, 100)
niko = Course('Niko', 1, 75)
sarah = Course('Sarah', 2, 99)
alice = Course('Alice', 3, 100)

# Add students to course
niko.add_student('Niko')
sarah.add_student('Sarah')
alice.add_student('Alice')
print()

# Get course GPA
Course.get_course_gpa()
print()

# Remove student(s) from course
alice.remove_student(3)
print()

# Get new course GPA
Course.get_course_gpa()
print()