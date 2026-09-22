from datetime import datetime


# Function untuk menghitung biaya
def hitung_biaya(jenis_kamar, lama_menginap):

    if jenis_kamar == "Standard":
        tarif = 200000

    elif jenis_kamar == "Deluxe":
        tarif = 350000

    else:
        print("Jenis kamar tidak ditemukan")
        return 0

    total_biaya = tarif * lama_menginap
    return total_biaya


# Data pemesanan
def pesan_hotel():
    jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
    checkin = input("Masukkan tanggal check-in: ")
    checkout = input("Masukkan tanggal check-out: ")
    lama_menginap = int(input("Masukkan lama menginap: "))

    total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

    print("======= Data Pemesanan Hotel =======")
    print("Jenis Kamar       :", jenis_kamar)
    print("Tanggal Check-in :", checkin)
    print("Tanggal Check-out:", checkout)
    print("Lama Menginap    :", lama_menginap, "malam")
    print("Total Biaya      : Rp", total_biaya)
    
# Menu
while True:
    print("======= Menu =======")
    print("1. Pesan Hotel")
    print("2. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        pesan_hotel()

    elif pilihan == "2":
        print("Sampai Jumpa")
        break

    else:
        print("Pilihan tidak valid")