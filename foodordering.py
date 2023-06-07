import csv

namefile = 'daftar_menu.csv'

def daftarmenu():
    with open (namefile) as filecsv:
        readcsv = csv.reader (filecsv,delimiter = ',')
        line_count = 0
        for row in readcsv:
            if line_count == 0:
                print(f'menu:\n{row}')
                line_count += 1
            else:
                line_count += 1
                print(row)
                jumlahdata = int(line_count - 1)
        print("jumlah menu : ", jumlahdata)

def programkasir():
    with open(namefile, newline='') as filecsv:
        reader = csv.reader(filecsv)
        datamenu = list(reader)

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

while True:
    print("================================================")
    print("=================SELAMAT DATANG=================")
    print("===================CACA RESTO===================")
    print("================================================")
    print("==========SILAKAN PILIH MENU BERIKUT============")
    print("")
    print("           Klik (1) Program Kasir               ")
    print("           Klik (2) Tampilkan Menu              ")
    mulai = input("> ")
    if mulai == "1":
        print("=========================================")
        print("===============CACA RESTO================")
        print("=========================================")
        print("")
        nama = str(input("Ketik Nama Anda: "))
        nomor = int(input("Ketik Nomor WhatsApp Anda: "))
        programkasir()
    elif mulai == "2":
        print("=========================================")
        print("===============CACA RESTO================")
        print("=========================================")
        daftarmenu()

