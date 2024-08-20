print("======================================")
print("======= ATM BANK CIPTA FAMILY ========")
print("======================================")
print("SELAMAT DATANG DI BANK CIPTA FAMILY")

saldo = 1000000

print()
print("Pilih Menu :")
print("1. Cek Saldo \n2. Isi Saldo \n3. Ambil Uang \n4. Transfer Uang \n5. Donasi")
print()

plh = int(input("Masukkan Pilihan :"))
print("=======================================")

if plh == 1:
    print("Saldo yang anda miliki adalah Rp{}".format(saldo))
    print("===================================")
elif plh== 2:
    print("Isi Saldo !")
    nominal = int(input("Masukkan Nominal (kelipatan 50.000) : Rp"))
    if nominal < 50000:
        print("Nominal yang anda masukkan kurang!")
        print("===================================")
    else:
        proses = saldo + nominal
        print("Saldo anda berhasil diisi Rp{}".format(nominal))
        print("Total Saldo anda adalah : Rp{}".format(proses))
        print("===================================")

elif plh == 3:
    print("Ambil Uang!")
    nominal = int(input("Masukkan Nominal :"))
    if nominal > 1000000:
        print("Nominal yang anda masukkan tidak mencukupi!")
        print("====================================")

    elif nominal < 50000:
        print("Nominal yang anda masukkan Salah!")
        print("====================================")
        
    else:
        proses = saldo - nominal
        print("Saldo anda berhasil diambil Rp{}".format(nominal))
        print("Saldo Sisa : Rp{}".format(proses))
        print("====================================")

elif plh == 4:
    print("Transfer Uang!")
    print("Masukkan Tujuan !")
    nama = str(input("Nama     :"))
    no = int(input("No Rekening :"))
    nominal = int(input("Masukkan Nominal :"))
    if nominal > 1000000:
        print("Nominal yang anda masukkan Tidak Cukup!")
        print("========================================")
    elif nominal < 50000:
        print("Nominal yang anda masukkan Salah")
        print("========================================")
    else: 
        proses = saldo - nominal
        print("Anda Berhasil Transfer ke {} Sebesar Rp".format(nama) ,nominal)
        print("Saldo Sisa Anda Adalah : Rp{}".format(proses))

elif plh == 5:
    print("Donasi!")
    print("Masukkan Tujuan !")
    nama = str(input("Nama     :"))
    no = int(input("No Rekening :"))
    nominal = int(input("Masukkan Nominal :"))
    pesan = str(input("Pesan :"))
    if nominal > 1000000:
        print("Nominal yang anda masukkan Tidak Cukup!")
        print("=======================================")
    elif nominal < 50000:
        print("Nominal yang anda masukkan Salah!")
        print("========================================")
    else:
        proses = saldo - nominal
        print("Anda Berhasil Donasi ke {} Sebesar Rp".format(nama) ,nominal)
        print("Saldo Sisa Anda Adalah : Rp{}".format(proses))
        print("========================================")










         


   
