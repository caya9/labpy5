kontak = {
    "Syava": "0812678888",
    "Caya": "087677776"
}

print("Kontak Syava:", kontak["Syava"])

kontak["Sakira"] = "087654544"

kontak["Caya"] = "088999776"

print("Semua nama:", list(kontak.keys()))

print("Semua nomor:", list(kontak.values()))

print("Daftar kontak lengkap:")
for nama, nomor in kontak.items():
    print(nama, ":", nomor)

del kontak["Caya"]

print("\nKontak setelah Caya dihapus:", kontak)
