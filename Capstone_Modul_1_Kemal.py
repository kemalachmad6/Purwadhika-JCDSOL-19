import math

list_sewa = [
    {'tipe': 'Toyota Innova',   'tarif': 500000, 'durasi': 2},
    {'tipe': 'Honda Brio',      'tarif': 250000, 'durasi': 4},
    {'tipe': 'Daihatsu Sigra',  'tarif': 300000, 'durasi': 7}
]

dict_admin = {
    'admin1': '1234', 'admin2': '3456', 'admin3': '5678'
}

cart = []

# Fungsi untuk menampilkan daftar kendaraan
def show_unit():
    print('Daftar Kendaraan \n')
    print('No | Tipe Unit  \t | Tarif Sewa (Rp)\t | Durasi Tersedia (Hari)')
    for i in range(len(list_sewa)):
        print(f'{i+1}  | {list_sewa[i]["tipe"]}  \t | {list_sewa[i]["tarif"]}\t\t | {list_sewa[i]["durasi"]}')

# Fungsi untuk menjalankan proses sewa
def menu_sewa():
    show_unit()

    while True:
        input_no = int(input('Masukkan nomor unit: '))
        input_dur = int(input('Masukkan durasi sewa: '))
        mobil = list_sewa[input_no-1]
        
        if input_dur > mobil['durasi']: 
            print(f'Maaf, durasi sewa untuk Unit {mobil["tipe"]} hanya tersedia {mobil["durasi"]} hari.')
            input_dur = mobil['durasi'] # Jika durasi input > durasi tersedia: otomatis ubah durasi input = durasi tersedia
            print(f'Durasi sewa disesuaikan menjadi {input_dur} hari.')
        
        cart.append({'no': input_no-1, 'tipe': mobil['tipe'], 'tarif': mobil['tarif'], 'durasi': input_dur}) 
        mobil['durasi'] -= input_dur # Update durasi sewa pada list

        print('Keranjang Sewa: ')
        print('Tipe Unit \t\t | Tarif Sewa (Rp)\t | Durasi Sewa (Hari)')
        for j in cart:
            print(f"{j['tipe']} \t\t | {j['tarif']}\t\t | {j['durasi']}")

        pilihan = input("Ingin menambah unit sewa lain? (ya/tidak): ")
        if pilihan.lower() == 'tidak':
            break

    print('Rincian Sewa: ')
    print('Tipe Unit \t\t | Durasi (Hari)\t | Tarif (Rp)\t| Total Tarif')
    total_tarif = 0
    for j in cart:
        print(f"{j['tipe']} \t\t | {j['durasi']} \t\t\t | {j['tarif']}\t| {(j['durasi']*j['tarif'])}")
        total_tarif += (j['durasi']*j['tarif'])
    
    while True:
        print(f"Total yang harus dibayar = Rp{total_tarif}")
        bayar = int(input("Masukkan jumlah pembayaran: "))
        if bayar > total_tarif:
            print(f"Terima kasih! \nKembalian anda: Rp{bayar - total_tarif}")
            cart.clear()
            break
        elif bayar == total_tarif:
            print("Terima kasih!")
            cart.clear() 
            break
        else:
            print(f"Transaksi gagal. \nNominal pembayaran kurang sebesar Rp{int(math.fabs(bayar - total_tarif))}")

# Fungsi untuk validasi akses login admin
def menu_login():
    login_berhasil = False

    while not login_berhasil:
        username = input('Masukkan username anda: ')
        password = input('Masukkan password anda: ')

        # Cek apakah username ada di dict_admin dan passwordnya sesuai
        if username in dict_admin and dict_admin[username] == password:
            login_berhasil = True
            print(f"Login berhasil! Selamat datang, {username}.")
        else:
            print('Username atau password yang anda masukkan salah.')

    return username

# Fungsi untuk menjalankan menu 1 admin (Tambah Unit)
def adm_menu_1():
    show_unit()
    tipe_new = input('Masukkan tipe kendaraan: ')
    tarif_new = int(input('Masukkan tarif sewa: '))
    durasi_new = int(input('Masukkan durasi sewa: '))
    list_sewa.append(
        {'tipe': tipe_new.title(), 
            'tarif': tarif_new, 
            'durasi': durasi_new})
    show_unit()

# Fungsi untuk menjalankan menu 2 admin (Hapus Unit)
def adm_menu_2():
    show_unit()
    hapus = int(input('Masukkan nomor unit yang ingin dihapus: '))
    del list_sewa[hapus-1]
    show_unit()

# Fungsi untuk menjalankan menu 3 admin (Update Durasi)
def adm_menu_3():
    show_unit()
    x = int(input('Masukkan nomor unit yang ingin diupdate: '))
    y = int(input('Masukkan durasi: '))
    list_sewa[x-1]['durasi'] = y
    show_unit()

# Fungsi untuk menjalankan menu admin
def menu_admin(username):
    while True:
        adm_menu = int(input(f'''             
        1. Tambah Unit Sewa
        2. Hapus Unit Sewa
        3. Update Durasi Unit Sewa
        4. Logout
        Masukkan nomor menu yang ingin diakses: '''))

        if adm_menu == 1:
            adm_menu_1()

        elif adm_menu == 2:
            adm_menu_2()

        elif adm_menu == 3:
            adm_menu_3()

        elif adm_menu == 4:
            print(f"Logout berhasil! Sampai jumpa, {username}")
            break

# Program utama
while True:
    menu = int(input('''
        Selamat datang di PurwadhiCar Rental
                     
         1. Cek Ketersediaan Unit
         2. Sewa
         3. Login (Admin Only)
         4. Keluar

        Masukkan nomor menu yang ingin diakses: '''))

    if menu == 1:
        show_unit()

    elif menu == 2:
        menu_sewa()

    elif menu == 3:
        username = menu_login()
        menu_admin(username)

    elif menu == 4:
        break

    else:
        print('\nError. Menu tidak tersedia.')

