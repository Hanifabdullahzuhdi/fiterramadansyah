# Contoh kode Object-Oriented Programming

# Definisi kelas 'Circle' untuk mewakili lingkaran
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

# Membuat objek dari kelas 'Circle'
my_circle = Circle(5)

# Menggunakan metode pada objek
print(my_circle.area())  # Output: 78.5
print(my_circle.circumference())  # Output: 31.4
