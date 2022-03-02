def cekAngka(akg) :
    strPr = "Prima"
    if isPrime(akg) != True :
        strPr = "Bukan "+strPr

    if akg%2 == 0 :
        print("Angka ",akg," merupakan bilangan genap dan merupakan bilangan ",strPr)
    else :
        print("Angka ",akg," merupakan bilangan ganjil dan merupakan bilangan ",strPr)


def isPrime(akg) :
    prime = True

    for i in range(2,akg) :
        if akg % i == 0 :
            prime = False
            break

    return prime


cekAngka(3)

