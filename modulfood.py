import csv
from tabulate import tabulate
import random

namefile = 'daftar_menu.csv'

def daftarmenu():
    data = []
    with open (namefile) as filecsv:
        readcsv = csv.reader (filecsv,delimiter = ',')
        data = list(readcsv)
    headers = data[0]
    tablefmt = "grid"
    numalign = "center"

    table = tabulate(data[1:], headers=headers, tablefmt=tablefmt, numalign=numalign)
    print(table)

def hitung_ongkir_menu(kecamatan, totalharga):
    ongkir = 0
    
    if kecamatan == "jebres" or "banjarsari" or "laweyan" or "serengan" or "pasar kliwon":
        ongkir = 5000
    elif kecamatan == "mojosongo" or "grogol":
        ongkir = 7000
    elif kecamatan == "colomadu" or "ngemplak":
        ongkir = 10000
    else:
        print("kecamatan tidak valid.")
    
    total_biaya = ongkir + totalharga
    return total_biaya

def kodekupon(kode, totalharga):
    kupon = 0
    if kode == "caca0214":
        kupon = 5000
    elif kode == "caca2728":
        kupon = 7000
    else:
        kupon = 0
    hargakupon = totalharga - kupon
    return hargakupon

def metode_transfer(norek_resto, no_telepon, totalharga):
    valid_input = False
    while not valid_input:
        nomor_rekening = input("Input nomor rekening tujuan: ")
        if nomor_rekening == norek_resto or nomor_rekening == no_telepon:
            valid_harga = False
            while not valid_harga:
                totalbayar = float(input("Masukkan total pembayaran: "))
                if totalbayar == totalharga:
                    valid_harga = True
                    valid_input = True
                else:
                    print("Tidak valid")
        else:
            print("nomor rekening tidak valid")
    return True

def harga_pajak1(totalharga):
    pajak = totalharga * 0.1
    totalpajak = totalharga + pajak
    return totalpajak

def harga_pajak2(biaya_total):
    pajak = biaya_total * 0.1
    totalpajak = biaya_total + pajak
    return totalpajak

