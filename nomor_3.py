mk = ['BTI','PPL','HTI','SPM','FP','MAT','MP','SBP','SIMBADA','SI','SO']
matkul = [
        1,
        {
          "mk":"BTI",
          "kode":"BTI001",
          "sks":3
        },
        {
            "mk":"PPL",
            "kode":"PPL002",
            "sks":3
        },
        {
            "mk":"HTI",
            "kode":"HTI003",
            "sks":3
            },
        {
            "mk":"SPM",
            "kode":"SPM004",
            "sks":2
            },
        {
            "mk":"FP",
            "kode":"FP005",
            "sks":3
            },
        {
            "mk":"MAT",
            "kode":"MAT006",
            "sks":2
            },
        {
            "mk":"MP",
            "kode":"MP007",
            "sks":2
            },
        {
            "mk":"SBP",
            "kode":"SBP008",
            "sks":3
            },
        {
            "mk":"SIMBADA",
            "kode":"SIMBADA009",
            "sks":2
            },
        {
            "mk":"SI",
            "kode":"SI010",
            "sks":3
            },
        {   
            "mk":"SO",
            "kode":"SO011",
            "sks":3
            }
        
    ]

def matkuliah(index):
    hasil = []
    hasil.append(mk[index])
    hasil.append(kode[index])
    hasil.append(sks[index])
    print(hasil)

    
def main():    

    maks_sks = 22
    sks_sekarang = 0
    id_mk = []
    sks_mk = []
    print("---------- Masukan Data ----------")
    data_nama = input("Masukan Nama : ")
    data_nim  = input("Masukan Nim : ")
    semester  = int(input("Masukan Semester : "))
    data_alamat = input("Masukkan Alamat : ")
    urutan = 0
    for daftar in mk:
        urutan+=1
        print(f"{urutan} : {daftar}")
    for jml_mk in range(0,len(mk)):
        data_matakuliah = int(input("Masukkan no menu : "))
        if(data_matakuliah in id_mk):
            print("data sudah ada")
            main()
        else:
            sks_mk.append(matkul[data_matakuliah]["sks"])
            ttl = sum(sks_mk)
            print(f"Total Sks Sekarang yang anda ambil {ttl}")
            id_mk.append(data_matakuliah)
            if(sum(sks_mk) > maks_sks):
                print("Sks telah melebihi batas maksimum")
                break
            else:
                next
    print("-------- KARTU RENCANA STUDY ---------")
    print("Total Sks anda sekarang : ",sum(sks_mk))
    print(f"Nama : {data_nama}")
    print(f"Nim  : {data_nim}")
    print(f"Semester : {semester}")
    print("--------------------------------------")
    print("Daftar yang diambil")
    print("-------------------")
    for my_mk in id_mk:
        print(matkul[my_mk]["mk"])
main()

