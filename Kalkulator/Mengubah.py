# Program Mengubah dan Menentukan Bilangan
while True:
# Program utama
        print("Mengubah dan Menentukan Bilangan".center(50,"-"))
        print("Pilihan Mengubah dan Menentukan:")
        print("1. KM ke Mil")
        print("2. Mil ke KM")
        print("3. Menentukan Ganjil dan Genap")
        print("4. Menentukan Positif Negatif dan Nol")
        print("5. Exit")
    
    # Meminta input dari pengguna
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4/5): "))

# Menghitung hasil sesuai dengan operasi yang diminta
        if pilihan == 1:
    # Fungsi untuk merubah kilometer ke mil
            kilometer = float(input("Masukan Jumlah Kilometer:"))
            def km_to_miles(kilometer):
                return kilometer / 1.609
            hasil = km_to_miles(kilometer)
            print(f"{kilometer} sama dengan {hasil} mil")

        elif pilihan == 2:
    # Fungsi untuk merubah mil ke kilometer
            mil = float(input("Masukan Jumlah mil:"))
            def miles_to_km(mil):
                return mil * 1.609
            hasil = miles_to_km(mil)
            print(f"{mil} sama dengan {hasil} Kilometer")
    
        elif pilihan == 3:
    # Fungsi untuk menentukan ganjil dan genap
            bilangan = int(input("Masukkan suatu bilangan: "))
            def ganjil_genap(bilangan):
                if bilangan % 2 == 0:
                    return f"{bilangan} adalah bilangan genap"
                else:
                    return f"{bilangan} adalah bilangan ganjil"
            hasil = ganjil_genap(bilangan)
            print(hasil)

        elif pilihan == 4:
    # Fungsi untuk menentukan bilangan positif, negatif dan nol
            bilangan = int(input("Masukkan suatu bilangan: "))
            def positif_negatif_nol(bilangan):
                if bilangan > 0:
                    return f"{bilangan} adalah bilangan positif"
                elif bilangan < 0:
                    return f"{bilangan} adalah bilangan negatif"
                else:
                    return f"{bilangan} adalah bilangan nol"
            hasil = positif_negatif_nol(bilangan)
            print(hasil)

        elif pilihan == 5:
    # Perintah untuk keluar program  
            quit = input("\nApakah Anda Ingin Keluar Program? (y/n) : ")
            if quit == 'y':
                print("Terima Kasih")
                break
            else: continue
        else:
            print("ERROR - Angka yang anda masukan tidak ada di daftar")  
