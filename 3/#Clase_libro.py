#clase_libro
class Libro:
        def __init__(self, title = '', author = '', date = 0, ISBN = ''):
                self.title = title
                self.author = author
                self.date = date
                self.ISBN = ISBN
                
        def __str__ (self):
                return 'El libro {} fué escrito por {} en el año {} y tiene como ISBN {}'.format(self.title, self.author, self.date, self.ISBN)


Libro1 = Libro('holamundo','batman',1234,'dhfrk3u5o')
Libro2 = Libro('hola','bat','dhfrk3u5o')

print(Libro1)
print(Libro2)
