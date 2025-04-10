class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
    def suara(self):
        print(f"{self.nama} mengaong: 'Meowwww!'")
    def info(self):
        print(f"Kucing: {self.nama}, Warna: {self.warna}, Umur: {self.umur}")

class Burung:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
    def suara(self):
        print(f"{self.nama} berkicau: 'Cuit cuit!'")
    def info(self):
        print(f"Burung: {self.nama}, Jenis: {self.jenis}, warna: {self.warna}")

class Ikan:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat
    def berenang(self):
        print(f"{self.nama} sedang berenang di {self.habitat}.")
    def info(self):
        print(f"Ikan: {self.nama}, Jenis: {self.jenis}, Habitat: {self.habitat}")
# List data untuk setiap jenis hewan
data_kucing = [("Milo", "Oren", "7 bulan"),("Luna", "Belang", "1 tahun"),("Simba", "Putih","4bulan")]
data_burung = [("Ciko", "Beo", "hijau"),("Geo", "Merpati", "putih"),("Bara", "Dara", "Coklat")]
data_ikan = [("Nemo", "Bandeng", "Tambak"),("Goldy", "Ikan Mas", "Kolam"),("Sharky", "Hiu", "Laut")]
# Membuat objek hewan menggunakan looping
kucing_list = [Kucing(nama, warna, umur) for nama, warna, umur in data_kucing]
burung_list = [Burung(nama, jenis, warna) for nama, jenis, warna in data_burung]
ikan_list = [Ikan(nama, jenis, habitat) for nama, jenis, habitat in data_ikan]
# Menampilkan informasi setiap hewan
print("\n--- Daftar Kucing ---")
for kucing in kucing_list:
    kucing.info()
    kucing.suara()

print("\n--- Daftar Burung ---")
for burung in burung_list:
    burung.info()
    burung.suara()

print("\n--- Daftar Ikan ---")
for ikan in ikan_list:
    ikan.info()
    ikan.berenang()