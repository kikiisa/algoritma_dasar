#nomor 1

def main(value):
    ganjil = []
    empty  = []
    urutan = 0
    for x in range(0,value):
        urutan+=1
        nilai = int(input(f"Masukan angka {urutan} : "))
        if(nilai % 2 == 0):
            empty.append(nilai)
        else:
            ganjil.append(nilai)
    jml = len(ganjil)
    
    for i in range(0,len(ganjil)-1):
        for j in range(len(ganjil)-1,i,-1):
            if(ganjil[j] < ganjil[j-1]):
                temp = ganjil[j]
                ganjil[j] = ganjil[j-1]
                ganjil[j-1] = temp
    print(f"jumlah bilangan ganjil : {jml}")
    print("-------------------------------")
    print("Jumlah Data Setelah Di Desc")
    for data in ganjil:
        print(data,end=' ')
        
            
num = int(input("Masukan jumlah angka : "))
main(num)
