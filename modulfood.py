import csv
from tabulate import tabulate

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

def programkasir():
    with open(namefile, newline='') as filecsv:
        reader = csv.reader(filecsv)
        datamenu = list(reader)
    nama = str(input("Ketik Nama Anda: "))
    nomor = int(input("Ketik Nomor WhatsApp Anda: "))
    daftarmenu()
    totalharga = 0
    listjmlpesan= []
    print ("")
    print ("Masukkan KODE berikut pada 'Kode Makanan dipesan' apabila selesai memilih menu:")
    print ("Input (1) untuk TOTAL PEMBAYARAN")
    print ("Input (2) untuk Keluar dari Program Kasir")
    print ("")
    pilihanmenu = input("Kode makanan dipesan: ")
    while pilihanmenu != ("2"):
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
                menu = [i[1], jml_pesan,hargamenu]
                
                listjmlpesan.append(menu)
                print (listjmlpesan)
                
        if pilihanmenu == "1":
            match += 1
            pajak = totalharga*1.1
            print ("Total Pembelian: Rp ", totalharga)
            print("\n===================================")
            print("===============N O T A=============")
            print("========C A C A - R E S T O========")
            print("===================================")
            print("Nama     : ", nama)
            print("No WA    : +62", nomor)
            print("Pesanan  :".format(len(listjmlpesan)))
            for pesanan in listjmlpesan:
                print (pesanan)
            print("Total    : Rp", pajak)
            print("====== Selamat Datang Kembali======")
            print("===================================")  
        if match == ("a"):
            print ("Input salah, ulangi input")
        pilihanmenu = input("Kode makanan dipesan: ")