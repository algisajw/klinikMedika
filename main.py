# IMPORT MODUL DATETIME UNTUK MENGAKSES FUNGSI-FUNGSI YANG BERHUBUNGAN DENGAN WAKTU DAN TANGGAL
import datetime

# DEFINISI CLASS PASIEN YANG AKAN MENYIMPAN INFORMASI TENTANG PASIEN
class Pasien:
    # KONSTRUKTOR UNTUK INISIALISASI OBJEK PASIEN DENGAN PARAMETER YANG DIBUTUHKAN
    def __init__(self, nomor, nama, usia, keluhan):
        # MENYIMPAN NOMOR ANTRIAN PASIEN KE DALAM ATTRIBUTE
        self.nomor = nomor
        # MENYIMPAN NAMA PASIEN KE DALAM ATTRIBUTE
        self.nama = nama
        # MENYIMPAN USIA PASIEN KE DALAM ATTRIBUTE
        self.usia = usia
        # MENYIMPAN KELUHAN PASIEN KE DALAM ATTRIBUTE
        self.keluhan = keluhan
        # MENETAPKAN NAMA DOKTER DEFAULT UNTUK SEMUA PASIEN
        self.dokter = "Dr. Haerul Saleh, M.Kes., Sp.THT"
        # MENGAMBIL TANGGAL SAAT INI DAN MEMFORMATNYA DALAM BENTUK HARI, TANGGAL BULAN TAHUN
        self.tanggal = datetime.datetime.now().strftime("%A, %d %B %Y")
        # MENGAMBIL WAKTU SAAT INI DAN MEMFORMATNYA DALAM BENTUK JAM:MENIT ZONA WAKTU
        self.jam = datetime.datetime.now().strftime("%H:%M WITA")

    # METHOD UNTUK MENCETAK TIKET ANTRIAN PASIEN DALAM FORMAT YANG TELAH DITENTUKAN
    def cetakTiket(self):
        # MENCETAK PEMBATAS DAN HEADER TIKET
        print("\n========================================")
        print("         🎟️ TIKET ANTRIAN �️         ")
        print("========================================")
        # MENCETAK NOMOR ANTRIAN PASIEN
        print(f"  🔢 Nomor Antrian : {self.nomor}")
        # MENCETAK NAMA PASIEN
        print(f"  🏥 Nama Pasien   : {self.nama}")
        # MENCETAK USIA PASIEN
        print(f"  🎂 Usia          : {self.usia} Tahun")
        # MENCETAK KELUHAN PASIEN
        print(f"  🫅 Keluhan       : {self.keluhan}")
        # MENCETAK NAMA DOKTER YANG MENANGANI
        print(f"  👨‍⚕️ Dokter        : {self.dokter}")
        # MENCETAK TANGGAL KUNJUNGAN
        print(f"  📅 Tanggal       : {self.tanggal}")
        # MENCETAK WAKTU KUNJUNGAN
        print(f"  ⏰ Jam           : {self.jam}")
        # MENCETAK PENUTUP TIKET
        print("========================================\n")

