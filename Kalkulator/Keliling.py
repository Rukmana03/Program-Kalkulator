# Program menghitung keliling bangun datar
while True:
# Program utama
        print(" Menghitung Keliling Bangun Datar ".center(50,"-"))
        print("Pilih bangun datar yang ingin dicari kelilingnya:")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Trapesium")
        print("5. Exit")

# Meminta input dari user
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4/5): "))

# Menghitung keliling sesuai dengan pilihan user
        if pilihan == 1:
    # Fungsi untuk menghitung keliling persegi
            sisi = float(input("Masukkan panjang sisi: "))
            def keliling_persegi(sisi):
                return 4 * sisi
            print("Keliling persegi adalah", keliling_persegi(sisi))

        elif pilihan == 2:
    # Fungsi untuk menghitung keliling lingkaran
            diameter = float(input("Masukkan diameter: "))
            import math
            def keliling_lingkaran(diameter):
                return math.pi * diameter
            print("Keliling lingkaran adalah", keliling_lingkaran(diameter))

        elif pilihan == 3:
    # Fungsi untuk menghitung keliling segitiga
            sisi1 = float(input("Masukkan panjang sisi 1: "))
            sisi2 = float(input("Masukkan panjang sisi 2: "))
            sisi3 = float(input("Masukkan panjang sisi 3: "))
            def keliling_segitiga(sisi1, sisi2, sisi3):
                return sisi1 + sisi2 + sisi3
            print("Keliling segitiga adalah", keliling_segitiga(sisi1, sisi2, sisi3))

        elif pilihan == 4:
    # Fungsi untuk menghitung keliling trapesium
            sisi1 = float(input("Masukkan panjang sisi 1: "))
            sisi2 = float(input("Masukkan panjang sisi 2: "))
            tinggi = float(input("Masukkan tinggi: "))
            def keliling_trapesium(sisi1, sisi2, tinggi):
                return sisi1 + sisi2 + 2 * tinggi
            print("Keliling trapesium adalah", keliling_trapesium(sisi1, sisi2, tinggi))
        
        elif pilihan == 5:
    # Perintah untuk keluar program
            quit = input("\nApakah Anda Ingin Keluar Program? (y/n) : ")
            if quit == 'y':
                print("Terima Kasih")
                break
            else: continue
        else:
            print("ERROR - Angka yang anda masukan tidak ada di daftar")