# Program Operasi Matematika
while True:
# Program utama
        print(" Operasi Matematika ".center(50,"-"))
        print("Pilih Perhitungan :")
        print("1. Perpangkatan")
        print("2. Akar")
        print("3. Jarak")
        print("4. Kecepatan")
        print("5. Exit")
    
    # Meminta input dari pengguna
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4/5): "))

# Menghitung hasil sesuai dengan operasi yang diminta
        if pilihan == 1:
    # Fungsi untuk menghitung perpangkatan      
            bilangan = float(input("masukan bilangan:"))
            pangkat = float(input("masukan pangkat:"))
            def hitung_pangkat(bilangan, pangkat):
                if pangkat > 1:
                    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

                return bilangan
            hasil = hitung_pangkat(bilangan, pangkat)
            print(f'Hasil = {hasil}')

        elif pilihan == 2:
    # Fungsi untuk menghitung akar
            import math
            bilangan = float(input("Masukkan bilangan: "))
            def akar_kuadrat(x):
                return math.sqrt(x)
            hasil = akar_kuadrat(bilangan)
            print(f"Akar kuadrat dari {bilangan} adalah {hasil}")
       
        elif pilihan == 3:
    # Fungsi untuk menghitung jarak
            kecepatan = float(input("Masukkan kecepatan (dalam m/s): "))
            waktu = float(input("Masukkan waktu (dalam detik): "))
            def hitung_jarak(kecepatan, waktu):
                hasil = kecepatan * waktu
                return hasil
            print(f"Jarak yang ditempuh {hitung_jarak(kecepatan, waktu)} meter")

        elif pilihan == 4:
    # Fungsi untuk menghitung kecepatan
            jarak = float(input("Masukkan jarak (dalam meter): "))
            waktu = float(input("Masukkan waktu (dalam detik): "))
            def hitung_kecepatan(jarak, waktu):
                hasil = jarak / waktu
                return hasil
            print(f"Kecepatan yang ditempuh {hitung_kecepatan(jarak, waktu)} m/s")  

        elif pilihan == 5:
    # Perintah untuk keluar program  
            quit = input("\nApakah Anda Ingin Keluar Program? (y/n) : ")
            if quit == 'y':
                print("Terima Kasih")
                break
            else: continue
        else:
            print("ERROR - Angka yang anda masukan tidak ada di daftar")  
