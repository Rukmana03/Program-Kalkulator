# Program menghitung luas bangun datar
while True:
# Program utama
        print(" Menghitung luas Bangun Datar ".center(50,"-"))
        print("Pilih bangun datar yang ingin dicari luasnya:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Exit")

# Meminta input dari user
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4/5): "))

# Menghitung luas sesuai dengan pilihan user
        if pilihan == 1:
    # Fungsi untuk menghitung luas persegi
            sisi = float(input("Masukkan sisi: "))
            def luas_persegi(sisi):
                luas = sisi * sisi
                return luas
            print(f"Luas persegi adalah {luas_persegi(sisi)}")
        
        elif pilihan == 2:
     # Fungsi untuk menghitung luas persegi panjang        
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            def luas_persegi_panjang(panjang, lebar):
                luas = panjang * lebar
                return luas
            print(f"Luas persegi panjang adalah {luas_persegi_panjang(panjang, lebar)}")
        
        elif pilihan == 3:
    # Fungsi untuk menghitung luas segitiga
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            def luas_segitiga(alas, tinggi):
                luas = alas * tinggi / 2
                return luas
            print(f"Luas segitiga adalah {luas_segitiga(alas, tinggi)}")
        
        elif pilihan == 4:
    # Fungsi untuk menghitung luas lingkaran
            jari_jari = float(input("Masukkan jari-jari: "))
            def luas_lingkaran(jari_jari):
                luas = 3.14 * jari_jari * jari_jari
                return luas
            print(f"Luas lingkaran adalah {luas_lingkaran(jari_jari)}")
        
        elif pilihan == 5:
    # Perintah untuk keluar program  
            quit = input("\nApakah Anda Ingin Keluar Program? (y/n) : ")
            if quit == 'y':
                print("Terima Kasih")
                break
            else: continue
        else:
            print("ERROR - Angka yang anda masukan tidak ada di daftar")
        
        
