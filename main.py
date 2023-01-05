while True:
        print(" kalkulator sederhana ".center(50,"-"))
        print(" isi menu ".center(50,"="))
        print("""
    [1] Operasi Aritmetika Dasar
    [2] Operasi Matematika Lanjutan
    [3] Mengubah dan Menentukan Bilangan
    [4] Menghitung Luas Bangun Datar
    [5] Menghitung Keliling Bangun Datar
    [6] exit""")
        opt = int(input("Pilihan anda : "))
        if opt == 1:
            import Kalkulator.Perhitungan
        elif opt == 2:
            import Kalkulator.Perhitungan2    
        elif opt == 3:
            import Kalkulator.Mengubah
        elif opt == 4:
            import Kalkulator.Luas
        elif opt == 5:
             import Kalkulator.Keliling
        elif opt == 6:
            quit = input("\nApakah Kamu Ingin Keluar Program Kalkulator? (y/n) : ")
            if quit == 'y':
                print("Terima Kasih")
                break
            else: continue
        else:
            print("ERROR - Angka yang anda masukan tidak ada di daftar")
