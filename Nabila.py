print('SELAMAT DATANG DI ATM BANK CIPTA')
print('PILIH OPTION')
print('1. check uang saya')
print('2. ambil uang saya')
print('3. tabung uang saya')
option=int(input('silahkan pilih option'))
uang_kamu=250000
if option==1:
    print('uang saya berjumlah Rp. 250.000')
elif option==2:
    print('uang saya berjumlah Rp. 250.000, mau ambil berapa?')
    print('1. Rp. 50.000')
    print('2. Rp. 100.000')
    print('3. Rp. 200.000')
    option2=int(input('option:'))
    if option2==1:
        hasil=uang_kamu-200000
        print('uang kamu sekarang berjumlah ',hasil)
    elif option2==2:
        hasil2=uang_kamu-150000
        print('uang kamu sekarang berjumlah ',hasil2)
        if option3==3:
            hasil3=uang_kamu-50000
            print('uang kamu sekarang berjumlah ',hasil3)
        else:
            print('keyword anda salah, mohon ulangi lagi!')
        elif option==3:
ptint('uang saya berjumlah Rp. 250.000, mau tabung berapa?')
opyion3=int(input('masukkan jumlah uang:'))
hasil3=uang_kamu+option3
print('jumlah uang kamu sekarang adalah',hasil3)
else:
print("pilihan anda salah, silahkan ulangi lagi!")
        

