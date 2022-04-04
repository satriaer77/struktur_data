namaList = []
nrpList  = []



def tampilkanMahasiswa(nmLst,nrLst):
    print("    NRP     NAMA")

    for i in range(len(nmLst)) :
        print("%d   %s      %s" % (i,nmLst[i],nrLst[i]))


def inputMahasiswa(nmLst,nrLst) :
    jmlMhs = int(input("-> Masukkan jumlah mahasiswa yang akan diinputkan = "))
    for i in range(jmlMhs) :
        print("\n\nMahasiswa ",i)
        nrLst.append(input("=> Ketikkan NRP  Mahasiswa %d  = " % (i)))
        nmLst.append(input("=> Ketikkan Nama Mahasiswa %d  = " % (i)))
 

def cariMahasiswa(nmLst,nrLst,cariNrp):
    print("   NRP     NAMA")

    for i in range(len(nmLst)) :
        if nrLst[i] == cariNrp :
            print("%d   %s      %s" % (i,nmLst[i],nrLst[i]))





lanjut = True 

while lanjut :

    print("""

Daftar Menu 
-----------
1. Tampilkan Mahasiswa
2. Tambah Mahasiswa
3. Cari Mahasiswa berdasar NRP

            """)
    pilih = int(input("=> Masukkan pilihan anda :"))
    if pilih == 1 :
        tampilkanMahasiswa(namaList,nrpList)
    elif pilih == 2 :
        inputMahasiswa(namaList,nrpList)
    elif pilih == 3 :
        cari = input("-> Ketikkan NRP Mahasiswa = ")
        cariMahasiswa(namaList,nrpList,cari)
   
    stp = input("Apakah anda ingin melanjutkan? y/t")

    if stp == "t" :
        lanjut=False
#print(nrpList)


    


