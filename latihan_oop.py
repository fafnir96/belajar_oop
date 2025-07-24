# class DataLoader:
#     def __init__(self, nama_file):
#         self.nama_file = nama_file

#     def muat_data(self):
#         print(f"Data dimuat dari {self.nama_file}")


# class CSVLoader(DataLoader):
#     def muat_data(self):
#         print(f"Memuat data dari file CSV: {self.nama_file}")


# class JSONLoader(DataLoader):
#     def muat_data(self):
#         print(f"Memuat data dari file JSON: {self.nama_file}")


# class Analyzer:
#     def __init__(self, data):
#         self.data = data

#     def jumlah_data(self):
#         print(f"Terdapat {self.data} Baris Data")


# csv_loader = CSVLoader("produk.csv")
# json_loader = JSONLoader("transaksi.json")

# csv_loader.muat_data()
# json_loader.muat_data()

# analyst1 = Analyzer(100)
# analyst2 = Analyzer(100)

# analyst1.jumlah_data()
# analyst2.jumlah_data()


# class Mahasiswa:
#     def __init__(self, nama, nim, jurusan):
#         self.nama = nama
#         self.nim = nim
#         self.jurusan = jurusan

#     def perkenalan(self):
#         return f"Halo, saya {self.nama} dari jurusan {self.jurusan}, NIM {self.nim}"


# class Pengguna:
#     def __init__(self, nama, email):
#         self.nama = nama
#         self.email = email


# class Admin(Pengguna):
#     def __init__(self, nama, email, hak_akses):
#         self.hak_akses = hak_akses
#         super().__init__(nama, email)

#     def cetak(self):
#         return f"Nama: {self.nama}, email: {self.email}, hak_akses: {self.hak_akses}"


# class DataLoader:
#     def __init__(self, nama_file):
#         self.nama_file = nama_file

#     def muat_data(self):
#         return f"Data dimuat dari {self.nama_file}"


# class ExcelLoader(DataLoader):
#     def muat_data(self):
#         return f"Memuat file Excel dari: {self.nama_file}"


# class JSONLoader(DataLoader):
#     def muat_data(self):
#         return f"Memuat file JSON dari: {self.nama_file}"


# def proses_data(loader):
#     print(loader.muat_data())


# file_excel = ExcelLoader("File.xlsx")
# file_json = JSONLoader("File.json")

# proses_data(file_excel)
# proses_data(file_json)


# class AkunBank:
#     def __init__(self, saldo_awal):
#         self.__saldo = saldo_awal

#     def setor(self, jumlah):
#         self.__saldo += jumlah
#         print(f"Setor: {jumlah}. Saldo sekarang: {self.__saldo}")

#     def tarik(self, jumlah):
#         if jumlah <= self.__saldo:
#             self.__saldo -= jumlah
#             print(f"Tarik: Rp{jumlah}. Saldo sekarang: Rp{self.__saldo}")

#     def lihat_saldo(self):
#         print(f"Saldo saat ini: {self.__saldo}")


# akun = AkunBank(1000000)
# akun.lihat_saldo()
# akun.setor(500000)
# akun.tarik(300000)


# class Produk:
#     def __init__(self, nama, harga):
#         self.nama = nama
#         self.harga = harga


# class Transaksi:
#     def __init__(self):
#         self.list_transaksi = []

#     def masukkan_transaksi(self, transaksi):
#         self.list_transaksi.append(transaksi)

#     def total_harga(self):
#         total = 0
#         for transaksi in self.list_transaksi:
#             total += transaksi.harga
#         return total


# class Laporan:
#     def __init__(self, transaksi):
#         self.transaksi = transaksi

#     def cetak_laporan(self):
#         print("=== Laporan Transaksi ===")
#         for produk in self.transaksi.list_transaksi:
#             print(f"{produk.nama} - Rp{produk.harga}")
#         print(f"\nTotal: Rp{self.transaksi.total_harga()}")


# # Buat produk-produk
# produk1 = Produk("Mouse Wireless", 150000)
# produk2 = Produk("Keyboard Mechanical", 300000)
# produk3 = Produk("USB Hub", 75000)

# # Tambahkan ke transaksi
# transaksi_hari_ini = Transaksi()
# transaksi_hari_ini.masukkan_transaksi(produk1)
# transaksi_hari_ini.masukkan_transaksi(produk2)
# transaksi_hari_ini.masukkan_transaksi(produk3)

# # Cetak laporan
# laporan = Laporan(transaksi_hari_ini)
# laporan.cetak_laporan()


class Film:
    def __init__(self, judul, durasi, rating):
        self.judul = judul
        self.durasi = durasi
        self.rating = rating


class Tiket:
    def __init__(self, film, nomor_kursi, harga):
        self.film = film
        self.nomor_kursi = nomor_kursi
        self.harga = harga


class Bioskop:
    def __init__(self, nama_bioskop):
        self.nama_bioskop = nama_bioskop
        self.daftar_tiket = []

    def pesan_tiket(self, tiket):
        self.daftar_tiket.append(tiket)

    def tampilkan_tiket(self):
        print(f"Tiket di {self.nama_bioskop}")
        for i, tiket in enumerate(self.daftar_tiket, 1):
            print(
                f"{i}. Film {tiket.film.judul}, Kursi: {tiket.nomor_kursi}, Harga: {tiket.harga}"
            )

    def total_pemasukan(self):
        pemasukan = 0
        for tiket in self.daftar_tiket:
            pemasukan += tiket.harga
        return pemasukan


film1 = Film("Sore", 120, "18+")
film2 = Film("Juragan", 90, "R+")
film3 = Film("Lebah", 110, "12+")

tiket1 = Tiket(film1, "D4", 40000)
tiket2 = Tiket(film1, "D5", 40000)
tiket3 = Tiket(film3, "C6", 40000)

bioskop = Bioskop("Cinepolis DETOS")

bioskop.pesan_tiket(tiket1)
bioskop.pesan_tiket(tiket2)
bioskop.pesan_tiket(tiket3)

bioskop.tampilkan_tiket()
print("Total Pemasukan: ", bioskop.total_pemasukan())
