from prettytable import PrettyTable

class Produk:
    def __init__(self, id, nama, harga, stok):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.stok = stok

class TokoBuah:
    def __init__(self):
        self.produk = []

    def tambah_produk(self, id, nama, harga, stok):
        self.produk.append(Produk(id, nama, harga, stok))
        print(f"Produk {nama} telah ditambahkan.")

    def lihat_produk(self):
        table = PrettyTable(["ID", "Nama Produk", "Harga", "Stok"])
        for p in self.produk:
            table.add_row([p.id, p.nama, p.harga, p.stok])
        print(table)

    def ubah_produk(self, id, nama, harga, stok):
        for p in self.produk:
            if p.id == id:
                p.nama = nama
                p.harga = harga
                p.stok = stok
                print(f"Produk ID {id} telah diubah.")
                return
        print(f"Tidak ada produk dengan ID {id}.")

    def hapus_produk(self, id):
        for p in self.produk:
            if p.id == id:
                self.produk.remove(p)
                print(f"Produk ID {id} telah dihapus.")
                return
        print(f"Tidak ada produk dengan ID {id}.")

class Pembeli:
    def __init__(self):
        self.keranjang = []

    def beli_produk(self, toko, id, jumlah):
        for p in toko.produk:
            if p.id == id:
                if p.stok >= jumlah:
                    p.stok -= jumlah
                    self.keranjang.append(Produk(p.id, p.nama, p.harga, jumlah))
                    print(f"{jumlah} {p.nama} telah ditambahkan ke keranjang.")
                    return
                else:
                    print(f"Stok {p.nama} tidak mencukupi.")
                    return
        print(f"Tidak ada produk dengan ID {id}.")

def login_admin():
    while True:
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")

        # Ganti username dan password dengan yang sesuai
        if username == "admin" and password == "rizy123":
            return True
        else:
            print("Username atau password admin salah. Coba lagi.")

def main():
    toko = TokoBuah()
    peran = "pembeli"  # Defaultnya, peran adalah pembeli
    pembeli = Pembeli()

    while True:
        if peran == "admin":
            print("\nMenu Admin:")
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Ubah Produk")
            print("4. Hapus Produk")
            print("5. Keluar sebagai Admin")
        else:
            print("\nMenu Pembeli:")
            print("1. Beli Produk")
            print("2. Lihat Keranjang")
            print("3. Keluar sebagai Pembeli")
            print("4. Ganti ke mode Admin")

        pilihan = input("Masukkan pilihan: ")

        if peran == "admin":
            if pilihan == '1':
                id = int(input("Masukkan ID produk: "))
                nama = input("Masukkan nama produk: ")
                harga = float(input("Masukkan harga produk: "))
                stok = int(input("Masukkan stok produk: "))
                toko.tambah_produk(id, nama, harga, stok)
            elif pilihan == '2':
                toko.lihat_produk()
            elif pilihan == '3':
                id = int(input("Masukkan ID produk yang akan diubah: "))
                nama = input("Masukkan nama produk baru: ")
                harga = float(input("Masukkan harga produk baru: "))
                stok = int(input("Masukkan stok produk baru: "))
                toko.ubah_produk(id, nama, harga, stok)
            elif pilihan == '4':
                id = int(input("Masukkan ID produk yang akan dihapus: "))
                toko.hapus_produk(id)
            elif pilihan == '5':
                peran = "pembeli"  # Keluar dari mode admin
            else:
                print("Pilihan tidak valid.")
        else:
            if pilihan == '1':
                id = int(input("Masukkan ID produk yang ingin dibeli: "))
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                pembeli.beli_produk(toko, id, jumlah)
            elif pilihan == '2':
                print("\nKeranjang Belanja:")
                print("Selamat Barang Anda Sudah Masuk Ke Keranjang Silahkan Lanjutkan Pembayaran Ke Kasir")
                table = PrettyTable(["Nama Produk", "Harga", "Jumlah"])
                for p in pembeli.keranjang:
                    table.add_row([p.nama, p.harga, p.stok])
                print(table)
            elif pilihan == '3':
                break
            elif pilihan == '4':
                if login_admin():
                    peran = "admin"  # Ganti ke mode admin
                else:
                    print("Login admin gagal.")
            else:
                print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
