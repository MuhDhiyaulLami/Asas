# Program untuk menghitung biaya parkir berdasarkan durasi parkir yang dimasukkan oleh pengguna

while True:  # Memulai loop tak terbatas
    # Meminta input dari pengguna untuk durasi parkir dalam jam
    durasi = float(input('berapa lama anda parkir: '))
    
    # Memeriksa apakah durasi yang dimasukkan valid (lebih dari 0)
    if durasi <= 0:
        print('masukan data dengan valid!')  # Menampilkan pesan jika input tidak valid
        
    # Jika durasi parkir kurang dari atau sama dengan 2 jam
    elif durasi <= 2:
        biaya = 3000  # Biaya tetap untuk parkir hingga 2 jam
        print('biaya yang harus anda bayar:', biaya)  # Menampilkan biaya yang harus dibayar
        
    # Jika durasi parkir lebih dari 2 jam tetapi kurang dari atau sama dengan 24 jam
    elif durasi <= 24:
        # Menghitung biaya tambahan untuk setiap jam setelah 2 jam
        biaya2 = 3000 + (durasi - 2) * 1500
        print('biaya yang harus anda bayar:', biaya2)  # Menampilkan total biaya
        
    # Jika durasi parkir lebih dari 24 jam
    else:
        # Menghitung biaya untuk parkir lebih dari 24 jam dengan biaya tambahan
        biaya3 = 3000 + (durasi - 2) * 1500 + 5000
        print('biaya yang harus anda bayar:', biaya3)  # Menampilkan total biaya
        
    # Menanyakan kepada pengguna apakah ingin mengulang program
    kondisi = input('\napakah anda ingin mengulang kembali y/n: ').strip().lower()
    if kondisi != 'y':  # Jika pengguna tidak ingin mengulang
        break  # Keluar dari loop