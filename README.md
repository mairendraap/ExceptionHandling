# Laporan Praktikum 6

Repository ini berisi hasil pengerjaan Praktikum 6 yang berfokus pada implementasi *Exception Handling* (`try-except`), manipulasi string/regex, serta (membaca dan menulis file `.txt`) menggunakan Python.

## Exercise 1
Pada bagian ini berisi implementasi fungsi pembacaan input angka dengan validasi *range* tertentu.
- **Catatan:** Sesi QnA Praktikum (Herdan kebingungan) - mencoba *recode* kode dari punya Habibi untuk mengecek batasan nilai (batas bawah dan batas atas) menggunakan perulangan dan *exception handling*.

## Exercise 2
Pada latihan ini, fokus utama adalah pencarian pola atau kata yang tersembunyi (Subsequence) di dalam sebuah teks acak.
- **Catatan:** Trial and error, coba melatih *logic* untuk mencocokkan inputan *hidden word* dengan teks acak, serta melacak posisi indeks karakter tersebut jika ditemukan secara berurutan.

## Exercise 3
Latihan ini berfokus pada pembuatan sistem bank sederhana berbasis *Command Line Interface* (CLI) yang terhubung dengan file teks.
1. Membuat file `accounts.txt` dengan isi data akun (ID, Nama, PIN, Saldo) yang sudah ditentukan.
2. Melakukan *crosscheck* untuk memastikan isi file sudah benar dan bisa dipanggil/dibaca oleh program.

### Catatan Pengerjaan Exercise 3:
Nah ini, untuk khusus yang Exercise 3 ini cukup menguras tenaga dan pikiran karena memang instruksi yang diminta dan output yang ditampilkan lumayan kompleks, ini saya buat untuk mempertajam kemampuan *logic* saya khususnya di *conditional statement*. 

Mulai dari baris pertama kode ini, terutama kita perlu memanggil file `accounts.txt` yang sudah kita buat sebelumnya, *read* dan memasukkannya ke dalam variabel data agar dapat diproses nantinya, dan kemudian membuat sebuah fungsi sistem bank (`def bank_system()`). Kemudian untuk *for loop* disana saya lumayan bingung awalnya dan setelah kelas teori tadi saya *recall* materi tentang *dictionary* dan *indexing*. Sesuai yang dijelaskan saat kelas teori, terdapat beberapa grup dari *list* yang kemudian dirubah ke dalam bentuk *dict*. 

Dari logika pemrosesan itu full menguras tenaga karena harus memikirkan *logic* program agar semua berjalan terstruktur. Tadi saya sempat *error* terus karena ada beberapa *syntax error*, *logic error* juga sempat ada karena salah penyusunan alhasil ter-*looping* terus menerus. 

Disini saya mau menjelaskan sedikit yang lumayan *tricky* ada di variabel `transaction_success`. Kenapa *tricky*? Karena di setiap *conditional statement* disana akan menyimpan variable `transaction_success`, apabila `True` dia akan segera eksekusi untuk memasukkan/update data ke dalam `accounts.txt`, serta menampilkan *closing message*.

**Eksperimen Tambahan:**
Mencoba menggunakan metode *dictionary* dan RegEx (Regular Expression) dari contoh kode Ibu Lely, namun sempat menemui kendala/error (`"dict object is not callable"`).

## Exercise 4
Implementasi *exception handling* sederhana menggunakan identitas diri.

### Catatan Pengerjaan Exercise 4:
Untuk Exercise 4 ini saya membuat program yang sangat amat simpel sekali, karena di instruksi harus menggunakan 1 *exception handling*. Jadi saya buat sebuah program untuk mengenali saya dengan *conditional statement*. Saya pertajam lagi *conditional statement* saya, sebenarnya mau bikin *full* `if-else` untuk mempertajam logika *conditional* saya, tetapi karena diminta menggunakan *exception handling* jadi saya buat program sederhana dengan blok `try-except` untuk menangkap potensi *error*.