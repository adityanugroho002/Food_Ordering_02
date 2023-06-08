import modulfood as mf

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
        mf.programkasir()
    elif mulai == "2":
        print("=========================================")
        print("===============CACA RESTO================")
        print("=========================================")
        mf.daftarmenu()

