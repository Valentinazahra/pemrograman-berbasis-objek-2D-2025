class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        pass
    def berjalan(self):
        print(f"{self.nama} sedang berjalan di Taman")
    def berlari(self):
        print(f"{self.nama} sedang berlari di tepi jalan")
manusia1 = Manusia("Valentina Zahra", 18, "Lamongan" )
manusia2 = Manusia("Riza Nurul", 19, "Bandung" )
manusia3 = Manusia("Adelia Putri", 20, "Bojonegoro" )
manusia4  = Manusia("Indy Diana", 18, "Bangkalan" )
manusia5= Manusia("Herlian Savira", 19, "Lamongan" )

manusia1.berlari()
manusia2.berjalan()
manusia3.berlari()
manusia4.berjalan()
manusia5.berlari()
print()
