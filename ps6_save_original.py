# Gallery of Paintings
    # OOP, classes, creating class attributes, instance methods, overriding special methods

# Create class Painter 
class Painter:
    # Initiate list of painters
    all_painters = []
    paintings = []
    def __init__(self, name, dob, nationality):
        self.name = name
        self.dob = dob
        self.nationality = nationality
        # Add painter to list when new painter is created
        if name not in self.all_painters:
            self.all_painters.append(self.name)
    
    def paint(self, title='', year=''):
        self.title = title
        self.year = year
        Painter.paintings.append(self.title)

# Create class Painting
class Painting:
    # Initiate list of paintings
    all_paintings = []
    # New Painting object
    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year
        # Add painting to list when new painting is created
        self.all_paintings.append(self.title)

    # Override __str__()
    def __str__(self):
        return f'Title: {self.title}, Artist: {self.painter}, year: {self.year}'

# Create class Gallery   
class Gallery:
    # Initiate list of paintings in collection
    collection = []

    def add_painting(self, painting):
        if painting not in self.collection: 
            Gallery.collection.append(painting)
            print(f'"{painting}" added to the gallery.')
        else:
            print(f'"{painting}" is already in the gallery.')

    def list_paintings(self):
        if len(self.collection) >= 1:
            print('Paintings in the gallery:')
            for painting in self.collection:
                print(painting)
        else:
            print(f'The gallery is empty.\n')


# Testing implementation
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
    pollock.paint('Convergence', '1986')

    # Confirm that the gallery is empty
    gallery.list_paintings()
    print()

    # Add paintings to the gallery
    for painter in Painter.all_painters:
        for painting in Painter.paintings:
            gallery.add_painting(painting)
    print()

    # Try adding duplicate
    gallery.add_painting(pollock.paintings[0])
    print()

    # List paintings in the gallery
    gallery.list_paintings()

    print(pollock.paintings)