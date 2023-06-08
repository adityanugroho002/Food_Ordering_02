import modulfood as mf

while True:
    print("========================================================")
    print("=====================SELAMAT DATANG=====================")
    print("=======================CACA RESTO=======================")
    print("========================================================")
    print("=======Jl. Utara Pasar Besar No.34, Sudiroprajan,=======")
    print("========Kec. Jebres, Kota Surakarta, Jawa Tengah========")
    print("================SILAKAN PILIH MENU BERIKUT==============")
    print("")
    print("                 Klik (1) Program Kasir                 ")
    print("                 Klik (2) Tampilkan Menu                ")
    print("                 Klik (3) Keluar Program                ")
    mulai = input("> ")
    if mulai == "1":
        print("========================================================")
        print("=======================CACA RESTO=======================")
        print("========================================================")
        print("")
        mf.programkasir()

    elif mulai == "2":
        print("========================================================")
        print("=======================CACA RESTO=======================")
        print("========================================================")
        mf.daftarmenu()

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