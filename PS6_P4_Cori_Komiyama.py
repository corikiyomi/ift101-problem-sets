# Zoo Management
    # classes, objects, inheritance, polymorphism
    # functionality of menu, accept user input

# Create a Zoo class
class Zoo:
    animals = []
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def add_animal():
        animal_type = input('Enter the animal type (Lion, Elephant): ').capitalize()
        name = input('Enter the animal\'s name: ').capitalize()
        age = int(input('Enter the animal\'s age: '))
        if animal_type == 'Lion':
            name = Lion(name, age, 'Lion')
            Zoo.animals.append()
            print(f'{animal_type} has been added to the zoo.')

        elif animal_type == 'Elephant':
            Elephant(name, age, 'elephant')
        elif animal_type != 'Lion' or animal_type != 'Elephant':
            print('Invalid animal type')
            menu()
        else:
            animal_type != 'Lion' or animal_type != 'Elephant'
            print('Invalid animal type')
            menu()

    def remove_animal():
        pass

    def get_animals():
        pass

    def make_sound():
        pass

# Create Animal class (parent)
class Animal(Zoo):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def make_sound():
        return f'Sound here'
    
# Create child classes of Animal parent class
class Lion(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def make_sound():
        return f'Override sound'
    
class Elephant(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def make_sound():
        return f'Override sounds'
    
# Create an interactive menu that accepts user input
def startup():
    print()
    print('===== Sparky\'s Zoo Management System =====')
    print()

def menu():
    menu_choice = '1'
    print()
    print('1. Add Animal')
    print('2. Remove Animal')
    print('3. List Animals')
    print('4. Quit')
    print()
    menu_choice = input('Choose an option: ')
    # add animal
    while menu_choice != '4':
        if menu_choice == '1':
            Zoo.add_animal()
            menu()
        # remove animal
        elif menu_choice == '2':
            Zoo.remove_animal()
            menu()
        # list animals
        elif menu_choice == '3':
            Zoo.get_animals()
            menu()
        else:
            print()
            print('Try again! Please enter a menu number.')
            menu()
    else:
        print('Quitting Sparky\'s Zoo Management System\n')
        print()
    menu_choice = '4'
        

startup()
menu()

