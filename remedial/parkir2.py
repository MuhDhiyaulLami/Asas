# Program untuk menghitung biaya parkir berdasarkan jenis kendaraan dan durasi parkir yang dimasukkan oleh pengguna

while True:  # Memulai loop tak terbatas
    # Meminta input dari pengguna untuk jenis kendaraan yang digunakan
    Kendaraan = input('kendaraan yang anda pakai mobil/motor: ')
    
    # Meminta input dari pengguna untuk durasi parkir dalam jam
    durasi = float(input('berapa lama anda parkir: '))
    
    # Memeriksa apakah durasi yang dimasukkan valid (lebih dari 0)
    if durasi <= 0:
        print('masukan data dengan valid')  # Menampilkan pesan jika input tidak valid
        
    # Jika durasi parkir kurang dari atau sama dengan 2 jam
    elif durasi <= 2:
        print('biaya yang harus anda bayar:', 3000)  # Biaya tetap untuk parkir hingga 2 jam
        
    # Jika durasi parkir lebih dari 2 jam tetapi kurang dari atau sama dengan 24 jam
    elif durasi <= 24:
        # Memeriksa jenis kendaraan yang digunakan
        if Kendaraan == 'mobil':
            # Menghitung biaya tambahan untuk mobil setiap jam setelah 2 jam
            print('biaya yang harus anda bayar:', 3000 + (durasi - 2) * 1500)
            
        else:
            # Menghitung biaya tambahan untuk motor setiap jam setelah 2 jam
            print('biaya yang harus anda bayar:', 3000 + (durasi - 2) * 1000)
            
    # Jika durasi parkir lebih dari 24 jam
    else:
        # Memeriksa jenis kendaraan yang digunakan
        if Kendaraan == 'mobil':
            # Menghitung biaya untuk mobil parkir lebih dari 24 jam dengan biaya tambahan
            print('biaya yang harus anda bayar:', 3000 + (durasi - 2) * 1500 + 10000)
        
        else:
            # Menghitung biaya untuk motor parkir lebih dari 24 jam dengan biaya tambahan
            # Namun, biaya tambahan untuk motor lebih dari 24 jam sama dengan mobil
            print('biaya yang harus anda bayar:', 3000 + (durasi - 2) * 1500 + 10000)
            
    # Menanyakan kepada pengguna apakah ingin mengulang program
    kondisi = input('\napakah anda ingin mengulang kembali y/n: ').strip().lower()
    if kondisi != 'y':  # Jika pengguna tidak ingin mengulang
        break  # Keluar dari loop