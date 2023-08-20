import csv
import os
import datetime
import random
import numpy
print("halo")
data_karyawan = "DaftarKaryawan.csv"

def start():
    print("~" * 57)
    print("~\t\t\t| Workaholic |\t\t\t~")
    print("~" * 57)
    print("\t\t\t   | LOGIN |")
    print("Selamat datang di halaman login")
    nama = input("Nama: ")
    sandi = input("Kata Sandi: ")
    if nama == "Bos" and sandi == "111":
        clear()
        menu_bos()
    elif nama == "Karyawan" and sandi == "100":
        clear()
        menu_karyawan()
    else:
        print("Input tidak sesuai")
        konfirmasi = input("Apakah ingin melanjutkan? [y]/[t]")
        if konfirmasi == "y":
            start()
        else:
            print("CLosing Workaholic")

def menu_bos():
    clear()
    print("~" * 57)
    print("~\t\t\t| Menu |\t\t\t~")
    print("~" * 57)
    index = 1
    menu1 = ["Daftar Karyawan", "Tambah Data", "Perbarui Data", "Hapus Data", "Keluar"]
    for menubos in menu1:
        print(str(index) + ". " + menubos)
        index += 1
    selected_menubos = input("Pilih menu: ")
    if selected_menubos == "1": 
        clear()
        id_karyawan()
        back()
    elif selected_menubos == "2": 
        clear()
        tambah()
        back()
    elif selected_menubos == "3":
        clear()
        update()
        back()
    elif selected_menubos == "4":
        clear()
        hapus()
        back()
    elif selected_menubos == "5":
        logout()
    else:
        print("Terjadi Kesalahan")

def id_karyawan():
    data = []
    with open(data_karyawan, "r") as filekry:
        get_data = csv.reader(filekry, delimiter = ",") 
        for row in get_data: 
            data.append(row)
    if (len(data) > 1):
        title = data.pop(0) 
        print("~"*142)
        print(f"|{title[0]:^6}|{title[1]:^30}|{title[2]:^20}|{title[3]:^23}|{title[4]:^33}|{title[5]:^23}|") 
        print("~"*142)
        for i in data:
            print(f"|{i[0]:^6}|{i[1]:^30}|{i[2]:^20}|Rp.{i[3]:^20}|Rp.{i[4]:^30}|Rp.{i[5]:^20}|") 
        print("~"*142)
    else:
        print("Terjadi Kesalahan")

def tambah():
    print("Tambah Data Karyawan Baru")
    NIP = input("NIP: ")
    nama = input("Nama: ")
    jabatan = input("Jabatan: ")
    gaji_pokok = input("Gaji Pokok: ")
    bonus = input("Bonus: ")
    gaji_bersih = int(gaji_pokok) + int(bonus)
    
    with open(data_karyawan, "a+", newline="") as filekry:
        tambah_data = csv.writer(filekry, delimiter = ",")
        data = [NIP, nama, jabatan, gaji_pokok, bonus, gaji_bersih]
        tambah_data.writerow(data)
        print("Data berhasil ditambahkan")
    print("\nBerikut adalah data karyawan terbaru")
    id_karyawan()

def update():
    id_karyawan()
    print("Update Data Karyawan")
    data = []
    with open(data_karyawan, "r") as filekry:
        read_data = csv.DictReader(filekry)
        for baris in read_data:
            data.append(baris)

    pilih = input("Masukkan NIP: ")
    print("~"*57)
    print("Memperbarui Data Karyawan dengan NIP." + pilih) 
    nama = input("Nama: ")
    jabatan = input("Jabatan: ")
    gaji_pokok = input("Gaji Pokok: ")
    bonus = input("Bonus: ")
    gaji_bersih = int(gaji_pokok) + int(bonus)
    
    index = 0
    for j in data:
        if (j["NIP"] == pilih):
            data[index]["Nama"] = nama
            data[index]["Jabatan"] = jabatan
            data[index]["Gaji Pokok"] = gaji_pokok
            data[index]["Bonus"] = bonus
            data[index]["Gaji Bersih"] = gaji_bersih
        index += 1

    with open(data_karyawan, "w", newline = "") as csv_file:
        fieldnames = ["NIP", "Nama", "Jabatan", "Gaji Pokok", "Bonus", "Gaji Bersih"]
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()
        for k in data:
            writer.writerow({
                "NIP": k["NIP"], 
                "Nama": k["Nama"], 
                "Jabatan": k["Jabatan"], 
                "Gaji Pokok": k["Gaji Pokok"], 
                "Bonus": k["Bonus"], 
                "Gaji Bersih": k["Gaji Bersih"]
            })
    print('\nUpdate Data Berhasil !')

