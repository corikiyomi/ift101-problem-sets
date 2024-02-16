# Gallery of Paintings
    # OOP, simple Painter and Paintings Management System
    # classes, attributes, instance methods, special methods

class Painter:
    all_painters = []
    def __init__(self, name, dob, nationality, paintings=[]):
        self.name = name
        self.dob = dob
        self.nationality = nationality
        self.paintings = []
        Painter.all_painters.append(self)

    def paint(self, title, year):
        self.title = title
        self.year = year
        self.paintings.append([title, year])

class Painting(Painter):
    all_paintings = []
    def __init__(self, title, year, painter=''):
        self.title = title
        self.year = year
        self.name = painter
        if self not in Painting.all_paintings:
            Painting.all_paintings.append(Painter.paint(self,title, year))
            print(self)
    
    def __str__(self):
        print(f'Title: {self.title}, Artist: {self.name}, Year: {self.year}')

class Gallery:
    collection = []

    def add_painting(self, painting):
        if painting not in self.collection:
            self.collection.append(painting)
            print(f'{painting} added to the gallery.')
        else:
            print(f'{painting} is already in the gallery.')
    
    def list_paintings(self):
        if len(self.collection) == 0:
            print('The gallery is empty.')
        else:
            print(f'Paintings in the gallery:')
            for painting in self.collection:
                print(painting)


# Testing the implementation
if __name__ == '__main__':
    # Create painters
    hundert = Painter('Hundertwasser', 'December 15, 1928', 'Austria')
    pollock = Painter('Pollock', 'January 28, 1912', 'U.S.')

    # Create a gallery
    gallery = Gallery()

    # Hundertwasser paintings
    hundert.paint('The Way to You', '1966')
    hundert.paint('The Second Skin', '1986')

    # Pollock paintings
    pollock.paint('Alchemy', '1947')
    pollock.paint('Convergence', '1952')

    # Confirm that the gallery is empty
    gallery.list_paintings()
    print()

    # Add paintings to the gallery
    for painter in Painter.all_painters:
        for painting in painter.paintings:
           gallery.add_painting(painting)
    
print(pollock.paintings)
print(hundert.paintings)
print()
print(gallery.collection)