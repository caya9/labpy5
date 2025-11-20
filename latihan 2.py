data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

while True:
    print("\n=== MENU ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

        data_mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": nilai_akhir
        }
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        nama = input("Masukkan nama yang akan diubah: ")
        if nama in data_mahasiswa:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

            data_mahasiswa[nama] = {
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": nilai_akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Nama tidak ditemukan!")

    elif pilihan == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        if nama in data_mahasiswa:
            del data_mahasiswa[nama]
            print("Data berhasil dihapus!")
        else:
            print("Nama tidak ditemukan!")

    elif pilihan == "4":
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        if len(data_mahasiswa) == 0:
            print("Belum ada data.")
        else:
            for nama, nilai in data_mahasiswa.items():
                print(f"{nama} - Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Akhir: {nilai['akhir']:.2f}")

    elif pilihan == "5":
        nama = input("Masukkan nama yang dicari: ")
        if nama in data_mahasiswa:
            nilai = data_mahasiswa[nama]
            print(f"Data ditemukan!")
            print(f"Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Nilai Akhir: {nilai['akhir']:.2f}")
        else:
            print("Nama tidak ditemukan!")

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")

