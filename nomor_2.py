#nomor 2

def kehadiran(nilai):
    hasil = nilai * (10 / 100)
    return hasil

def mid(nilai):
    hasil = nilai * (25 / 100)
    return hasil

def tugas(nilai):
    hasil = nilai * (25 / 100)
    return hasil

def quiz (nilai):
    hasil = nilai * (15 / 100)
    return hasil

def uas (nilai):
    hasil = nilai * (30 / 100)
    return hasil
    
def main(values):
    
    nama = []
    mid  = []
    tugas = []
    quiz = []
    uas = []
    kehadiran = []
    for jumlah in range(0,values):
        print("---------- Masukan Data ----------")
        data_nama = input("Masukan Nama : ")
        data_mid  = float(input("Masukan Nilai Mid : "))
        data_tugas = float(input("Masukkan nilai tugas : "))
        data_quiz = float(input("Masukkan nilai quiz : "))
        data_uas = float(input("Masukkan nilai UAS : "))
        data_hadir = float(input("Masukan jumlah kehadiran : "))
        nama.append(data_nama)
        mid.append(data_mid)
        tugas.append(data_tugas)
        quiz.append(data_quiz)
        uas.append(data_uas)
        kehadiran.append(data_hadir)
        

    print("Daftar Mahasiswa")
    for x in range(0,len(nama)):
        print("--------------------------")
        print("nama mahasiswa : ", nama[x])
        print("nilai mid : ", mid[x])
        print("nilai tugas : ", tugas[x])
        print("nilai quiz : ", quiz[x])
        print("nilai uas : ", uas[x])
        print("nilai Kehadiran : ",kehadiran[x])

jml = int(input("Masukan Jumlah Mahasiswa : "))
main(jml)
                         
