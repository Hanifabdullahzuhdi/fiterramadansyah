# Contoh kode Functional Programming

# Fungsi murni untuk menghitung kuadrat suatu bilangan
def square(x):
    return x ** 2

# Fungsi murni untuk menjumlahkan dua bilangan
def add(x, y):
    return x + y

# Fungsi murni untuk mengalikan dua bilangan
def multiply(x, y):
    return x * y

# Menggunakan fungsi-fungsi tersebut
result = multiply(add(2, 3), square(4))
print(result)  # Output: 100
