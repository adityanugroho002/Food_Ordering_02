import csv
from tabulate import tabulate
import datetime

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

def database_meja(database):
    with open("data_meja.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nomor Meja"])  # Menulis header
        for nomor_meja in database:
            writer.writerow([nomor_meja])

def baca_database():
    database = []
    try:
        with open("data_meja.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Melompati baris header
            for row in reader:
                nomor_meja = int(row[0])
                database.append(nomor_meja)
    except FileNotFoundError:
        return database
    return database

def pesan_nomor_meja():
    global nomor_meja
    database = baca_database()
    nomor_meja = int(input("Masukkan nomor meja: "))
    while nomor_meja in database or nomor_meja > 10:
        if nomor_meja in database:
            print("Nomor meja telah dipesan. Silakan pilih nomor meja lain.")
        elif nomor_meja > 10:
            print("Meja tidak tersedia.")
        nomor_meja = int(input("Masukkan nomor meja: "))
    database.append(nomor_meja)
    database_meja(database)
    print("Nomor meja berhasil dipesan.")

def hitung_ongkir_menu(kecamatan, totalharga):
    global ongkir
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
    global kupon 
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
            pesan_nomor_meja()
            kode = str(input("KODE KUPON (input 0 jika tidak ada): "))
            harga_akhir = kodekupon(kode, totalpajak)
            tanggal = datetime.date.today()
            tanggal_pesan = tanggal.strftime("%d/%m/%Y")
            nama_file = "data_struk.txt" 
            with open(nama_file, 'a') as file:
                file.write("\n===================================\n")
                file.write("===============N O T A=============\n")
                file.write("========C A C A - R E S T O========\n")
                file.write("===================================\n")
                file.write("Tanggal      : {}\n".format(tanggal_pesan))
                file.write("Nama         : {}\n".format(nama))
                file.write("No WA        : +62 {}\n".format(nomor_telepon))
                file.write("Pesanan      : \n".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    file.write(str(pesanan))
                file.write("\nNomor Meja   : {}\n".format(nomor_meja))
                file.write("Jumlah orang : {}\n".format(orang))
                file.write("Harga menu   : Rp {}\n".format(totalharga))
                file.write("Pajak        : 10%\n")
                file.write("Kupon        : -Rp {}\n".format(kupon))
                file.write("Total        : Rp {}\n".format(harga_akhir))
                file.write("Silahkan melakukan pembayaran\n")
                file.write("====== Selamat Datang Kembali======\n")
                file.write("===================================\n")
            print("\n===================================")
            print("===============N O T A=============")
            print("========C A C A - R E S T O========")
            print("===================================")
            print("Nama         :", nama)
            print("No WA        : +62", nomor_telepon)
            print("Pesanan      :".format(len(listjmlpesan)))
            for pesanan in listjmlpesan:
                print (pesanan)
            print("Nomor Meja   :", nomor_meja)
            print("Jumlah orang :", orang)
            print("Harga menu   : Rp", totalharga)
            print("Pajak        : 10%")
            print("Kupon        : -Rp", kupon)
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
                exit()
            elif choice == "2":
                norek_resto = "123456789"
                no_telepon = "081328023385"
                totalbayar = harga_akhir                
                if metode_transfer(norek_resto, no_telepon, totalbayar):
                    print("--------------------")
                    print(" Transaksi berhasil ")
                    print("--------------------")
                    exit()
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
                tanggal = datetime.date.today()
                tanggal_pesan = tanggal.strftime("%d/%m/%Y")
                nama_file = "data_struk.txt"
                with open(nama_file, 'a') as file:
                    file.write("\n===================================\n")
                    file.write("============== N O T A ============\n")
                    file.write("======= C A C A - R E S T O =======\n")
                    file.write("===================================\n")
                    file.write("Tanggal      : {}\n".format(tanggal_pesan))
                    file.write("Nama         : {}\n".format(nama))
                    file.write("No WA        : +62 {}\n".format(nomor_telepon))
                    file.write("Alamat       : {}\n".format(alamat))
                    file.write("Pesanan      : \n".format(len(listjmlpesan)))
                    for pesanan in listjmlpesan:
                        file.write(str(pesanan))
                    file.write("\nHarga Menu   : Rp {}\n".format(totalharga))
                    file.write("Ongkir       : Rp {}\n".format(ongkir))
                    file.write("Pajak        : 10%\n")
                    file.write("Kupon        : - Rp {}\n".format(kupon))
                    file.write("Total Harga  : Rp {}\n".format(harga_akhir))
                    file.write("Silahkan melakukan pembayaran\n")
                    file.write("====== Selamat Datang Kembali======\n")
                    file.write("===================================\n")
                    
                print("\n===================================")
                print("============== N O T A ============")
                print("======= C A C A - R E S T O =======")
                print("===================================")
                print("Nama         :", nama)
                print("No WA        : +62", nomor_telepon)
                print("Alamat       : ", alamat)
                print("Pesanan      :".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    print (pesanan)
                print("Harga Menu   : Rp", totalharga)
                print("Ongkir       : Rp", ongkir)
                print("Pajak        : 10%")
                print("Kupon        : - Rp", kupon)
                print("Total Harga  : Rp", harga_akhir)
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
                    exit()
                elif choice == "2":
                    norek_resto = "123456789"
                    no_telepon = "081328023385"
                    totalbayar = harga_akhir                
                    if metode_transfer(norek_resto, no_telepon, totalbayar):
                        print("--------------------")
                        print(" Transaksi berhasil ")
                        print("--------------------")
                        exit()
                    else:
                        print("-----------------")
                        print(" Transaksi gagal ")
                        print("-----------------")

            elif opsi == 2:
                totalpajak = harga_pajak1(totalharga)
                kode = str(input("KODE KUPON (input 0 jika tidak ada): "))
                harga_akhir = kodekupon(kode, totalpajak)
                tanggal = datetime.date.today()
                tanggal_pesan = tanggal.strftime("%d/%m/%Y")
                nama_file = "data_struk.txt"
                with open(nama_file, 'a') as file:
                    file.write("\n=================================================\n")
                    file.write("====================N O T A======================\n")
                    file.write("=============C A C A - R E S T O=================\n")
                    file.write("=================================================\n")
                    file.write("Tanggal      : {}\n".format(tanggal_pesan))
                    file.write("Nama         : {}\n".format(nama))
                    file.write("No WA        : +62 {}\n".format(nomor_telepon))
                    file.write("Pesanan      : \n".format(len(listjmlpesan)))
                    for pesanan in listjmlpesan:
                        file.write(str(pesanan))
                    file.write("\nHarga Menu   : Rp {}\n".format(totalharga))
                    file.write("pajak        : 10%\n")
                    file.write("Kupon        : -Rp {}\n".format(kupon))
                    file.write("Total Harga  : Rp {}\n".format(harga_akhir))
                    file.write(f"silahkan ambil pesanan anda dalam {estimasi} menit\n")
                    file.write("Pembayaran dilakukan secara tunai\n")
                    file.write("=========== Selamat Datang Kembali================\n")
                    file.write("==================================================\n")
                print("\n=================================================")
                print("====================N O T A======================")
                print("=============C A C A - R E S T O=================")
                print("=================================================")
                print("Nama         :", nama)
                print("No WA        : +62", nomor_telepon)
                print("Pesanan      :".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    print (pesanan)
                print("Harga Menu   : Rp", totalharga)
                print("pajak        : 10%")
                print("Kupon        : -Rp", kupon)
                print("Total Harga  : Rp", harga_akhir)
                print(f"silahkan ambil pesanan anda dalam {estimasi} menit")
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
                    exit()
                elif choice == "2":
                    norek_resto = "123456789"
                    no_telepon = "081328023385"
                    totalbayar = harga_akhir                
                    if metode_transfer(norek_resto, no_telepon, totalbayar):
                        print("--------------------")
                        print(" Transaksi berhasil ")
                        print("--------------------")
                        exit()
                    else:
                        print("-----------------")
                        print(" Transaksi gagal ")
                        print("-----------------")

            else:
                print("Input tidak valid")

        if match == ("a"):
            print ("Input salah, ulangi input")
        pilihanmenu = input("Kode makanan dipesan: ")