def hapus():
    id_karyawan() 
    data = []  
    with open (data_karyawan, "r") as filekry: 
        get_data = csv.DictReader(filekry) 
        for row in get_data: 
            data.append(row) 
    hapus = input("Masukkan NIP Karyawan yang ingin dihapus datanya: ") 
    for row in data:
        if row["NIP"] == hapus:
            data.remove(row) 
    print("\nData Karyawan dengan NIP " + hapus + " berhasil dihapus")

    with open(data_karyawan, "w", newline = "") as filekry: 
        fieldnames = ["NIP", "Nama", "Jabatan", "Gaji Pokok", "Bonus", "Gaji Bersih"]
        writer = csv.DictWriter(filekry, fieldnames=fieldnames) 
        writer.writeheader() 
        for i in data: 
            writer.writerow({
                "NIP": i["NIP"], 
                "Nama": i["Nama"], 
                "Jabatan": i["Jabatan"], 
                "Gaji Pokok": i["Gaji Pokok"], 
                "Bonus": i["Bonus"], 
                "Gaji Bersih": i["Gaji Bersih"]
            }) 

def menu_karyawan():
    print("~" * 57)
    print("~\t\t\t| Menu |\t\t\t~")
    print("~" * 57)
    index = 1
    menu2 = ["Cek Status", "Slip Gaji", "Logout"]
    for menukry in menu2:
        print(str(index) + ". " + menukry)
        index += 1

    selected_menukry = input("Pilih menu: ")
    if selected_menukry == "1":
        clear()
        status()
        back2()
    elif selected_menukry == "2":
        clear()
        slip()
        back2()
    elif selected_menukry == "3":
        logout()
    else:
        print("Terjadi Kesalahan")

def status():
    data = []
    print("~"*70)
    print("~\t\t\t| Status Karyawan |\t\t\t     ~")
    print("~"*70)
    print("|" + " "*68 + "|")
    with open(data_karyawan, "r") as filekry:
        get_data = csv.reader(filekry, delimiter=",")
        for baris in get_data:
            data.append(baris)
    if (len(data_karyawan)>0):
        title = data.pop(0)
        print("-"*70)
        print(f"|{title[0]:^10}|{title[1]:^30}|{title[2]:^26}|")
        print("-"*70)
        for i in data: 
            print(f"|{i[0]:^10}|{i[1]:^30}|{i[2]:^26}|") 
            print('-'*70) 
    else:
        print("Terjadi Kesalahan")
    

def slip():
    data = []
    with open(data_karyawan, "r") as csv_file:
        read_data = csv.DictReader(csv_file)
        for baris in read_data:
            data.append(baris)          
    cetak = input("Masukkan NIP untuk mencetak slip gaji ")
    slip = []
    index = 0
    for i in data:
        if (i["NIP"] == cetak):
            slip = data[index]
        index += 1
    tanggal = datetime.datetime.today()
    ref = random.randint(0, 10000000000)

    if len(slip) > 0:
        print("~"*73)
        print("~\t\t\t\t| Slip Gaji |\t\t\t\t~")
        print("~"*73)
        print("\t\t\t", tanggal)
        print("\t\t\t\tREF.", ref)
        print("~"*73)
        print(f"|NIP      : {slip['NIP']}")
        print(f"|Nama     : {slip['Nama']}")
        print(f"|Jabatan  : {slip['Jabatan']}")
        print("~"*73)
        print(f"| Gaji Pokok  : Rp. {slip['Gaji Pokok']}")
        print(f"| Bonus       : Rp. {slip['Bonus']}")
        print(f"| Gaji Bersih : Rp. {slip['Gaji Bersih']}")
        print("~"*73)
    else:
        print("Data tidak ditemukan")

def logout():
    konfirmasi = input("\nApakah Anda yakin ingin keluar? [y]/[t] ")
    if konfirmasi == "y":
        clear()
        print("~~~~~ Closing Workaholic ~~~~~")
    else:
        clear()
        start()

def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def back():
    input("Tekan Enter untuk kembali ke menu")
    menu_bos()

def back2():
    input("Tekan Enter untuk kembali ke menu")
    clear() 
    menu_karyawan()


start()
