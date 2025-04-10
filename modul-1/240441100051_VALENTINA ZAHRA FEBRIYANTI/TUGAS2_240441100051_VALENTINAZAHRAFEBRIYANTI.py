class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
        pass
    def tampilkan_info(self):
        print("=====Data Mahasiswa=====")
        print(f"Nama     :{self.nama}")
        print(f"Nim      :{self.nim}")
        print(f"Jurusan  :{self.jurusan}")
        print(f"Alamat   :{self.alamat}")
        print("========================================")

Data_Mahasiswa=[]
Daftar_Nim=set()
for i in range(3):
    print(f"\nMasukkan data mahasiswa ke-{i+1}:")
    nama= input("Nama     :")
    while True:
        nim= input("Nim      :")
        if not nim.isdigit():
            print("Nim harus berupa angka!")
        elif nim in Daftar_Nim:
            print("nim sudah digunakan, masukkan yang beda!")
        else:
            Daftar_Nim.add(nim)
            break   
    jurusan= input("Jurusan   :")
    alamat= input("Alamat   :")
    mahasiswa = Mahasiswa(nama,nim,jurusan,alamat)
    Data_Mahasiswa.append(mahasiswa)
for mhs in Data_Mahasiswa:
    mhs.tampilkan_info()









