import csv
namefile = 'daftar_menu.csv'

def daftarmenu():
    with open (namefile) as filecsv:
        readcsv = csv.reader (filecsv,delimiter = ',')
        line_count = 0
        for row in readcsv:
            if line_count == 0:
                print(f'Daftar Menu CACA RESTO:\n{row}')
                line_count += 1
            else:
                line_count += 1
                print(row)
                jumlahdata = int(line_count - 1)
        print("jumlah menu : ", jumlahdata)

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
                
        if pilihanmenu == "1":
            match += 1
            totalpajak = harga_pajak1(totalharga)
            orang = int(input("Jumlah orang: "))
            bayar = str(input("Metode Pembayaran: "))
            if bayar == "cash":
                print("\n===================================")
                print("===============N O T A=============")
                print("========C A C A - R E S T O========")
                print("===================================")
                print("Nama         :", nama)
                print("No WA        : +62", nomor)
                print("Pesanan      :".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    print (pesanan)
                print("jumlah orang :", orang)
                print("Total        : Rp", totalpajak)
                print("Pembayaran dilakukan secara tunai  ")
                print("====== Selamat Datang Kembali======")
                print("===================================")
            elif bayar == "tf":
                print("\n===================================")
                print("===============N O T A=============")
                print("========C A C A - R E S T O========")
                print("===================================")
                print("Nama         :", nama)
                print("No WA        : +62", nomor)
                print("Pesanan      :".format(len(listjmlpesan)))
                for pesanan in listjmlpesan:
                    print (pesanan)
                print("jumlah orang :", orang)
                print("Total        : Rp", totalpajak)
                print("Silakan transfer ke rekening")
                print("BRI         : 213681212")
                print("DANA/Spay   : 081328023385")
                print("segera konfirmasi pembayaran.")
                print("====== Selamat Datang Kembali======")
                print("===================================")
        
        elif pilihanmenu == "2":
            print("""Silahkan Pilih Menu Berikut
            Pilih [1] untuk DELIVERY
            Pilih [2] untuk TAKE AWAY""")
            opsi = int(input("[1] atau [2]: "))
            if opsi == 1:
                alamat = str(input('Input alamat lengkap: '))
                kecamatan = str(input("input kecamatan: "))
                biaya_total = hitung_ongkir_menu(kecamatan, totalharga)
                totalpajak = harga_pajak2(biaya_total)
                bayar = str(input("Metode pembayaran: "))
                if bayar == "cash":
                    print("\n===================================")
                    print("============== N O T A ============")
                    print("======= C A C A - R E S T O =======")
                    print("===================================")
                    print("Nama     :", nama)
                    print("No WA    : +62", nomor)
                    print("Pesanan  :".format(len(listjmlpesan)))
                    for pesanan in listjmlpesan:
                        print (pesanan)
                    print("Alamat   : ", alamat)
                    print("Harga    : Rp", totalpajak)
                    print("              Pajak 10%            ")
                    print("Pembayaran dilakukan secara tunai  ")
                    print("====== Selamat Datang Kembali======")
                    print("===================================")
                    kecamatan.lower
                elif bayar == "tf":
                    print("\n===================================")
                    print("============== N O T A ============")
                    print("======= C A C A - R E S T O =======")
                    print("===================================")
                    print("Nama     :", nama)
                    print("No WA    : +62", nomor)
                    print("Pesanan  :".format(len(listjmlpesan)))
                    for pesanan in listjmlpesan:
                        print (pesanan)
                    print("Alamat   : ", alamat)
                    print("Harga    : Rp", totalpajak)
                    print("              Pajak 10%            ")
                    print("Silakan transfer ke rekening")
                    print("BRI         : 213681212")
                    print("DANA/Spay   : 081328023385")
                    print("segera konfirmasi pembayaran.")
                    print("====== Selamat Datang Kembali======")
                    print("===================================")
                    kecamatan.lower

            elif opsi == 2:
                bayar = str(input("Metode pembayaran: "))     
                if bayar == "cash":
                    totalpajak = harga_pajak1(totalharga)
                    print("\n===================================")
                    print("===============N O T A=============")
                    print("========C A C A - R E S T O========")
                    print("===================================")
                    print("Nama     :", nama)
                    print("No WA    : +62", nomor)
                    print("Pesanan  :".format(len(listjmlpesan)))
                    for pesanan in listjmlpesan:
                        print (pesanan)
                    print("Harga    : Rp", totalpajak)
                    print(f"silahkan ambil pesanan anda dalam {jml_pesan*10} menit")
                    print("              Pajak 10%            ")
                    print("Pembayaran dilakukan secara tunai  ")
                    print("====== Selamat Datang Kembali======")
                    print("===================================")
                elif bayar == "tf":
                    totalpajak = harga_pajak1(totalharga)
                    print("\n===================================")
                    print("===============N O T A=============")
                    print("========C A C A - R E S T O========")
                    print("===================================")
                    print("Nama     :", nama)
                    print("No WA    : +62", nomor)
                    print("Pesanan  :".format(len(listjmlpesan)))
                    for pesanan in listjmlpesan:
                        print (pesanan)
                    print("Harga    : Rp", totalpajak)
                    print(f"silahkan ambil pesanan anda dalam {jml_pesan*10} menit")
                    print("              Pajak 10%            ")
                    print("Silakan transfer ke rekening")
                    print("BRI         : 213681212")
                    print("DANA/Spay   : 081328023385")
                    print("segera konfirmasi pembayaran.")
                    print("====== Selamat Datang Kembali======")
                    print("===================================")

            else:
                print("Input tidak valid")

        if match == ("a"):
            print ("Input salah, ulangi input")
        pilihanmenu = input("Kode makanan dipesan: ")

while True:
    print("================================================")
    print("=================SELAMAT DATANG=================")
    print("===================CACA RESTO===================")
    print("================================================")
    print("==========SILAKAN PILIH MENU BERIKUT============")
    print("")
    print("           Klik (1) Program Kasir               ")
    print("           Klik (2) Tampilkan Menu              ")
    print("           Klik (3) Keluar Program              ")
    mulai = input("> ")
    if mulai == "1":
        print("=========================================")
        print("===============CACA RESTO================")
        print("=========================================")
        print("")
        nama = str(input("Ketik Nama Anda:"))
        nomor = int(input("Ketik Nomor WhatsApp Anda: "))
        programkasir()

    elif mulai == "2":
        print("=========================================")
        print("===============CACA RESTO================")
        print("=========================================")
        daftarmenu()

    elif mulai == ("3"):
        print ("")
        print ("PROGRAM TERHENTI!")
        print ("")
        break 

    else:
        print ("")
        print ("Input SALAH!")
        print ("PROGRAM TERHENTI!")
        print ("")
        break