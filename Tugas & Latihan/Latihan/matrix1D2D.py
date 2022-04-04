def buatMatrix1D(sz):
    lst = []
    for i in range(sz) :
        lst.append(int(input("-> ")))
    return lst

def buatMatrix2D(baris,kolom) :
    lstR = []

    for i in range(baris) :
        bar = []
        for j in range(kolom) :
            bar.append(int(input("-> ")))

        lstR.append(bar)
    return lstR 


def jumlahMatrix1D(mat1,mat2) :
    lst = []
    cek = len(mat1)==len(mat2) 
    if cek :
        for i in range(len(mat1)) :
            lst.append(mat1[i]+mat2[i])
        return lst
    else :
        return "ukuran matrix tidak sama"

def jumlahMatrix2D(mat1,mat2) :
    cek = len(mat1) == len(mat2)
    lstR = []

    if cek :
        for i in range(len(mat1)) :
            bar = []
            for j in range(len(mat2)) :
                bar.append(mat1[i][j]+mat2[i][j])
            lstR.append(bar)

    return lstR




def kaliMatrix1D(mat1,mat2) :
    lst = []
    cek = len(mat1)==len(mat2) 
    if cek :
        for i in range(len(mat1)) :
            lst.append(mat1[i]*mat2[i])
        return lst
    else :
        return "ukuran matrix tidak sama"




print("""
Pilih jeni matrix
1. Matrix 1D
2. Matrix 2D


        """)
pilih = int(input("=> Masukkan pilihan = "))

if pilih == 1 :
    size1 = int(input("=> Masukkan ukuran matrix 1 = "))
    mat1 = buatMatrix1D(size1)
    size2 = int(input("=> Masukkan ukuran matrix 2 = "))
    mat2 = buatMatrix1D(size2)
    
    hasilJml = jumlahMatrix1D(mat1,mat2)
    hasilKali = kaliMatrix1D(mat1,mat2)
    print("Hasil penjumlahan matrix = ",hasilJml)
    print("Hasil perkalian matrix = ", hasilKali)

elif pilih ==2 : 
    barisa = int(input("=> Masukkan jumlah baris matrix A : "))
    koloma = int(input("=> Masukkan jumlah kolom matrix A : "))
    matrixa= buatMatrix2D(barisa,koloma)


    barisb = int(input("=> Masukkan jumlah baris matrix B : "))
    kolomb = int(input("=> Masukkan jumlah kolom matrix B : "))
    matrixb= buatMatrix2D(barisb,kolomb)
    
    jmlMat = jumlahMatrix2D(matrixa,matrixb)
    kaliMat= kaliMatrix2D(matrixa,matrixb)


    print("Hasil penjumlahan matrix = ",jmlMat)

