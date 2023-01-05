# Program Operasi Aritmetika dasar
while True:
# Program utama
        print(" Operasi Aritmetika dasar ".center(50,"-"))
        print("Pilih Perhitungan :")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Exit")
    
    # Meminta input dari pengguna
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4/5): "))

# Menghitung hasil sesuai dengan operasi yang diminta
        if pilihan == 1:
    # Fungsi untuk menghitung penjumlahan
            angka1 = float(input("Masukkan angka1: "))
            angka2 = float(input("Masukkan angka2: "))
            def hasil_tambah (angka1, angka2):
                hasil = angka1 + angka2
                return hasil
            print(f"hasil penjumlahannya adalah {hasil_tambah(angka1, angka2)}")
    
        elif pilihan == 2:
    # Fungsi untuk menghitung pengurangan
            angka1 = float(input("Masukkan angka1: "))
            angka2 = float(input("Masukkan angka2: "))
            def hasil_kurang (angka1, angka2):
                hasil = angka1 - angka2
                return hasil
            print(f"hasil pengurangannya adalah {hasil_kurang(angka1, angka2)}")
        
        elif pilihan == 3:
     # Fungsi untuk menghitung perkalian        
            angka1 = float(input("Masukkan angka1: "))
            angka2 = float(input("Masukkan angka2: "))
            def hasil_kali (angka1, angka2):
                hasil = angka1 * angka2
                return hasil
            print(f"hasil perkaliannya adalah {hasil_kali(angka1, angka2)}")
        
        elif pilihan == 4:
     # Fungsi untuk menghitung pembagian
            angka1 = float(input("Masukkan angka1: "))
            angka2 = float(input("Masukkan angka2: "))
            def hasil_bagi (angka1, angka2):
                hasil = angka1 / angka2
                return hasil
            print(f"hasil pembagiannya adalah {hasil_bagi(angka1, angka2)}")
        
        elif pilihan == 5:
    # Perintah untuk keluar program  
            quit = input("\nApakah Anda Ingin Keluar Program? (y/n) : ")
            if quit == 'y':
                print("Terima Kasih")
                break
            else: continue
        else:
            print("ERROR - Angka yang anda masukan tidak ada di daftar")