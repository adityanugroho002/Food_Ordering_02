import csv
import os

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

print("=========================================")
print("===============CACA RESTO================")
print("=========================================")
daftarmenu()