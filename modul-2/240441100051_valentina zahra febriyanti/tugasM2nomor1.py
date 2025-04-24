#method class sendiri & method tdk brgntng clas,
class Mahasiswa:
    total_mahasiswa = 0
    def __init__(self, nama, nim, prodi):
        self.mata_kuliah = []  

        if not Mahasiswa.validasi_nim(nim):
            print(f"NIM {nim} tidak valid. NIM harus dimulai dengan '23' dan terdiri dari 10 digit.")
            self.nama = None
            self.nim = None
            self.prodi = None
        else:
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            Mahasiswa.total_mahasiswa += 1

    def tambah_mata_kuliah(self, mata_kuliah):
        if self.nama is not None and mata_kuliah.sks is not None:
            self.mata_kuliah.append(mata_kuliah)

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah:")
        for mk in self.mata_kuliah:
            print(f"  - {mk.nama} ({mk.sks} SKS)")

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return len(nim) == 10 and nim.startswith("23") and nim.isdigit()

# Class MataKuliah
class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = None
        if MataKuliah.cek_sks_valid(sks):
            self.sks = sks
        else:
            print(f"SKS {sks} tidak valid. SKS harus 2 atau 3.")

    @staticmethod
    def cek_sks_valid(sks):
        return sks in (2, 3)
    
# Class Kampus
class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        if self.validasi_nama(nama):
            print("Peringatan: Nama kampus tidak valid. Tidak boleh mengandung angka.")
            self.nama = None
        else:
            self.nama = nama
        self.alamat = alamat
        self.mahasiswa = []

    @staticmethod
    def validasi_nama(nama):
        return any(char.isdigit() for char in nama)

    @classmethod
    def tampilkan_info_kampus(cls, kampus):
        if kampus.nama is None:
            return f"Nama Kampus: {kampus.nama}\nAlamat: {kampus.alamat}"

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)
        Kampus.total_mahasiswa += 1

mk1 = MataKuliah("MK001", "Algoritma Pemrograman", 3)
mk2 = MataKuliah("MK002", "Pemrograman Berbasis Objek", 2)
mk3 = MataKuliah("MK003", "Pengantar Basis Data", 2)
mk4 = MataKuliah("MK004", "Pemrograman Web", 3)
mk5 = MataKuliah("MK005", "Analisis Proses Bisnis", 3)
mk6 = MataKuliah("MK006", "Jaringan Komputer", 2)
mk7 = MataKuliah("MK007", "Bahasa Inggris", 2)
mk8 = MataKuliah("MK008", "E Bussines & E Commers", 3)

mhs1 = Mahasiswa("Valentina", "2301234567", "Teknik Informatika")
mhs2 = Mahasiswa("Zahra", "2302345678", "Sistem Informasi")
mhs3 = Mahasiswa("Febriyanti", "2303456789", "Teknik Informatika")
mhs4 = Mahasiswa("Herlian", "2304567890", "Teknik Informatika")
mhs5 = Mahasiswa("Savira", "2305678901", "Sistem Informasi")
mhs6 = Mahasiswa("Anggriani", "2306789012", "Sistem Informasi")

mhs1.tambah_mata_kuliah(mk1)
mhs1.tambah_mata_kuliah(mk2)
mhs1.tambah_mata_kuliah(mk3)
mhs1.tambah_mata_kuliah(mk4)

mhs2.tambah_mata_kuliah(mk5)
mhs2.tambah_mata_kuliah(mk6)
mhs2.tambah_mata_kuliah(mk7)
mhs2.tambah_mata_kuliah(mk8)

mhs3.tambah_mata_kuliah(mk2)
mhs3.tambah_mata_kuliah(mk3)
mhs3.tambah_mata_kuliah(mk5)
mhs3.tambah_mata_kuliah(mk6)

mhs4.tambah_mata_kuliah(mk1)
mhs4.tambah_mata_kuliah(mk4)
mhs4.tambah_mata_kuliah(mk7)
mhs4.tambah_mata_kuliah(mk8)

mhs5.tambah_mata_kuliah(mk3)
mhs5.tambah_mata_kuliah(mk4)
mhs5.tambah_mata_kuliah(mk5)
mhs5.tambah_mata_kuliah(mk6)

mhs6.tambah_mata_kuliah(mk1)
mhs6.tambah_mata_kuliah(mk2)
mhs6.tambah_mata_kuliah(mk7)
mhs6.tambah_mata_kuliah(mk8)

# Membuat objek kampus (validasi nama otomatis)
kampus = Kampus("Universitas Trunojoyo Madura 11 ", "Jl. Raya Telang, Bangkalan")

# Menambahkan mahasiswa ke kampus
for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    kampus.tambah_mahasiswa(mhs)

# Output data mahasiswa
print("\n===== DATA MAHASISWA =====")
for mhs in kampus.mahasiswa:
    mhs.tampilkan_biodata()
    print()

# Output info kampus
print("===== INFO KAMPUS =====")
print(Kampus.tampilkan_info_kampus(kampus))

# Cek validitas nama kampus
if kampus.nama is None:
    print("Nama Kmpus Tidak Valid (Mngandung Angka)")
else:
    print(f"\nJumlah Mahasiswa Valid yang Terdaftar: {Mahasiswa.jumlah_mahasiswa()}")