def programkasir():
    with open(namefile, newline='') as filecsv:
        reader = csv.reader(filecsv)
        datamenu = list(reader)
    nama = str(input("Ketik Nama Anda: "))
    while True:
        try:
            nomor_telepon = int(input("Masukkan nomor telepon: "))
            break
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
    print("Nomor telepon yang dimasukkan:", nomor_telepon)

    daftarmenu()
    totalharga = 0
    listjmlpesan= []
    print ("")
    print ("Masukkan KODE berikut pada 'Kode Makanan dipesan' apabila selesai memilih menu:")
    print ("Input (1) untuk DINE IN")
    print ("Input (2) untuk DELIVERY/TAKE AWAY")
    print ("Input (3) untuk Keluar dari Program Kasir")
    print ("")
    pilihanmenu = input("Kode makanan dipesan: ")
    while pilihanmenu != ("3"):
        match = 0
        for i in datamenu:
            if pilihanmenu == i[0]:
                match += 1
                try:
                    jml_pesan = int(input("Jumlah dipesan: "))
                except ValueError:
                    print ("Input salah. Masukkan jumlah pesanan")
                    jml_pesan = int(input("Jumlah dipesan: "))
                hargamenu = int(i[2])*jml_pesan
                totalharga += hargamenu
                print (i[1],"\t Rp",hargamenu)
                entry = [i[1], jml_pesan,hargamenu]
                listjmlpesan.append(entry)
                print (listjmlpesan)
                estimasi = int(i[3])*jml_pesan
                
        if pilihanmenu == "1":
            match += 1
            totalpajak = harga_pajak1(totalharga)
            orang = int(input("Jumlah orang: "))
            nomormeja = random.randint(1,10)
            kode = str(input("KODE KUPON (input 0 jika tidak ada): "))
            harga_akhir = kodekupon(kode, totalpajak)
            print("\n===================================")
            print("===============N O T A=============")
            print("========C A C A - R E S T O========")
            print("===================================")
            print("Nama         :", nama)
            print("No WA        : +62", nomor_telepon)
            print("Pesanan      :".format(len(listjmlpesan)))
            for pesanan in listjmlpesan:
                print (pesanan)
            print("Nomor Meja   :", nomormeja)
            print("Jumlah orang :", orang)
            print("Harga menu   : ", totalharga)
            print("Pajak        : 10%")
            print("Total        : Rp", harga_akhir)
            print("Silahkan melakukan pembayaran")
            print("====== Selamat Datang Kembali======")
            print("===================================")
            print("")
            print("Silahkan pilih Metode Pembayaran")
            print("[1] Cash               ")
            print("[2] Transfer >> BCA              : 123456789")
            print("                Dana/Spay/Gopay  : 081328023385")
            choice = str(input(">> "))
            if choice == "1":
                print("------------------------------------")
                print("Mohon untuk membayar dengan uang pas")
                print("------------------------------------")
            elif choice == "2":
                norek_resto = "123456789"
                no_telepon = "081328023385"
                totalbayar = harga_akhir                
                if metode_transfer(norek_resto, no_telepon, totalbayar):
                    print("--------------------")
                    print(" Transaksi berhasil ")
                    print("--------------------")
                else:
                    print("-----------------")
                    print(" Transaksi gagal ")
                    print("-----------------")


        elif pilihanmenu == "2":
            match += 1
            print("""Silahkan Pilih Menu Berikut
            Pilih [1] untuk DELIVERY
            Pilih [2] untuk TAKE AWAY""")
            opsi = int(input("[1] atau [2]: "))
            if opsi == 1:
                alamat = str(input('Input alamat lengkap: '))
                kecamatan = str(input("input kecamatan: "))
                biaya_total = hitung_ongkir_menu(kecamatan, totalharga)
                totalpajak = harga_pajak2(biaya_total)
                kode = str(input("KODE KUPON (input 0 jika tidak ada): "))
                harga_akhir = kodekupon(kode, totalpajak)
                print("\n===================================")
                print("============== N O T A ============")
                print("======= C A C A - R E S T O =======")
                print("===================================")
                print("Nama     :", nama)
                print("No WA    : +62", nomor_telepon)
                print("Pesanan  :".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    print (pesanan)
                print("Alamat   : ", alamat)
                print("Harga    : Rp", harga_akhir)
                print("              Pajak 10%            ")
                print("Silahkan melakukan pembayaran")
                print("====== Selamat Datang Kembali======")
                print("===================================")
                kecamatan.lower
                print("")
                print("Silahkan pilih Metode Pembayaran")
                print("[1] Cash               ")
                print("[2] Transfer >> BCA              : 123456789")
                print("                Dana/Spay/Gopay  : 081328023385")
                choice = str(input(">> "))
                if choice == "1":
                    print("------------------------------------")
                    print("Mohon untuk membayar dengan uang pas")
                    print("------------------------------------")
                elif choice == "2":
                    norek_resto = "123456789"
                    no_telepon = "081328023385"
                    totalbayar = harga_akhir                
                    if metode_transfer(norek_resto, no_telepon, totalbayar):
                        print("--------------------")
                        print(" Transaksi berhasil ")
                        print("--------------------")
                    else:
                        print("-----------------")
                        print(" Transaksi gagal ")
                        print("-----------------")

            elif opsi == 2:
                totalpajak = harga_pajak1(totalharga)
                kode = str(input("KODE KUPON (input 0 jika tidak ada): "))
                harga_akhir = kodekupon(kode, totalpajak)
                print("\n=================================================")
                print("====================N O T A======================")
                print("=============C A C A - R E S T O=================")
                print("=================================================")
                print("Nama     :", nama)
                print("No WA    : +62", nomor_telepon)
                print("Pesanan  :".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    print (pesanan)
                print("Harga    : Rp", harga_akhir)
                print(f"silahkan ambil pesanan anda dalam {estimasi} menit")
                print("              Pajak 10%            ")
                print("Pembayaran dilakukan secara tunai  ")
                print("=========== Selamat Datang Kembali================")
                print("==================================================")
                print("")
                print("Silahkan pilih Metode Pembayaran")
                print("[1] Cash               ")
                print("[2] Transfer >> BCA              : 123456789")
                print("                Dana/Spay/Gopay  : 081328023385")
                choice = str(input(">> "))
                if choice == "1":
                    print("------------------------------------")
                    print("Mohon untuk membayar dengan uang pas")
                    print("------------------------------------")
                elif choice == "2":
                    norek_resto = "123456789"
                    no_telepon = "081328023385"
                    totalbayar = harga_akhir                
                    if metode_transfer(norek_resto, no_telepon, totalbayar):
                        print("--------------------")
                        print(" Transaksi berhasil ")
                        print("--------------------")
                    else:
                        print("-----------------")
                        print(" Transaksi gagal ")
                        print("-----------------")

            else:
                print("Input tidak valid")

        if match == ("a"):
            print ("Input salah, ulangi input")
        pilihanmenu = input("Kode makanan dipesan: ")