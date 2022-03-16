import sys
sys.path.append("..")

from modules import stack as st

def tambahKurung(strMat) :

    stack=st.stack()
    jml=1

    for mat in strMat :
        
        if mat == "(" :
            st.push(stack,mat)
        elif mat == ")" :
            if st.isEmpty(stack) :
                return "Kelebihan %d kurung Tutup" % (jml)
            else :
                jml+=1
                st.pop(stack)
    if st.isEmpty(stack) :
        print(stack)
        return "Benar"
    else :
        return "Kelebihan %d Kurung buka" % (st.size(stack))



print(tambahKurung("8*(6+2):(7-1))"))
