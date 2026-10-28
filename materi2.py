def sapa():
    print("Halo, siswa!")

sapa()

def sapa(nama):
    print("Halo,", nama)

sapa("Andi")
sapa("Budi")

def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print(hasil)

def cek_nilai(nilai):
    if nilai >= 75:
        print("Lulus")
    else:
        print("Tidak Lulus")

cek_nilai(80)

def a():
    print("Ini adalah fungsi a")
    
makanan = ["Nasi Goreng", "Mie Ayam", "Sate"]
nilai = [80, 90, 70]
boolean = [True, False, True]

print(makanan)

buah = ["Apel", "Anggur", "Pisang"]
print(buah[0])  # Output: Apel

nilai_1 = [80, 90, 70]
nilai_1[0] = 85
print(nilai_1)

buah_1 = ["Apel", "Anggur", "Pisang"]
buah_1.append("Jeruk")
print(buah_1)

buah_2 = ["Apel", "Anggur", "Pisang"]
buah_2.remove("Anggur")
print(buah_2)

buah_3 = ["Apel", "Anggur", "Pisang", "Jeruk"]
jumlah_buah = len(buah_3)
print(jumlah_buah)