# DEFINISI CLASS ANTRIAN YANG AKAN MENGELOLA DAFTAR PASIEN YANG MENUNGGU
class Antrian:
    # KONSTRUKTOR UNTUK INISIALISASI OBJEK ANTRIAN DENGAN PARAMETER KAPASITAS
    def __init__(self, kapasitas):
        # INISIALISASI LIST UNTUK MENYIMPAN DAFTAR ANTRIAN PASIEN
        self.daftarAntrian = []
        # MENYIMPAN KAPASITAS MAKSIMAL ANTRIAN
        self.kapasitas = kapasitas
        # INISIALISASI NOMOR ANTRIAN BERIKUTNYA YANG AKAN DIBERIKAN
        self.nomorBerikutnya = 1

    # METHOD UNTUK MENAMBAHKAN PASIEN BARU KE DALAM ANTRIAN
    def tambahPasien(self):
        # MEMERIKSA APAKAH ANTRIAN SUDAH PENUH
        if len(self.daftarAntrian) >= self.kapasitas:
            # JIKA PENUH, CETAK PESAN DAN KEMBALI TANPA MELAKUKAN APA-APA
            print("\n⚠️ Antrian Penuh! Tidak Dapat Menambahkan Pasien Baru.")
            return

        # MENCETAK HEADER UNTUK MENAMBAH ANTRIAN
        print("\n========================================")
        print("         ➕ TAMBAH ANTRIAN ➕         ")
        print("========================================")
        # MEMINTA INPUT NAMA PASIEN DARI PENGGUNA
        nama = input("📝 Nama Pasien   : ")
        # MEMINTA INPUT USIA PASIEN DARI PENGGUNA DAN KONVERSI KE INTEGER
        usia = int(input("🎂 Usia Pasien   : "))
        # MEMINTA INPUT KELUHAN PASIEN DARI PENGGUNA
        keluhan = input("🤕 Keluhan Pasien: ")

        # MEMBUAT OBJEK PASIEN BARU DENGAN INFORMASI YANG DIBERIKAN
        pasienBaru = Pasien(self.nomorBerikutnya, nama, usia, keluhan)
        # MENAMBAHKAN PASIEN BARU KE DALAM DAFTAR ANTRIAN
        self.daftarAntrian.append(pasienBaru)
        # MENCETAK PESAN KONFIRMASI PENAMBAHAN ANTRIAN
        print(f"\n✅ Nomor Antrian {self.nomorBerikutnya} Untuk {nama} Telah Ditambahkan.")
        # MENCETAK TIKET ANTRIAN UNTUK PASIEN BARU
        pasienBaru.cetakTiket()
        # MENAMBAHKAN NOMOR ANTRIAN BERIKUTNYA UNTUK PASIEN SELANJUTNYA
        self.nomorBerikutnya += 1

    # METHOD UNTUK MEMANGGIL PASIEN YANG ADA DI URUTAN TERDEPAN ANTRIAN
    def panggilPasien(self):
        # MEMERIKSA APAKAH ANTRIAN KOSONG
        if not self.daftarAntrian:
            # JIKA KOSONG, CETAK PESAN DAN KEMBALI
            print("\n⚠️ Antrian Kosong.")
            return

        # MENGAMBIL PASIEN DARI URUTAN TERDEPAN ANTRIAN (FIFO)
        pasienDipanggil = self.daftarAntrian.pop(0)
        # MENCETAK INFORMASI PASIEN YANG DIPANGGIL
        print("\n========================================")
        print(f"📢 MEMANGGIL PASIEN: {pasienDipanggil.nomor} - {pasienDipanggil.nama}")
        print("========================================\n")

        # JIKA ANTRIAN SUDAH KOSONG SETELAH DIPANGGIL, RESET NOMOR ANTRIAN KE 1
        if not self.daftarAntrian:
            self.nomorBerikutnya = 1

    # METHOD UNTUK MENAMPILKAN DAFTAR PASIEN YANG SEDANG MENUNGGU DALAM ANTRIAN
    def tampilkanAntrian(self):
        # MENCETAK HEADER DAFTAR ANTRIAN
        print("\n========================================")
        print("         📋 DAFTAR ANTRIAN 📋        ")
        print("========================================")
        # MENCETAK INFORMASI KAPASITAS ANTRIAN YANG TERISI DAN TOTAL
        print(f"  🏥 Kapasitas Antrian: {len(self.daftarAntrian)}/{self.kapasitas}")
        # MEMERIKSA APAKAH ANTRIAN KOSONG
        if not self.daftarAntrian:
            # JIKA KOSONG, CETAK PESAN
            print("⚠️ Antrian Kosong.")
        else:
            # JIKA TIDAK KOSONG, ITERASI DAN CETAK INFORMASI SETIAP PASIEN
            for pasien in self.daftarAntrian:
                print(f"  🔢 No: {pasien.nomor} | 🏥 Nama: {pasien.nama} | 🎂 Usia: {pasien.usia} Tahun | 🤕 Keluhan: {pasien.keluhan}")
        # MENCETAK PENUTUP DAFTAR ANTRIAN
        print("========================================\n")

# DEFINISI CLASS SISTEMANTRIAN YANG AKAN MENJALANKAN APLIKASI UTAMA
class SistemAntrian:
    # KONSTRUKTOR UNTUK INISIALISASI SISTEM ANTRIAN
    def __init__(self):
        # LOOP UNTUK MEMASTIKAN INPUT KAPASITAS VALID
        while True:
            try:
                # MEMINTA INPUT KAPASITAS MAKSIMAL ANTRIAN DARI PENGGUNA
                kapasitas = int(input("🛑 Masukkan Batas Maksimum Antrian: "))
                # MEMERIKSA APAKAH KAPASITAS LEBIH DARI 0
                if kapasitas > 0:
                    break
                # JIKA TIDAK, CETAK PESAN ERROR
                print("⚠️ Harus Lebih Dari 0!")
            except ValueError:
                # JIKA INPUT BUKAN ANGKA, CETAK PESAN ERROR
                print("⚠️ Masukkan Angka Yang Valid!")

        # MEMBUAT OBJEK ANTRIAN DENGAN KAPASITAS YANG TELAH DITENTUKAN
        self.antrian = Antrian(kapasitas)

    # METHOD UTAMA UNTUK MENJALANKAN SISTEM ANTRIAN DAN MENAMPILKAN MENU
    def mulai(self):
        # LOOP UTAMA UNTUK MENJALANKAN APLIKASI SECARA BERKELANJUTAN
        while True:
            # MENCETAK MENU UTAMA
            print("\n========================================")
            print(" 🏥 MENU SISTEM ANTRIAN KLINIK MEDIKA 🏥 ")
            print("========================================")
            print(" 1️⃣ ➕ Tambah Antrian")
            print(" 2️⃣ 📢 Panggil Antrian")
            print(" 3️⃣ 📋 Lihat Daftar Antrian")
            print(" 4️⃣ ❌ Keluar")
            print("========================================")
            # MEMINTA INPUT PILIHAN MENU DARI PENGGUNA
            pilihan = input("🛑 Pilih Menu (1-4): ")

            # MENJALANKAN FUNGSI SESUAI DENGAN PILIHAN PENGGUNA
            if pilihan == '1':
                self.antrian.tambahPasien()
            elif pilihan == '2':
                self.antrian.panggilPasien()
            elif pilihan == '3':
                self.antrian.tampilkanAntrian()
            elif pilihan == '4':
                # JIKA PILIHAN 4, CETAK PESAN SELAMAT TINGGAL DAN KELUAR DARI LOOP
                print("\n👋 Terima Kasih Telah Menggunakan Sistem Antrian Klinik Medika. Semoga Sehat Selalu! 💙\n")
                break
            else:
                # JIKA PILIHAN TIDAK VALID, CETAK PESAN ERROR
                print("⚠️ Pilihan Tidak Valid! Silakan Coba Lagi.\n")

# MEMBUAT OBJEK SISTEMANTRIAN DAN MENJALANKAN METHOD MULAI
SistemAntrian().mulai()