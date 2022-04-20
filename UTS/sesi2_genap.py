def stack ():
    s=[]
    return s
def push (s, data):
    s.append(data)
def pop (s):
    data=s.pop()
    return (data)
def peek (s):
    return (s[len(s)-1])
def isEmpty(s):
    return (s==[])
def size (s):
    return (len(s))
    
def deshek(angka):
    he=stack()
    dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    temp=''

    #untuk ini tadi kamu menggunakan angka > 0 sedangkan pada code di dalam while yaitu
    # menggunakan variabel terpisah seperti tadi
    # mod = angka%16 
    # div = angka//16 
    # maka angkanya tidak akan berkurang malah akan membandingkan angka 126 > 1 tidak akan berhenti karena hasilnya true terus
    while angka > 1:
        print(angka)
        mod   = angka%16
        print("Mod = ",mod)
        
        #ini kalau di kodemu tadi mod == dic.keys() jadi hasil dari modulus akan dibandingkan dengan dic.keys
        # yaitu mod == [10,11,12,13,14,15,16] maka kode di if tidak dijalankan karena tidak sama antara int dengan list
        if mod in dic.keys(): 
            push(he,dic[mod])
        else : 
            print(angka)
            push(he,angka)
    
        angka = angka//16

    while not(isEmpty(he)) :
        temp+=str(pop(he))


    return temp
print(deshek(126)) #7E
