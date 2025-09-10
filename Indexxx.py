import functools

class Kece:
    def __init__(self, data):
        self.data = data

    def filter_ganjil(self):
        return list(filter(lambda x: x % 2 != 0, self.data))

    def kuadratkan(self, data_terfilter):
        return list(map(lambda x: x**2, data_terfilter))

    def faktorial(self, data_terkuadrat):
        return list(map(lambda x: functools.reduce(lambda a, b: a*b, range(1, x+1)), data_terkuadrat))

# Contoh penggunaan
data_awal = list(range(1, 6))  # Angka 1 sampai 5
objek_kece = Kece(data_awal)

# Proses
data_ganjil = objek_kece.filter_ganjil()
data_kuadrat = objek_kece.kuadratkan(data_ganjil)
data_faktorial = objek_kece.faktorial(data_kuadrat)

# Output
print("Data Awal:", data_awal)
print("Data Ganjil:", data_ganjil)
print("Data Kuadrat:", data_kuadrat)
print("Data Faktorial:", data_faktorial)
