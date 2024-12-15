while True: # Memulai perulangan tanpa batas hingga kondisi penghentian terpenuhi
    dimensi = input('Apakah paketmu berdimensi lebih dari 50 x 50 x 50 (y/n)? ')
    berat = float(input('Berapa kilogram paket anda? '))
    kota = input('apakah paket tersebut dikirim ke area kota atau kabupaten pasuruan(y/n)? ')

    if kota == 'n':
        print('Maaf layanan kami hanya terdapat di area kota atau kabupaten pasuruan')
        
    elif berat < 1:
        print('maaf minimal pengiriman adalah 1 kilogram')
        
    elif berat == 1:#menghitung total harga jika berat paket adalah 1 kilogram
        print(8000)
        
    elif dimensi == 'y': #menghitung total harga jika paket berdimensi lebih dari 50 x 50 x 50
        print(50000 + (7000 * berat))
        
    else:#menghitung total harga jika paket berdimensi kurang dari 50 x 50 x 50
        print(5000 * berat)

    kondisi = input('\nApakah ada ingin menggunakan program lagi(y/n)? ').strip().lower()# Meminta input apakah pengguna ingin menjalankan program lagi
    if kondisi != 'y': # jika input tidak sama dengan 'y' akan mengakhiri program
        print('terima kasih telah menggunakan program')
        break