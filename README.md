# LAPORAN PRAKTIKUM 5 
Nama        : Chaya Aulia

Nim         : 312510197

Kelas       : TI.25.A2

Mata Kuliah : Pengantar Pemrograman 

# Tujuan Praktikum

- Mempelajari konsep dictionary sebagai struktur data utama dalam Python.

- Mampu membuat, mengakses, mengubah, dan menghapus data pada dictionary.

- Dapat menerapkan dictionary untuk membuat program pengolahan nilai mahasiswa.

- Mengimplementasikan logika program menggunakan menu interaktif.

- Melatih pembuatan program yang modular, rapi, dan mudah dipahami.
  
# Dasar Teori

Dictionary adalah struktur data Python yang menyimpan pasangan key : value.
Dictionary bersifat:

- Mutable (bisa diubah)

- Unordered

- Indexed melalui key

- Cocok untuk data berlabel (nama, id, dll.)

  Contoh :
  ```python
  data = {
    "Ari": 90,
    "Dina": 80
}
```


``` python
data.keys()      # semua key
data.values()    # semua value
data.items()     # key dan value
data["Ari"]      # akses via key
data["Budi"] = 75  # menambah data
del data["Ari"]    # menghapus data
```
# Flowchart
``` python
                ┌──────────────┐
                │ Mulai Program │
                └───────┬──────┘
                        ↓
              ┌──────────────────┐
              │ Tampilkan Menu   │
              └───────┬─────────┘
                      ↓
            ┌──────────────────────┐
            │ Input Pilihan User   │
            └───┬──────────────────┘
                ↓
     ┌────────────────────┬─────────────────────┬──────────────────────┬────────────────────┬─────────────────┐
     ↓                    ↓                     ↓                      ↓                    ↓
[Tambah Data]     [Ubah Data]          [Hapus Data]        [Tampilkan Data]       [Cari Data]
     ↓                    ↓                     ↓                      ↓                    ↓
Input nama,      Jika nama ada: ubah   Jika nama ada:    Tampilkan seluruh     Tampilkan data
tugas, uts, uas  nilai & hitung akhir   hapus data       data mahasiswa        mahasiswa
     ↓                    ↓                     ↓                      ↓                    ↓
     └────────────────────┴─────────────────────┴──────────────────────┴────────────────────┴───────┐
                                                                                                    ↓
                                                                                          Keluar?   
                                                                                                    ↓
                                                                                       Ya ───→ Selesai
                                                                                                    ↓
                                                                                                  Tidak
                                                                                                    ↓
                                                                                            Kembali ke Menu
```


# Analisis Program

Program menggunakan dictionary data_mhs untuk menyimpan data mahasiswa.
Setiap mahasiswa memiliki struktur:
```python
{
  "nama": {
     "tugas": xx,
     "uts": xx,
     "uas": xx,
     "akhir": xx
  }
}
```

Program menampilkan menu dan menerima input pengguna untuk:

- Menambah data

- Mengubah data

- Menghapus data

- Mencari data

- Menampilkan seluruh data

Nilai akhir dihitung otomatis melalui:
```python
nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
```
Loop akan terus berjalan sampai user memilih keluar.

# Kesimpulan

Berdasarkan praktikum ini, dictionary terbukti sangat efektif untuk menyimpan data yang berpasangan antara key dan value. Dengan dictionary kita dapat dengan mudah menambah, mengubah, menghapus, serta mencari data. Program pengolahan nilai mahasiswa dapat dibuat lebih sederhana dan dinamis berkat fleksibilitas dictionary. Praktikum ini membantu mahasiswa memahami dasar struktur data dan cara penerapannya dalam program aplikasi sederhana.
            
